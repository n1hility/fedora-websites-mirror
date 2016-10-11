#!/usr/bin/python
# -*- coding: utf-8 -*-
# This file defines all variable needed to be edited during the release cycle (alpha, beta...).
release={
    'prev_id':     '23',
    'curr_id':     '24',
    'next_id':     '25',
    'curr_name':   '',
    'next_name':   '',
    'curr_state':  'Beta',        # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_arm_state':  'Beta',         # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_ppc64_state':  'Beta',       # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_s390_state':  'Beta',        # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_cloud_state':  'Beta',       # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_cloud_AMI_state':  'Beta',   # either 'Alpha', 'Beta' or '' (i.e empty)
    'prev_arm_id': '23',
    'prev_ppc64_id': '23',
    'prev_s390_id': '23',
    'prev_cloud_id': '23',
    'curr_arm_id': '24',
    'curr_ppc64_id': '24',
    'curr_s390_id': '24',
    'curr_cloud_id': '24',
    'curr_cloud_AMI_id': '24',
    'next_arm_id': '25',
    'next_ppc64_id': '25',
    'next_s390_id': '25',
    'next_cloud_id': '25',
    'next_cloud_AMI_id': '25',
    'composedate': '20160616',
    'unofficial_compose': '20160614',
    # Note that atomic values here get overwritten by the twoweek script.
    'atomic_composedate': '20160616',
    'pre_cloud_composedate': '20150915',
    'cloud_AMI_composedate': '20160616',
    'pre_cloud_AMI_composedate': '20160507',
    'manual_cloud_composedate': '20160616',
    'manual_pre_cloud_composedate': '20160101',
    'manual_pre_cloud_atomic_composedate': '20160101',
    'manual_pre_cloud_AMI_atomic_composedate': '20160101',
    # Note that atomic values here get overwritten by the twoweek script.
    'pre_cloud_atomic_composedate': '20150915',
    'pre_cloud_AMI_atomic_composedate': '20150915',
    'RC_gold': '1.2',             # insert the number of the RC version declared GOLD
    'RC_build': '1.2',            # sometimes releng use the RC build
    'RC_pre_gold': '1.1',         # insert the number of the prerelease RC version declared GOLD
    'RC_pre_build': '1',          # sometimes releng use the RC build

    'atomic_freshness': False,
    'atomic_age': '???',
    'pre_cloud_atomic_freshness': False,
    'pre_cloud_atomic_age': '???',
}

path={
    'torrent':         'https://torrent.fedoraproject.org/torrents',
    'torrent_spins':   'https://torrent.fedoraproject.org/torrents',
    'download':        'https://download.fedoraproject.org/pub/fedora/linux/releases',
    'dl':              'https://download.fedoraproject.org/pub/fedora/linux/updates',
    'download_spins':  'https://download.fedoraproject.org/pub/alt/releases',
    'download_atomic': 'https://download.fedoraproject.org/pub/alt/atomic',
    'download_arch':   'https://download.fedoraproject.org/pub/fedora-secondary/releases',
    'mirrors':         'https://mirrors.fedoraproject.org/metalink?path=pub/fedora/linux/releases',
    'checksums':       './static/checksums',
    'doc':             'https://docs.fedoraproject.org/en-US/Fedora',
    'doc':             'https://docs.fedoraproject.org/en-US/Fedora',
    'unofficial':      'https://dl.fedoraproject.org/pub/alt/unofficial/releases',
}

