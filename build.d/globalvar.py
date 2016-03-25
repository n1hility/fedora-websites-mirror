#!/usr/bin/python
# -*- coding: utf-8 -*-
# This file defines all variable needed to be edited during the release cycle (alpha, beta...).
release={
    'prev_id':     '22',
    'curr_id':     '23',
    'next_id':     '24',
    'curr_name':   '',
    'next_name':   '',
    'curr_state':  'Alpha',        # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_arm_state':  'Alpha',         # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_ppc64_state':  'Alpha',       # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_s390_state':  'Alpha',        # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_cloud_state':  'Alpha',       # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_cloud_AMI_state':  'Alpha',   # either 'Alpha', 'Beta' or '' (i.e empty)
    'prev_arm_id': '22',
    'prev_ppc64_id': '22',
    'prev_s390_id': '22',
    'prev_cloud_id': '22',
    'curr_arm_id': '23',
    'curr_ppc64_id': '23',
    'curr_s390_id': '23',
    'curr_cloud_id': '23',
    'curr_cloud_AMI_id': '23',
    'next_arm_id': '24',
    'next_ppc64_id': '24',
    'next_s390_id': '24',
    'next_cloud_id': '24',
    'next_cloud_AMI_id': '24',
    'composedate': '20151030',
    # Note that atomic values here get overwritten by the twoweek script.
    'atomic_composedate': '20151030',
    'pre_cloud_composedate': '20150915',
    'pre_cloud_AMI_composedate': '20150915',
    'manual_pre_cloud_composedate': '20160101',
    'manual_pre_cloud_atomic_composedate': '20160101',
    'manual_pre_cloud_AMI_atomic_composedate': '20160101',
    # Note that atomic values here get overwritten by the twoweek script.
    'pre_cloud_atomic_composedate': '20150915',
    'pre_cloud_AMI_atomic_composedate': '20150915',
    'RC_gold': '10',              # insert the number of the RC version declared GOLD
    'RC_pre_gold': '7',           # insert the number of the prerelease RC version declared GOLD
    'RC_pre_build': '1.7',        # sometimes releng use the RC build

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
    'doc':             'https://docs.fedoraproject.org/en-US/Fedora'
}

