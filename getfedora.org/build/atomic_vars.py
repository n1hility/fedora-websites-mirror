#!/usr/bin/python
""" Return the results of the atomic release engine from datagrepper.

For the Two-Week Atomic Change (F23)

Deps:  $ sudo dnf install python-requests

Author:     Ralph Bean <rbean@redhat.com>
License:    LGPLv2+
"""

from __future__ import print_function

import collections
import functools
import json
import logging
import os
import socket

from datetime import datetime, timedelta

import dateutil.relativedelta
import dateutil.tz
import dogpile.cache
import requests

log = logging.getLogger("atomic_vars")

base_url = 'https://apps.fedoraproject.org/datagrepper/raw'
topic = "org.fedoraproject.prod.releng.atomic.twoweek.complete"

UTC = dateutil.tz.tzutc()

session = requests.session()

cache = dogpile.cache.make_region().configure(
    "dogpile.cache.dbm",
    # 'make clean' does not remove this cache, but we let the values expire
    # once every this many seconds (once a day)
    expiration_time=86400,
    arguments={
        "filename": os.path.join(os.getcwd(), 'build/atomic.cache')
    },
)

# Are we running in fedora-infra or on someone's laptop?
hostname = socket.gethostname()
if '.phx2.fedoraproject.org' in hostname:
    DL_URL_PREFIX = 'http://dl.phx2.fedoraproject.org'
else:
    DL_URL_PREFIX = 'https://dl.fedoraproject.org'

download_fpo = 'https://dl.fedoraproject.org'


def get_page(page, pages):
    """ Retrieve the JSON for a particular page of datagrepper results """
    log.debug("Getting page %i of %s", page, pages)
    params = dict(
        start=1441402109,  # the timestamp of when we first started doing this
        topic=topic,
        page=page,
        rows_per_page=1,
    )
    response = session.get(base_url, params=params)
    if not bool(response):
        raise IOError("Failed to talk to %r %r" % (response.url, response))
    return response.json()


# A list of fedmsg messages ideas that were produced erroneously.
# We don't want to use them, so ban them from our results.
blacklist = [
    '2016-dd05c4b7-958b-439f-90d6-e5ca0af2197c',
    '2016-b2a2eb00-acef-4a1f-bc6a-ad5aa9d81eee',
    '2016-0307f681-1eae-4aeb-9126-8a43b7a378e2',
]

def get_messages(target):
    """ Generator that yields messages from datagrepper """

    # Get the first page
    data = get_page(1, 'unknown')
    for message in data['raw_messages']:
        if message['msg_id'] in blacklist:
            continue
        if target in json.dumps(message):
            yield message

    more = functools.partial(get_page, pages=data['pages'])

    # Get all subsequent pages (if there are any...)
    for page in range(1, data['pages']):
        data = more(page + 1)

        for message in data['raw_messages']:
            if message['msg_id'] in blacklist:
                continue
            if target in json.dumps(message):
                yield message


def make_templates(release):
    return [
        # As things stand now, we only do two-week-atomic stuff for the current
        # stable release.
        (release['curr_id'], '', ''),

        # If we ever move to doing pre-release versions as well, just uncomment
        # the following line and it should all work. We leave it commented out
        # now because querying datagrepper for pre-release results that are not
        # there is much more slow than querying for something that exists.
        #(release['next_id'], 'pre_cloud_', 'pre_'),
    ]


# We cache this guy on disk so we don't hit datagrepper over and over.
@cache.cache_on_arguments()
def collect(release):
    results = collections.defaultdict(dict)

    for idx, composedate_prefix, iso_size_prefix in make_templates(release):

        log.info("Looking for latest atomic release for %s" % idx)
        # Get the *latest* atomic release information.
        messages = get_messages('-%s-' % idx)
        try:
            message = messages.next()
        except StopIteration:
            log.warn("Couldn't find any two-week-atomic content for %r" % idx)
            continue

        # Parse the composedate out of the image_name
        image_name = message['msg']['atomic_qcow2']['image_name']
        composedate = '.'.join(image_name.split('-')[-1].split('.')[:-2])
        log.info("    Found composedate: %s" % composedate)
        results['release'][composedate_prefix + 'atomic_composedate'] = composedate

        # Save the timestamp so we can compute the age later, off-cache.
        results['release'][composedate_prefix + 'atomic_ts'] = message['timestamp']

        # Get the sizes of the isos in megabytes.  To do this, we need...
        # A mapping between what the release-engine tool calls each artifact,
        # and what we call them.
        mapping = {
            'atomic_qcow2': 'atomic_qcow2_cloud',
            'atomic_raw': 'atomic_raw_cloud',
            'atomic_vagrant_libvirt': 'atomic_libvag_cloud',
            'atomic_vagrant_virtualbox': 'atomic_VBvag_cloud',
        }
        for key, entry in message['msg'].items():
            # There are some other keys in there we don't care about.
            if not key.startswith('atomic_'):
                continue

            # Do an HTTP HEAD to find the size of the file in megabytes
            url = entry['image_url']
            download_url = entry['image_url']
            if not url.startswith('http'):
                url = DL_URL_PREFIX + url
                download_url = download_fpo + entry['image_url']
            response = requests.head(url)
            if not bool(response):
                log.error("Failed to HEAD %s for size.  %r" % (url, response))
                continue

            length = int(response.headers['content-length']) / 1000000

            # Provide the download URL
            url_key = mapping[key] + "_url"
            results['release'][url_key] = download_url

            # Figure out which of our vars we're going to set, and set it
            iso_size_key = iso_size_prefix + mapping[key]
            results['iso_size'][iso_size_key] = str(length)

    return results


# Note, this is *not* cached, since we need to update it frequently.
def update_age(release):
    """ Is it old and stale?

    We aim to produce new atomic releases every two weeks at minimum.  If we're
    older than two weeks, we should put up a warning on the websites.  Here we
    just compute a flag that gets checked in the template.  If this latest
    release if younger than two weeks, call it "fresh".  If it is older than
    two weeks, it is no longer fresh.
    http://taiga.cloud.fedoraproject.org/project/acarter-fedora-docker-atomic-tooling/us/31
    """

    results = collections.defaultdict(dict)
    for idx, composedate_prefix, iso_size_prefix in make_templates(release):
        two_weeks_ago = datetime.now(UTC) - timedelta(days=14)
        timestamp = release[composedate_prefix + 'atomic_ts']
        latest = datetime.fromtimestamp(timestamp, UTC)
        freshness = bool(latest >= two_weeks_ago)
        relative_delta = datetime.now(UTC) - latest
        casual_delta = relative_delta.days
        results['release'][composedate_prefix + 'atomic_freshness'] = freshness
        results['release'][composedate_prefix + 'atomic_age'] = casual_delta
    return results