iso_size={

    #Media
    'macosx':             '20.7',       # In MB
    'windows':            '14.2',       # In MB

    # Legacy
    'x86_64_DVD':          '4.3',       # In GB
    'i386_DVD':            '4.4',       # In GB
    'source_DVD':          '9.2',       # In GB
    'i686_Live_Desktop':   '922',       # In MB
    'x86_64_Live_Desktop': '953',       # In MB
    'i386_Netinstall':     '357',       # In MB
    'x86_64_Netinstall':   '321',       # In MB
    'PPC64_DVD':           '4.3',       # In GB
    'PPC64_Netinstall':    '340',       # In MB
    's390_DVD':            '4.6',       # In GB
    'i686_sda.qcow2':      '212',       # In MB
    'x86_64_sda.qcow2':    '207',       # In MB
    'i686_raw':            '122',       # In MB
    'x86_64_raw':          '117',       # In MB
    # Lives
    'i686_Live_KDE':       '1.2',       # In GB
    'x86_64_Live_KDE':     '1.2',       # In GB
    'i686_Live_LXDE':      '964',       # In MB
    'x86_64_Live_LXDE':    '837',       # In MB
    'i686_Live_Xfce':      '891',       # In MB
    'x86_64_Live_Xfce':    '916',       # In MB
    'i686_Live_Mate':      '1.2',       # In GB
    'x86_64_Live_Mate':    '1.3',       # In GB
    'i686_Live_Soas':      '676',       # In MB
    'x86_64_Live_Soas':    '699',       # In MB
    'i686_Live_Cinnamon':   '1.2',       # In GB
    'x86_64_Live_Cinnamon': '1.2',       # In GB
    # Lives prerelease
    'pre_i686_Live_KDE':    '1.4',       # In GB
    'pre_x86_64_Live_KDE':  '1.3',       # In GB
    'pre_i686_Live_LXDE':   '1.0',       # In GB
    'pre_x86_64_Live_LXDE': '910',       # In MB
    'pre_i686_Live_Xfce':   '1.1',       # In GB
    'pre_x86_64_Live_Xfce': '1.0',       # In GB
    'pre_i686_Live_Mate':   '1.4',       # In GB
    'pre_x86_64_Live_Mate': '1.4',       # In GB
    'pre_i686_Live_Soas':   '763',       # In MB
    'pre_x86_64_Live_Soas': '684',       # In MB
    'pre_i686_Live_Cinnamon': '1.4',     # In GB
    'pre_x86_64_Live_Cinnamon': '1.3',   # In GB
    # Spins
    'i686_Live_Security':  '1.2',       # In GB
    'x86_64_Live_Security':'1.1',       # In GB
    'i686_Live_Games':     '3.8',       # In GB
    'x86_64_Live_Games':   '3.6',       # In GB
    'i686_Live_Elab':      '2.5',       # In GB
    'x86_64_Live_Elab':    '2.5',       # In GB
    'i686_Live_Design':    '1.9',       # In GB
    'x86_64_Live_Design':  '1.8',       # In GB
    'i686_Live_Sci-kde':   '3.2',       # In GB
    'x86_64_Live_Sci-kde': '2.9',       # In GB
    'i686_Live_Robotics':  '2.7',       # In GB
    'x86_64_Live_Robotics':'2.4',       # In GB
    'i686_Live_Jam':       '1.7',       # In GB
    'x86_64_Live_Jam':     '1.7',       # In GB
    'i686_Live_Astronomy': '2.5',       # In GB
    'x86_64_Live_Astronomy':'2.3',      # In GB
    # Spins prerelease
    'pre_i686_Live_Security':  '1.1',   # In GB
    'pre_x86_64_Live_Security':'1.1',   # In GB
    'pre_i686_Live_Games':     '3.8',   # In GB
    'pre_x86_64_Live_Games':   '3.7',   # In GB
    'pre_i686_Live_Elab':      '2.5',   # In GB
    'pre_x86_64_Live_Elab':    '2.5',   # In GB
    'pre_i686_Live_Design':    '2.0',   # In GB
    'pre_x86_64_Live_Design':  '2.0',   # In GB
    'pre_i686_Live_Sci-kde':   '2.9',   # In GB
    'pre_x86_64_Live_Sci-kde': '2.8',   # In GB
    'pre_i686_Live_Robotics':  '2.2',   # In GB
    'pre_x86_64_Live_Robotics':'2.2',   # In GB
    'pre_i686_Live_Jam':       '2.0',   # In GB
    'pre_x86_64_Live_Jam':     '1.9',   # In GB
    'pre_i686_Live_Astronomy': '2.4',   # In GB
    'pre_x86_64_Live_Astronomy':'2.3',  # In GB
    # Server
    'x86_64_server_DVD':   '1.9',       # In GB
    'i386_server_DVD':     '2.0',       # In GB
    'x86_64_server_net':   '470',       # In MB
    'i386_server_net':     '464',       # In MB
    # Server prerelease
    'pre_x86_64_server_DVD': '1.7',     # In GB
    'pre_i386_server_DVD':   '2.2',     # In GB
    'pre_x86_64_server_net': '422',     # In MB
    'pre_i386_server_net':   '552',     # In MB
    # Workstation
    'x86_64_workstation':  '1.4',       # In GB
    'i386_workstation':    '1.6',       # In GB
    'x86_64_workstation_net': '439',    # In MB
    'i386_workstation_net': '490',      # In MB
    # Workstation prerelease
    'pre_x86_64_workstation':  '1.3',   # In GB
    'pre_i386_workstation':    '1.4',   # In GB
    'pre_x86_64_workstation_net': '407',# In MB
    'pre_i386_workstation_net': '530',  # In MB
    # ARM
    'ARM_Workstation':     '1.2',       # In GB
    'ARM_Server':          '487',       # In MB
    'ARM_Minimal':         '441',       # In MB
    'ARM_KDE':             '1.4',       # In GB
    'ARM_Xfce':            '1.0',       # In MB
    'ARM_LXDE':            '887',       # In MB
    'ARM_Mate':            '1.3',       # In GB
    'ARM_SoaS':            '722',       # In MB
    # ARM prerelease
    'pre_ARM_Workstation': '1.2',       # In GB
    'pre_ARM_Server':      '1.7',       # In GB
    'pre_ARM_Minimal':     '431',       # In MB
    'pre_ARM_KDE':         '1.4',       # In GB
    'pre_ARM_Xfce':        '1.0',       # In GB
    'pre_ARM_LXDE':        '934',       # In MB
    'pre_ARM_Mate':        '1.3',       # In GB
    'pre_ARM_Cinnamon':    '780',       # In MB
    'pre_ARM_SoaS':        '693',       # In MB
    # Cloud
    'raw_x86_64_cloud':    '128',       # In MB
    'raw_i386_cloud':      '143',       # In MB
    'qcow2_x86_64_cloud':  '195',       # In MB
    'qcow2_i386_cloud':    '216',       # In MB
    'VBvag_cloud':         '210',       # In MB
    'libvag_cloud':        '201',       # In MB
    'x86_64_docker':       '42',        # In MB
    'raw_i386_cloud':      '144',       # In MB
    # Note that atomic values here get overwritten by the twoweek script.
    'atomic_raw_cloud':    '???',       # In MB
    'atomic_qcow2_cloud':  '???',       # In MB
    'atomic_VBvag_cloud':  '???',       # In MB
    'atomic_libvag_cloud': '???',       # In MB
    'VBvag_cloud':         '254',       # In MB
    'libvag_cloud':        '245',       # In MB
    'x86_64_docker':       '40',        # In MB
    # Cloud prerelease
    'pre_raw_x86_64_cloud':    '226',   # In MB
    'pre_raw_i386_cloud':      '172',   # In MB
    'pre_qcow2_x86_64_cloud':  '330',   # In MB
    'pre_qcow2_i386_cloud':    '268',   # In MB
    # Note that atomic values here get overwritten by the twoweek script.
    'pre_atomic_raw_cloud':    '???',   # In MB
    'pre_atomic_qcow2_cloud':  '???',   # In MB
    'pre_atomic_VBvag_cloud':  '???',   # In MB
    'pre_atomic_libvag_cloud': '???',   # In MB
    'pre_x86_64_docker':        '40',   # In MB
    'pre_VBvag_cloud':         '237',   # In MB
    'pre_libvag_cloud':        '227',   # In MB
    # Manual atomic prerelease image sizes go here.
    'manual_pre_atomic_raw_cloud':    '100',   # In MB
    'manual_pre_atomic_qcow2_cloud':  '200',   # In MB
    'manual_pre_atomic_VBvag_cloud':  '300',   # In MB
    'manual_pre_atomic_libvag_cloud': '400'    # In MB
}

