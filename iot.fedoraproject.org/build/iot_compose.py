import requests
import sys

try:
    sys.path.append('../../build.d')

    import globalvar
except ImportError:
    print "Unable to import globalvar"
    sys.exit(1)

IOT_ARCHES = ['x86_64', 'aarch64']
VERSION = globalvar.release['curr_iot_id']

def iot_compose_links():
    compose = requests.get(
        'https://kojipkgs.fedoraproject.org/compose/iot/latest-Fedora-IoT-' +
         VERSION + '/COMPOSE_ID').text

    date = compose.split('-')[-1].split('.')[0]

    links = {}
    links['date'] = date[0:4] + '-' + date[4:6] + '-' + date[6:8]
    links['arches'] = {}

    for arch in IOT_ARCHES:
        if arch not in links['arches'].keys():
            links['arches'][arch] = {}
        compose_iso = compose.replace(
            'Fedora-IoT',
            'Fedora-IoT-dvd-' + arch)

        links['date'] = date[0:4] + '-' + date[4:6] + '-' + date[6:8]
        links['arches'][arch]['iso'] = 'https://kojipkgs.fedoraproject.org/compose/' +\
                      'iot/latest-Fedora-IoT-' + VERSION + '/compose/IoT/' +\
                      arch + '/iso/' + compose_iso + '.iso'
    return links
