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
	  #, fedfind.release.get_release(27)
      fedfind.release.get_release(27, 'Beta')
    , fedfind.release.get_release(26)
    , fedfind.release.get_release(25)
    , fedfind.release.get_release(24)
    ]

for rel in releases_to_report:
    for img in rel.all_images:
        location = img['url']
        h = hashify(
                rel.version,
                rel.milestone,
                img['arch'],
                location,
                img['variant'],
                img['subvariant'])
        output.append(h)

print json.dumps(output)