# Redirect EC2 images

# A mapping of various pieces of EC2 region information...
import collections
region = collections.namedtuple('EC2_region', ['long', 'short', 'code'])

EC2_regions = [
    # long,                                    short,           code
    region(u'US East (N. Virginia)',           u'Virginia',     u'us-east-1'),
    region(u'US West (Oregon)',                u'Oregon',       u'us-west-2'),
    region(u'US West (N. California)',         u'California',   u'us-west-1'),
    region(u'EU West (Ireland)',               u'Ireland',      u'eu-west-1'),
    region(u'EU Central (Frankfurt)',          u'Frankfurt',    u'eu-central-1'),
    region(u'Asia Pacific SE (Singapore)',     u'Singapore',    u'ap-southeast-1'),
    region(u'Asia Pacific NE (Tokyo)',         u'Tokyo',        u'ap-northeast-1'),
    region(u'Asia Pacific SE (Sydney)',        u'Sydney',       u'ap-southeast-2'),
    region(u'South America East (Sāo Paulo)',  u'Saopaolo',     u'sa-east-1'),
]

path_stats={
    'path':        'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2',
}
_path_template = 'home?region={code}#LaunchInstanceWizard:ami='
for _, short, code in EC2_regions:
    path_stats[short] = _path_template.format(code=code)


