#!/usr/bin/python
""" Shared functions between the two fedimg_vars.py scripts

Search datagrepper to find the results.

Deps:  $ sudo dnf install python-requests

Author:     Ralph Bean <rbean@redhat.com>
License:    LGPLv2+
"""

from __future__ import print_function

import collections
import copy
from datetime import datetime, timedelta
import functools
import logging
import json
import os

import requests

log = logging.getLogger('fedimg_vars')

cache_file = '/tmp/fedora_websites_fedimg.cache'
dateformat = '%Y-%m-%dT%H:%MZ'
base_url = 'https://apps.fedoraproject.org/datagrepper/raw'
topic = "org.fedoraproject.prod.fedimg.image.upload"

session = requests.session()

def get_page(page, pages):
    """ Retrieve the JSON for a particular page of datagrepper results """
    log.debug("Getting page %i of %s", page, pages)
    response = session.get(base_url, params=dict(
        topic=topic,
        page=page,
        # Get messages from 28 weeks (7 months)
        delta=16934400,
        rows_per_page=100,
    ))
    return response.json()


def retrieve_messages():
    """ Generator that yields messages from datagrepper """
    # Get the first page
    data = get_page(1, 'unknown')
    for message in data['raw_messages']:
        yield message

    more = functools.partial(get_page, pages=data['pages'])

    # Get all subsequent pages (if there are any...)
    for page in range(1, data['pages']):
        data = more(page + 1)

        for message in data['raw_messages']:
            yield message


def filter_messages(messages, target):
    for message in messages:
        if target in str(message) and 'completed' in str(message):
            yield message


def get_messages(target):
    """ Filter the messages on target. """
    try:
        with open(cache_file, 'r') as cf:
            cache = json.load(cf)
            cachetime = datetime.strptime(cache['timestamp'], dateformat)
            if cachetime > (datetime.utcnow() - timedelta(days=1)):
                return filter_messages(cache['messages'], target)
    except:
        log.info('No cache, loading from scratch')

    messages = list(retrieve_messages())
    with open(cache_file, 'w') as cf:
        cache = {'timestamp': datetime.utcnow().strftime(dateformat),
                 'messages': messages}
        json.dump(cache, cf)

    return filter_messages(messages, target)


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


def mocked_fedimg(templates):
    regions = ['us-east-1', 'ap-northeast-1', 'sa-east-1', 'ap-southeast-1', 'ap-southeast-2',
               'us-west-2', 'us-west-1', 'eu-central-1', 'eu-west-1', 'ap-northeast-2',
               'ap-south-1', 'ca-central-1', 'eu-west-2']
    mockdata = {}
    for region in regions:
        mockdata[region] = 'ami-mocked'
    toreturn = {}
    for template in templates:
        for restype in template[1].keys():
            toreturn[restype] = copy.copy(mockdata)
    return toreturn
