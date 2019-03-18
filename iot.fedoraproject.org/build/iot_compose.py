import requests
import sys

try:
    sys.path.append('../../build.d')

    import globalvar
except ImportError:
    print "Unable to import globalvar"
    sys.exit(1)

VERSION = globalvar.release['curr_iot_id']
BASEURL = 'https://dl.fedoraproject.org/pub/alt/iot/' + VERSION + '/'

def iot_compose_links():
    json = requests.get(BASEURL + '/metadata/images.json').json()

    date = json['payload']['compose']['date']

    links = {}
    links['date'] = date[0:4] + '-' + date[4:6] + '-' + date[6:8]
    links['type'] = {}

    for arch,lst in json['payload']['images']['IoT'].iteritems():
        if arch == 'armhfp':
            continue
        for img in lst:
            if img['type'] not in links['type'].keys():
                links['type'][img['type']] = {}

            links['type'][img['type']][img['arch']] = BASEURL + img['path']

    return links