# EC2 AMI IDs

HVM_base_AMI={
    #'us-east-1':        'ami-775c9b1a',     # Virginia
    #'us-west-2':        'ami-cf00c5af',     # Oregon
    #'us-west-1':        'ami-4e98dd2e',     # California
    #'eu-west-1':        'ami-19fa646a',     # Ireland
    #'eu-central-1':     'ami-62628b0d',     # Frankfurt
    #'ap-southeast-1':   'ami-fde0339e',     # Singapore
    #'ap-northeast-1':   'ami-0c0be16d',     # Tokyo
    #'ap-southeast-2':   'ami-90a38af3',     # Sydney
    #'sa-east-1':        'ami-3ebf3552'      # Sao Paolo
}

GP2_HVM_base_AMI={
    #'us-east-1':        'ami-2a5d9a47',     # Virginia
    #'us-west-2':        'ami-dcfe3bbc',     # Oregon
    #'us-west-1':        'ami-aa9edbca',     # California
    #'eu-west-1':        'ami-16fd6365',     # Ireland
    #'eu-central-1':     'ami-a36188cc',     # Frankfurt
    #'ap-southeast-1':   'ami-1be73478',     # Singapore
    #'ap-northeast-1':   'ami-8a35dfeb',     # Tokyo
    #'ap-southeast-2':   'ami-93a38af0',     # Sydney
    #'sa-east-1':        'ami-0a46cc66'      # Sao Paolo
}

PV_base_AMI={
    #'us-east-1':        'ami-015b9c6c',     # Virginia
    #'us-west-2':        'ami-3c05c05c',     # Oregon
    #'us-west-1':        'ami-189edb78',     # California
    #'eu-west-1':        'ami-2afd6359',     # Ireland
    #'eu-central-1':     'ami-f561889a',     # Frankfurt
    #'ap-southeast-1':   'ami-f7e13294',     # Singapore
    #'ap-northeast-1':   'ami-6a0ee40b',     # Tokyo
    #'ap-southeast-2':   'ami-28a38a4b',     # Sydney
    #'sa-east-1':        'ami-e34fc58f'      # Sao Paolo
}

GP2_PV_base_AMI={
    #'us-east-1':        'ami-095b9c64',     # Virginia
    #'us-west-2':        'ami-fa06c39a',     # Oregon
    #'us-west-1':        'ami-a99fdac9',     # California
    #'eu-west-1':        'ami-28ff615b',     # Ireland
    #'eu-central-1':     'ami-6e638a01',     # Frankfurt
    #'ap-southeast-1':   'ami-28e1324b',     # Singapore
    #'ap-northeast-1':   'ami-b30ae0d2',     # Tokyo
    #'ap-southeast-2':   'ami-f4a58c97',     # Sydney
    #'sa-east-1':        'ami-4346cc2f'      # Sao Paolo
}

HVM_atomic_AMI={
    #'us-east-1':        'ami-f18fff9b',     # Virginia
    #'us-west-2':        'ami-79e8d449',     # Oregon
    #'us-west-1':        'ami-cb2337aa',     # California
    #'eu-west-1':        'ami-ca08b0a6',     # Ireland
    #'eu-central-1':     'ami-5208d721',     # Frankfurt
    #'ap-southeast-1':   'ami-06d68965',     # Singapore
    #'ap-northeast-1':   'ami-691f3a07',     # Tokyo
    #'ap-southeast-2':   'ami-5c736030',     # Sydney
    #'sa-east-1':        'ami-64ff9304'      # Sao Paolo
}

GP2_HVM_atomic_AMI={
    #'us-east-1':        'ami-e38cfc89',     # Virginia
    #'us-west-2':        'ami-182c3879',     # Oregon
    #'us-west-1':        'ami-0efc906e',     # California
    #'eu-west-1':        'ami-120ad561',     # Ireland
    #'eu-central-1':     'ami-d94c5fb5',     # Frankfurt
    #'ap-southeast-1':   'ami-3cb97e5f',     # Singapore
    #'ap-northeast-1':   'ami-261e3b48',     # Tokyo
    #'ap-southeast-2':   'ami-31d68952',     # Sydney
    #'sa-east-1':        'ami-8509b1e9'      # Sao Paolo
}