iso_size={
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
    'pre_i686_Live_KDE':    '1.2',       # In GB
    'pre_x86_64_Live_KDE':  '1.2',       # In GB
    'pre_i686_Live_LXDE':   '947',       # In MB
    'pre_x86_64_Live_LXDE': '941',       # In MB
    'pre_i686_Live_Xfce':   '1.0',       # In GB
    'pre_x86_64_Live_Xfce': '918',       # In MB
    'pre_i686_Live_Mate':   '1.3',       # In GB
    'pre_x86_64_Live_Mate': '1.3',       # In GB
    'pre_i686_Live_Soas':   '662',       # In MB
    'pre_x86_64_Live_Soas': '686',       # In MB
    'pre_i686_Live_Cinnamon': '1.2',     # In GB
    'pre_x86_64_Live_Cinnamon': '1.2',   # In GB
    # Spins
    'i686_Live_Security':  '916',       # In MB
    'x86_64_Live_Security':'940',       # In MB
    'i686_Live_Games':     '3.7',       # In GB
    'x86_64_Live_Games':   '3.9',       # In GB
    'i686_Live_Elab':      '2.5',       # In GB
    'x86_64_Live_Elab':    '2.5',       # In GB
    'i686_Live_Design':    '1.9',       # In GB
    'x86_64_Live_Design':  '1.8',       # In GB
    'i686_Live_Sci-kde':   '2.6',       # In GB
    'x86_64_Live_Sci-kde': '2.7',       # In GB
    'i686_Live_Robotics':  '2.5',       # In GB
    'x86_64_Live_Robotics':'2.5',       # In GB
    'i686_Live_Jam':       '1.7',       # In GB
    'x86_64_Live_Jam':     '1.7',       # In GB
    # Spins prerelease
    'pre_i686_Live_Security':  '919',   # In MB
    'pre_x86_64_Live_Security':'943',   # In MB
    'pre_i686_Live_Games':     '4.0',   # In GB
    'pre_x86_64_Live_Games':   '4.0',   # In GB
    'pre_i686_Live_Elab':      '2.5',   # In GB
    'pre_x86_64_Live_Elab':    '2.5',   # In GB
    'pre_i686_Live_Design':    '1.7',   # In GB
    'pre_x86_64_Live_Design':  '1.7',   # In GB
    'pre_i686_Live_Sci-kde':   '2.7',   # In GB
    'pre_x86_64_Live_Sci-kde': '2.7',   # In GB
    'pre_i686_Live_Robotics':  '2.5',   # In GB
    'pre_x86_64_Live_Robotics':'2.5',   # In GB
    'pre_i686_Live_Jam':       '1.7',   # In GB
    'pre_x86_64_Live_Jam':     '1.7',   # In GB
    'pre_i686_Live_Astronomy': '1.7',   # In GB
    'pre_x86_64_Live_Astronomy':'1.7',   # In GB
    # Server
    'x86_64_server_DVD':   '2.0',       # In GB
    'i386_server_DVD':     '2.1',       # In GB
    'x86_64_server_net':   '415',       # In MB
    'i386_server_net':     '458',       # In MB
    # Server prerelease
    'pre_x86_64_server_DVD': '2.1',     # In GB
    'pre_i386_server_DVD':   '2.2',     # In GB
    'pre_x86_64_server_net': '469',     # In MB
    'pre_i386_server_net':   '552',     # In MB
    # Workstation
    'x86_64_workstation':  '1.4',       # In GB
    'i386_workstation':    '1.3',       # In GB
    'x86_64_workstation_net': '413',    # In MB
    'i386_workstation_net': '455',      # In MB
    # Workstation prerelease
    'pre_x86_64_workstation':  '1.4',   # In GB
    'pre_i386_workstation':    '1.4',   # In GB
    'pre_x86_64_workstation_net': '467',# In MB
    'pre_i386_workstation_net': '550',  # In MB
    # ARM
    'ARM_Workstation':     '1.1',       # In GB
    'ARM_Server':          '438',       # In MB
    'ARM_Minimal':         '346',       # In MB
    'ARM_KDE':             '1.2',       # In GB
    'ARM_Xfce':            '844',       # In MB
    'ARM_LXDE':            '787',       # In MB
    'ARM_Mate':            '1.1',       # In GB
    'ARM_SoaS':            '644',       # In MB
    # ARM prerelease
    'pre_ARM_Workstation': '1.2',       # In GB
    'pre_ARM_Server':      '429',       # In MB
    'pre_ARM_Minimal':     '342',       # In MB
    'pre_ARM_KDE':         '1.2',       # In GB
    'pre_ARM_Xfce':        '843',       # In MB
    'pre_ARM_LXDE':        '788',       # In MB
    'pre_ARM_Mate':        '1.1',       # In GB
    'pre_ARM_Cinnamon':    '780',       # In MB
    'pre_ARM_SoaS':        '634',       # In MB
    # Cloud
    'raw_x86_64_cloud':    '146',       # In MB
    'raw_i386_cloud':      '143',       # In MB
    'qcow2_x86_64_cloud':  '218',       # In MB
    'qcow2_i386_cloud':    '216',       # In MB
    'VBvag_cloud':         '209',       # In MB
    'libvag_cloud':        '203',       # In MB
    'x86_64_docker':       '41',        # In MB
    'raw_i386_cloud':      '144',       # In MB
    'qcow2_x86_64_cloud':  '224',       # In MB
    'qcow2_i386_cloud':    '222',       # In MB
    # Note that atomic values here get overwritten by the twoweek script.
    'atomic_raw_cloud':    '???',       # In MB
    'atomic_qcow2_cloud':  '???',       # In MB
    'atomic_VBvag_cloud':  '???',       # In MB
    'atomic_libvag_cloud': '???',       # In MB
    'VBvag_cloud':         '254',       # In MB
    'libvag_cloud':        '245',       # In MB
    'x86_64_docker':       '45',        # In MB
    # Cloud prerelease
    'pre_raw_x86_64_cloud':    '176',   # In MB
    'pre_raw_i386_cloud':      '172',   # In MB
    'pre_qcow2_x86_64_cloud':  '275',   # In MB
    'pre_qcow2_i386_cloud':    '268',   # In MB
    # Note that atomic values here get overwritten by the twoweek script.
    'pre_atomic_raw_cloud':    '???',   # In MB
    'pre_atomic_qcow2_cloud':  '???',   # In MB
    'pre_atomic_VBvag_cloud':  '???',   # In MB
    'pre_atomic_libvag_cloud': '???',   # In MB
    'pre_x86_64_docker':        '49',   # In MB
    'pre_VBvag_cloud':         '257',   # In MB
    'pre_libvag_cloud':        '248',   # In MB
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
    'us-east-1':        'ami-7b8afa11',     # Virginia
    'us-west-2':        'ami-20203441',     # Oregon
    'us-west-1':        'ami-a6fc90c6',     # California
    'eu-west-1':        'ami-080bd47b',     # Ireland
    'eu-central-1':     'ami-084d5e64',     # Frankfurt
    'ap-southeast-1':   'ami-9cba7dff',     # Singapore
    'ap-northeast-1':   'ami-b4193cda',     # Tokyo
    'ap-southeast-2':   'ami-90d887f3',     # Sydney
    'sa-east-1':        'ami-e908b085'      # Sao Paolo
}

