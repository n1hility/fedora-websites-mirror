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
from datetime import datetime, timedelta
from hashlib import sha1
import logging
import shelve
import os

from fedimg_vars_lib import get_messages, sanity_check, mocked_fedimg, check_permissions

logging.basicConfig(level=logging.INFO)

log = logging.getLogger('fedimg_vars')

cachefile = '/tmp/fedora_websites_fedimg_getfedora_%s.cache'


# We cache this guy on disk for 500s
def collect(release):
    filename = cachefile % (sha1(str(release)).hexdigest())
    shelf = shelve.open(filename)
    check_permissions(filename=filename)
    if shelf.get('timestamp') and shelf.get('timestamp') > (datetime.utcnow() - timedelta(hours=1)):
        log.info('Retrieving release data from shelf')
        toreturn = shelf['collected']
        shelf.close()
        return toreturn

    results = collections.defaultdict(dict)

    # 1 - transform release vars into an image name we want to query for
    templates = [
        # The F22 released AMIs uploads didn't appear to go through fedimg, so
        # we can't use this scheme for them.  Stuff for F23 should all go that
        # route though, so we can hopefully switch over soon.
        #("Fedora-Cloud-Base-{curr_cloud_AMI_id}-{cloud_AMI_composedate}.n.0.x86_64", {
        #    'HVM_base_AMI':     lambda e: e.get('virt_type') == 'hvm' and e.get('vol_type') == 'standard',
        #    'GP2_HVM_base_AMI': lambda e: e.get('virt_type') == 'hvm' and e.get('vol_type') == 'gp2',
        #    'PV_base_AMI':      lambda e: e.get('virt_type') == 'paravirtual' and e.get('vol_type') == 'standard',
        #    'GP2_PV_base_AMI':  lambda e: e.get('virt_type') == 'paravirtual' and e.get('vol_type') == 'gp2',
        #}),
        ("Fedora-AtomicHost-{curr_atomic_id}-{atomic_composedate}.x86_64", {
           'HVM_atomic_AMI':     lambda e: e.get('virt_type') == 'hvm' and e.get('vol_type') == 'standard',
           'GP2_HVM_atomic_AMI': lambda e: e.get('virt_type') == 'hvm' and e.get('vol_type') == 'gp2',
        }),
        ("Fedora-AtomicHost-{curr_atomic_id}-{atomic_composedate}.aarch64", {
            'AARCH64_GP2_HVM_atomic_AMI': lambda e: e.get('virt_type') == 'hvm' and e.get('vol_type') == 'gp2',
        }),
        #("Fedora-Cloud-Base-{next_cloud_AMI_id}_{curr_cloud_AMI_state}-{RC_pre_gold}.x86_64", {
        #    'pre_HVM_base_AMI':     lambda e: e.get('virt_type') == 'hvm' and e.get('vol_type') == 'standard',
        #   'pre_GP2_HVM_base_AMI': lambda e: e.get('virt_type') == 'hvm' and e.get('vol_type') == 'gp2',
        #    'pre_PV_base_AMI':      lambda e: e.get('virt_type') == 'paravirtual' and e.get('vol_type') == 'standard',
        #    'pre_GP2_PV_base_AMI':  lambda e: e.get('virt_type') == 'paravirtual' and e.get('vol_type') == 'gp2',
        #}),
        #("Fedora-Cloud-Atomic-{next_cloud_AMI_id}_{curr_cloud_AMI_state}-{manual_pre_cloud_AMI_atomic_composedate}.x86_64", {
        #    'pre_HVM_atomic_AMI':     lambda e: e.get('virt_type') == 'hvm' and e.get('vol_type') == 'standard',
        #    'pre_GP2_HVM_atomic_AMI': lambda e: e.get('virt_type') == 'hvm' and e.get('vol_type') == 'gp2',
        #}),
    ]

    if not os.path.exists('/var/fedora_websites_live_fedimg'):
        return mocked_fedimg(templates)

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
                    region = upload['destination']
                    results[name][region] = ami

    shelf['timestamp'] = datetime.utcnow()
    shelf['collected'] = results
    shelf.close()

    return results
