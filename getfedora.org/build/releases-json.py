#!/usr/bin/env python

import fedfind.release
import fedfind.helpers
import json

output = []

def hashify(version, milestone, arch, link, variant, subvariant):
    return { 'version': version
           , 'arch': arch
           , 'link': link
           , 'variant': variant
           , 'subvariant': subvariant
           }

releases_to_report = [
      fedfind.release.get_release(26)
    , fedfind.release.get_release(26, 'Beta')
    , fedfind.release.get_release(26, 'Alpha')
    , fedfind.release.get_release(25)
    , fedfind.release.get_release(25, 'Beta')
    , fedfind.release.get_release(25, 'Alpha')
    , fedfind.release.get_release(24)
    , fedfind.release.get_release(24, 'Beta')
    , fedfind.release.get_release(24, 'Alpha')
    ]

for rel in releases_to_report:
    for img in rel.all_images:
        location = "/".join((rel.location, img['path']))
        h = hashify(
                rel.version,
                rel.milestone,
                img['arch'],
                location,
                img['variant'],
                img['subvariant'])
        output.append(h)

print json.dumps(output)