GP2_HVM_base_AMI={
    'us-east-1':        'ami-518bfb3b',     # Virginia
    'us-west-2':        'ami-ca2430ab',     # Oregon
    'us-west-1':        'ami-ecff938c',     # California
    'eu-west-1':        'ami-e00dd293',     # Ireland
    'eu-central-1':     'ami-ac4d5ec0',     # Frankfurt
    'ap-southeast-1':   'ami-4bb87f28',     # Singapore
    'ap-northeast-1':   'ami-7d1c3913',     # Tokyo
    'ap-southeast-2':   'ami-17d98674',     # Sydney
    'sa-east-1':        'ami-9009b1fc'      # Sao Paolo
}

PV_base_AMI={
    'us-east-1':        'ami-0187f76b',     # Virginia
    'us-west-2':        'ami-f5263294',     # Oregon
    'us-west-1':        'ami-efff938f',     # California
    'eu-west-1':        'ami-c00cd3b3',     # Ireland
    'eu-central-1':     'ami-1073607c',     # Frankfurt
    'ap-southeast-1':   'ami-d0c700b3',     # Singapore
    'ap-northeast-1':   'ami-fb1e3b95',     # Tokyo
    'ap-southeast-2':   'ami-93d887f0',     # Sydney
    'sa-east-1':        'ami-6a04bc06'      # Sao Paolo
}

GP2_PV_base_AMI={
    'us-east-1':        'ami-8f88f8e5',     # Virginia
    'us-west-2':        'ami-65263204',     # Oregon
    'us-west-1':        'ami-92fe92f2',     # California
    'eu-west-1':        'ami-cf0cd3bc',     # Ireland
    'eu-central-1':     'ami-af4d5ec3',     # Frankfurt
    'ap-southeast-1':   'ami-cfc700ac',     # Singapore
    'ap-northeast-1':   'ami-451d382b',     # Tokyo
    'ap-southeast-2':   'ami-37d48b54',     # Sydney
    'sa-east-1':        'ami-cf09b1a3'      # Sao Paolo
}

HVM_atomic_AMI={
    'us-east-1':        'ami-f18fff9b',     # Virginia
    'us-west-2':        'ami-79e8d449',     # Oregon
    'us-west-1':        'ami-cb2337aa',     # California
    'eu-west-1':        'ami-ca08b0a6',     # Ireland
    'eu-central-1':     'ami-5208d721',     # Frankfurt
    'ap-southeast-1':   'ami-06d68965',     # Singapore
    'ap-northeast-1':   'ami-691f3a07',     # Tokyo
    'ap-southeast-2':   'ami-5c736030',     # Sydney
    'sa-east-1':        'ami-64ff9304'      # Sao Paolo
}

GP2_HVM_atomic_AMI={
    'us-east-1':        'ami-e38cfc89',     # Virginia
    'us-west-2':        'ami-182c3879',     # Oregon
    'us-west-1':        'ami-0efc906e',     # California
    'eu-west-1':        'ami-120ad561',     # Ireland
    'eu-central-1':     'ami-d94c5fb5',     # Frankfurt
    'ap-southeast-1':   'ami-3cb97e5f',     # Singapore
    'ap-northeast-1':   'ami-261e3b48',     # Tokyo
    'ap-southeast-2':   'ami-31d68952',     # Sydney
    'sa-east-1':        'ami-8509b1e9'      # Sao Paolo
}