# EC2 AMI IDs PRERELEASE!!!

pre_HVM_base_AMI={
    #'us-east-1':        'ami-307a1927',     # Virginia
    #'us-west-2':        'ami-ab55a7cb',     # Oregon
    #'us-west-1':        'ami-8b4c35eb',     # California
    #'eu-west-1':        'ami-fb40cb88',     # Ireland
    #'eu-central-1':     'ami-b29974dd',     # Frankfurt
    #'ap-southeast-1':   'ami-6471a607',     # Singapore
    #'ap-northeast-1':   'ami-6b6a8f0a',     # Tokyo
    #'ap-southeast-2':   'ami-aae7cbc9',     # Sydney
    #'sa-east-1':        'ami-be1099d2'      # Sao Paolo
}

pre_GP2_HVM_base_AMI={
    #'us-east-1':        'ami-76701361',     # Virginia
    #'us-west-2':        'ami-80895ee0',     # Oregon
    #'us-west-1':        'ami-0e08456e',     # California
    #'eu-west-1':        'ami-8c2253ff',     # Ireland
    #'eu-central-1':     'ami-7189791e',     # Frankfurt
    #'ap-southeast-1':   'ami-0efa226d',     # Singapore
    #'ap-northeast-1':   'ami-a5d01ec4',     # Tokyo
    #'ap-southeast-2':   'ami-6d9fa80e',     # Sydney
    #'sa-east-1':        'ami-3c8c1d50'      # Sao Paolo
}

pre_PV_base_AMI={
    #'us-east-1':        'ami-55791a42',     # Virginia
    #'us-west-2':        'ami-3657a556',     # Oregon
    #'us-west-1':        'ami-8a4039ea',     # California
    #'eu-west-1':        'ami-ef40cb9c',     # Ireland
    #'eu-central-1':     'ami-aa9974c5',     # Frankfurt
    #'ap-southeast-1':   'ami-d571a6b6',     # Singapore
    #'ap-northeast-1':   'ami-ff6a8f9e',     # Tokyo
    #'ap-southeast-2':   'ami-7de5c91e',     # Sydney
    #'sa-east-1':        'ami-bd1099d1'      # Sao Paolo
}

pre_GP2_PV_base_AMI={
    #'us-east-1':        'ami-2f751638',     # Virginia
    #'us-west-2':        'ami-c357a5a3',     # Oregon
    #'us-west-1':        'ami-5f4a333f',     # California
    #'eu-west-1':        'ami-f840cb8b',     # Ireland
    #'eu-central-1':     'ami-1f987570',     # Frankfurt
    #'ap-southeast-1':   'ami-d071a6b3',     # Singapore
    #'ap-northeast-1':   'ami-ba6f8adb',     # Tokyo
    #'ap-southeast-2':   'ami-39e6ca5a',     # Sydney
    #'sa-east-1':        'ami-8b159ce7'      # Sao Paolo
}

pre_HVM_atomic_AMI={
    #'us-east-1':        'ami-7d1a6c18',     # Virginia
    #'us-west-2':        'ami-c5f5eaf5',     # Oregon
    #'us-west-1':        'ami-2945806d',     # California
    #'eu-west-1':        'ami-b5b895c2',     # Ireland
    #'eu-central-1':     'ami-b28eb0af',     # Frankfurt
    #'ap-southeast-1':   'ami-9e9683cc',     # Singapore
    #'ap-northeast-1':   'ami-28d04628',     # Tokyo
    #'ap-southeast-2':   'ami-2f165815',     # Sydney
    #'sa-east-1':        'ami-9b0c9986'      # Sao Paolo
}

pre_GP2_HVM_atomic_AMI={
    #'us-east-1':        'ami-bf1d6bda',     # Virginia
    #'us-west-2':        'ami-e9f5ead9',     # Oregon
    #'us-west-1':        'ami-23458067',     # California
    #'eu-west-1':        'ami-c7b895b0',     # Ireland
    #'eu-central-1':     'ami-ac8eb0b1',     # Frankfurt
    #'ap-southeast-1':   'ami-909683c2',     # Singapore
    #'ap-northeast-1':   'ami-12d54312',     # Tokyo
    #'ap-southeast-2':   'ami-3716580d',     # Sydney
    #'sa-east-1':        'ami-9d0c9980'      # Sao Paolo
}
