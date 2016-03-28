#!/usr/bin/python
""" Return the AMIs uploaded by fedimg for a given set of release vars.

Search datagrepper to find the results.

Deps:  $ sudo dnf install python-requests

Author:     Ralph Bean <rbean@redhat.com>
License:    LGPLv2+
"""

from __future__ import print_function

import collections
import functools
import logging
import os

import requests
import dogpile.cache

log = logging.getLogger('fedimg_vars')

base_url = 'https://apps.fedoraproject.org/datagrepper/raw'
topic = "org.fedoraproject.prod.fedimg.image.upload"

session = requests.session()

cache = dogpile.cache.make_region().configure(
    "dogpile.cache.dbm",
    # 'make clean' does not remove this cache, but we let the values expire
    # once every this many seconds (once a day)
    expiration_time=86400,
    arguments={
        "filename": os.path.join(os.getcwd(), 'build/amis.cache')
    },
)

def get_page(page, pages, target):
    """ Retrieve the JSON for a particular page of datagrepper results """
    log.debug("Getting page %i of %s", page, pages)
    response = session.get(base_url, params=dict(
        topic=topic,
        page=page,
        contains=target,
        rows_per_page=100,
    ))
    return response.json()


def get_messages(target):
    """ Generator that yields messages from datagrepper """

    # Get the first page
    data = get_page(1, 'unknown', target)
    for message in data['raw_messages']:
        yield message

    more = functools.partial(get_page, pages=data['pages'], target=target)

    # Get all subsequent pages (if there are any...)
    for page in range(1, data['pages']):
        data = more(page + 1)

        for message in data['raw_messages']:
            yield message

# We cache this guy on disk for 500s
@cache.cache_on_arguments()
def collect(release):
    results = collections.defaultdict(dict)

    # 1 - transform release vars into an image name we want to query for
    templates = [
        # The F22 released AMIs uploads didn't appear to go through fedimg, so
        # we can't use this scheme for them.  Stuff for F23 should all go that
        # route though, so we can hopefully switch over soon.
        ("Fedora-Cloud-Base-{curr_cloud_id}-{composedate}.x86_64", {
            'HVM_base_AMI':     lambda e: e.get('virt_type') == 'hvm' and e.get('vol_type') == 'standard',
            'GP2_HVM_base_AMI': lambda e: e.get('virt_type') == 'hvm' and e.get('vol_type') == 'gp2',
            'PV_base_AMI':      lambda e: e.get('virt_type') == 'paravirtual' and e.get('vol_type') == 'standard',
            'GP2_PV_base_AMI':  lambda e: e.get('virt_type') == 'paravirtual' and e.get('vol_type') == 'gp2',
        }),
        ("Fedora-Cloud-Atomic-{curr_cloud_id}-{atomic_composedate}.x86_64", {
            'HVM_atomic_AMI':     lambda e: e.get('virt_type') == 'hvm' and e.get('vol_type') == 'standard',
            'GP2_HVM_atomic_AMI': lambda e: e.get('virt_type') == 'hvm' and e.get('vol_type') == 'gp2',
        }),
        ("Fedora-Cloud-Base-{next_cloud_AMI_id}_{curr_cloud_AMI_state}-{RC_pre_gold}.x86_64", {
            'pre_HVM_base_AMI':     lambda e: e.get('virt_type') == 'hvm' and e.get('vol_type') == 'standard',
            'pre_GP2_HVM_base_AMI': lambda e: e.get('virt_type') == 'hvm' and e.get('vol_type') == 'gp2',
            'pre_PV_base_AMI':      lambda e: e.get('virt_type') == 'paravirtual' and e.get('vol_type') == 'standard',
            'pre_GP2_PV_base_AMI':  lambda e: e.get('virt_type') == 'paravirtual' and e.get('vol_type') == 'gp2',
        }),
        #("Fedora-Cloud-Atomic-{next_cloud_AMI_id}_{curr_cloud_AMI_state}-{manual_pre_cloud_AMI_atomic_composedate}.x86_64", {
        #    'pre_HVM_atomic_AMI':     lambda e: e.get('virt_type') == 'hvm' and e.get('vol_type') == 'standard',
        #    'pre_GP2_HVM_atomic_AMI': lambda e: e.get('virt_type') == 'hvm' and e.get('vol_type') == 'gp2',
        #}),
    ]

    for template, buckets in templates:
        # 2 - Build an intermediary dict
        intermediary = collections.OrderedDict()
        target = template.format(**release)
        log.info("Looking for AMIs for %s" % target)

        messages = get_messages(target)
        for message in messages:
            key = message['msg']['image_name']
            if not key in intermediary:
                intermediary[key] = []
            intermediary[key].append(message['msg'])

        if not intermediary:
            log.warn("No AMIs found for %s" % target)
            continue

        # What would this even mean?
        assert len(intermediary) < 2, "Impossible.  Got more than one target."

        uploads = intermediary[target]

        # 3- transform intermediary representation into results
        for name, matches in buckets.items():
            for upload in uploads:
                if matches(upload['extra']):
                    ami = upload['extra']['id']
                    # The region looks like "EC2 (REGION)", so we strip stuff.
                    region = upload['destination'][5:-1]
                    results[name][region] = ami

    return results


def sanity_check(globalvar, collected_fedimg_vars):
    """ This is a sanity check just to make sure the datagrepper code is not
    way off from what we had hand-typed before.

    Eventually, remove this.
    """

    names = [
        'pre_HVM_base_AMI',
        'pre_GP2_HVM_base_AMI',
        'pre_PV_base_AMI',
        'pre_GP2_PV_base_AMI',
        'pre_HVM_atomic_AMI',
        'pre_GP2_HVM_atomic_AMI',
    ]
    for name in names:
        handtyped = getattr(globalvar, name)
        collected = collected_fedimg_vars[name]

        for key in handtyped:
            if not key in collected:
                log.warn("collected %r is missing %r" % (name, key))

        for key in collected:
            if not key in handtyped:
                log.warn("handtyped %r is missing %r" % (name, key))