# EC2 AMI IDs PRERELEASE!!!

# TODO - replace the hand-typed IDs below with results harvested from fedimg

pre_HVM_base_AMI={
    'us-east-1':        'ami-a5303ccf',     # Virginia
    'us-west-2':        'ami-364ca456',     # Oregon
    'us-west-1':        'ami-78e59718',     # California
    'eu-west-1':        'ami-b743c7c4',     # Ireland
    'eu-central-1':     'ami-748b6d1b',     # Frankfurt
    'ap-southeast-1':   'ami-43824820',     # Singapore
    'ap-northeast-1':   'ami-132c397d',     # Tokyo
    'ap-southeast-2':   'ami-e9dfff8a',     # Sydney
    'sa-east-1':        'ami-1a901c76'      # Sao Paolo
}

pre_GP2_HVM_base_AMI={
    'us-east-1':        'ami-9c3438f6',     # Virginia
    'us-west-2':        'ami-fb4aa29b',     # Oregon
    'us-west-1':        'ami-0ee7956e',     # California
    'eu-west-1':        'ami-7c43c70f',     # Ireland
    'eu-central-1':     'ami-1f8a6c70',     # Frankfurt
    'ap-southeast-1':   'ami-0d82486e',     # Singapore
    'ap-northeast-1':   'ami-19223777',     # Tokyo
    'ap-southeast-2':   'ami-c5a383a6',     # Sydney
    'sa-east-1':        'ami-52911d3e'      # Sao Paolo
}

pre_PV_base_AMI={
    'us-east-1':        'ami-40373b2a',     # Virginia
    'us-west-2':        'ami-6740a807',     # Oregon
    'us-west-1':        'ami-70e59710',     # California
    'eu-west-1':        'ami-444dc937',     # Ireland
    'eu-central-1':     'ami-b98a6cd6',     # Frankfurt
    'ap-southeast-1':   'ami-f18e4492',     # Singapore
    'ap-northeast-1':   'ami-352f3a5b',     # Tokyo
    'ap-southeast-2':   'ami-ada585ce',     # Sydney
    'sa-east-1':        'ami-41971b2d'      # Sao Paolo
}

pre_GP2_PV_base_AMI={
    'us-east-1':        'ami-4a343820',     # Virginia
    'us-west-2':        'ami-c44ca4a4',     # Oregon
    'us-west-1':        'ami-08e69468',     # California
    'eu-west-1':        'ami-5e4dc92d',     # Ireland
    'eu-central-1':     'ami-008b6d6f',     # Frankfurt
    'ap-southeast-1':   'ami-1e83497d',     # Singapore
    'ap-northeast-1':   'ami-ce2f3aa0',     # Tokyo
    'ap-southeast-2':   'ami-73ddfd10',     # Sydney
    'sa-east-1':        'ami-a89915c4'      # Sao Paolo
}

pre_HVM_atomic_AMI={
    'us-east-1':        'ami-7d1a6c18',     # Virginia
    'us-west-2':        'ami-c5f5eaf5',     # Oregon
    'us-west-1':        'ami-2945806d',     # California
    'eu-west-1':        'ami-b5b895c2',     # Ireland
    'eu-central-1':     'ami-b28eb0af',     # Frankfurt
    'ap-southeast-1':   'ami-9e9683cc',     # Singapore
    'ap-northeast-1':   'ami-28d04628',     # Tokyo
    'ap-southeast-2':   'ami-2f165815',     # Sydney
    'sa-east-1':        'ami-9b0c9986'      # Sao Paolo
}

pre_GP2_HVM_atomic_AMI={
    'us-east-1':        'ami-bf1d6bda',     # Virginia
    'us-west-2':        'ami-e9f5ead9',     # Oregon
    'us-west-1':        'ami-23458067',     # California
    'eu-west-1':        'ami-c7b895b0',     # Ireland
    'eu-central-1':     'ami-ac8eb0b1',     # Frankfurt
    'ap-southeast-1':   'ami-909683c2',     # Singapore
    'ap-northeast-1':   'ami-12d54312',     # Tokyo
    'ap-southeast-2':   'ami-3716580d',     # Sydney
    'sa-east-1':        'ami-9d0c9980'      # Sao Paolo
}
