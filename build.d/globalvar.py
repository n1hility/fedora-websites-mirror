#!/usr/bin/python
# -*- coding: utf-8 -*-
# This file defines all variable needed to be edited during the release cycle (alpha, beta...).
release={
    'prev_id':     '26',
    'curr_id':     '27',
    'next_id':     '28',
    'curr_name':   '',
    'next_name':   '',
    'curr_state':  'Beta',        # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_arm_state':  'Beta',         # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_alt_state':  'Beta',        # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_cloud_state':  'Beta',       # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_cloud_AMI_state':  'Beta',   # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_server_state':  'Beta',         # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_atomic_state':  'Pre-Release',   # No Alpha/Beta for Atomic Host
    'prev_arm_id': '26',
    'prev_alt_id': '26',
    'prev_cloud_id': '26',
    'prev_atomic_id': '26',
    'curr_arm_id': '27',
    'curr_alt_id': '27',
    'curr_cloud_id': '27',
    'curr_atomic_id': '27',
    'curr_server_id': '27',
    'curr_cloud_AMI_id': '27',
    'next_arm_id': '28',
    'next_alt_id': '28',
    'next_cloud_id': '28',
    'next_atomic_id': '28',
    'next_server_id': '28',
    'next_cloud_AMI_id': '28',
    'composedate': '20160616',
    'unofficial_compose': '20160614',
    'alt_composedate': '20161118',
    # Fedora Media Writer
    'fmw': '4.1.0',
    # These variables are only necessary to keep fedoraproject.org working
    'curr_ppc64_id': '27',
    'prev_ppc64_id': '26',
    'curr_s390_id': '27',
    # Note that atomic values here get overwritten by the twoweek script.
    'atomic_composedate': '20160616',
    'pre_cloud_composedate': '20150915',
    'cloud_AMI_composedate': '20160616',
    'pre_cloud_AMI_composedate': '20160507',
    'manual_cloud_composedate': '20160616',
    'manual_pre_cloud_composedate': '20170330',
    'manual_pre_cloud_atomic_composedate': '20160101',
    'manual_pre_cloud_AMI_atomic_composedate': '20160101',
    # Note that atomic values here get overwritten by the twoweek script.
    'pre_cloud_atomic_composedate': '20150915',
    'pre_cloud_AMI_atomic_composedate': '20150915',
    'RC_gold': '1.6',             # insert the number of the RC version declared GOLD
    'RC_server_gold': '1.6',      # insert the number of the RC version declared GOLD
    'RC_build': '1.6',            # sometimes releng use the RC build
    'RC_gold_aarch64': '1.6',     # RC Gold for aarch64
    'RC_gold_ppc64': '1.6',       # RC Gold for ppc64
    'RC_gold_s390x': '1.6',       # RC Gold for s390x
    'RC_pre_gold': '1.3',         # insert the number of the prerelease RC version declared GOLD
    'RC_pre_build': '3',        # sometimes releng use the RC build
    'RC_pre_gold_aarch64': '1.3', # Pre RC Gold for aarch64
    'RC_pre_gold_ppc64': '1.3',   # Pre RC Gold for ppc64
    'RC_pre_gold_ppc64le': '1.3', # Pre RC Gold for ppc64le
    'RC_pre_gold_s390x': '1.3',   # Pre RC Gold for s390x

    'atomic_qcow2_cloud_url': 'FIXME',
    'atomic_raw_cloud_url': 'FIXME',
    'atomic_VBvag_cloud_url': 'FIXME',
    'atomic_libvag_cloud_url': 'FIXME',
    'atomic_freshness': False,
    'atomic_age': '???',
    'pre_cloud_atomic_freshness': False,
    'pre_cloud_atomic_age': '???',
    'manual_pre_atomic_iso_url': 'https://s3.amazonaws.com/fedora-atomic-s3/Atomic/x86_64/iso/Fedora-Atomic-ostree-x86_64-27-20170929.n.0.iso',
    'manual_pre_atomic_qcow2_cloud_url': 'https://s3.amazonaws.com/fedora-atomic-s3/CloudImages/x86_64/images/Fedora-Atomic-27-20170929.n.0.x86_64.qcow2',
    'manual_pre_atomic_raw_cloud_url': 'https://s3.amazonaws.com/fedora-atomic-s3/CloudImages/x86_64/images/Fedora-Atomic-27-20170929.n.0.x86_64.raw.xz',
    'manual_pre_atomic_VBvag_cloud_url': 'https://s3.amazonaws.com/fedora-atomic-s3/CloudImages/x86_64/images/Fedora-Atomic-Vagrant-27-20170929.n.0.x86_64.vagrant-virtualbox.box',
    'manual_pre_atomic_libvag_cloud_url': 'https://s3.amazonaws.com/fedora-atomic-s3/CloudImages/x86_64/images/Fedora-Atomic-Vagrant-27-20170929.n.0.x86_64.vagrant-libvirt.box',
    'manual_pre_atomic_date': '20180328',
}

path={
    'torrent':         'https://torrent.fedoraproject.org/torrents',
    'torrent_spins':   'https://torrent.fedoraproject.org/torrents',
    'download':        'https://download.fedoraproject.org/pub/fedora/linux/releases',
    'download_modular':'https://download.fedoraproject.org/pub/fedora/linux/modular/releases',
    'dl':              'https://download.fedoraproject.org/pub/fedora/linux/updates',
    'download_spins':  'https://download.fedoraproject.org/pub/alt/releases',
    'download_atomic': 'https://download.fedoraproject.org/pub/alt/atomic',
    'download_arch':   'https://download.fedoraproject.org/pub/fedora-secondary/releases',
    'mirrors':         'https://mirrors.fedoraproject.org/metalink?path=pub/fedora/linux/releases',
    'checksums':       './static/checksums',
    'doc':             'https://docs.fedoraproject.org/en-US/Fedora',
    'doc':             'https://docs.fedoraproject.org/en-US/Fedora',
    'unofficial':      'https://dl.fedoraproject.org/pub/alt/unofficial/releases',
    'devel':      	   'https://download.fedoraproject.org/pub/fedora/linux/development',
    'devel_alt':  	   'https://download.fedoraproject.org/pub/fedora-secondary/development',
    'devel_labs':      'https://download.fedoraproject.org/pub/alt/development',
}

iso_size={

    #Media
    'macosx':             '23.4',       # In MB
    'windows':            '22.7',       # In MB

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
    'aarch64_Server_DVD':  '2.2',       # In GB
    'aarch64_Server_net':  '462',       # In MB
    'aarch64_Cloud_net':   '459',       # In MB
    'aarch64_qcow2':       '265',       # In MB
    'aarch64_raw':         '151',       # In MB
    'aarch64_docker':      '46',        # In MB
    'aarch64_WS':          '1.2',       # In GB
    'aarch64_min':         '46',        # In MB
    'ppc64_Server_DVD':    '2.3',       # In GB
    'ppc64_Server_net':    '523',       # In MB
    'ppc64_Cloud_net':     '520',       # In MB
    'ppc64_qcow2':         '244',       # In MB
    'ppc64_raw':           '137',       # In MB
    'ppc64_docker':        '61',        # In MB
    'ppc64le_Server_DVD':  '2.4',       # In GB
    'ppc64le_Server_net':  '489',       # In MB
    'ppc64le_Cloud_net':   '488',       # In MB
    'ppc64le_qcow2':       '235',       # In MB
    'ppc64le_raw':         '134',       # In MB
    'ppc64le_docker':      '48',        # In MB
    's390x_Server_DVD':    '2.1',       # In GB
    'i686_sda.qcow2':      '212',       # In MB
    'x86_64_sda.qcow2':    '207',       # In MB
    'i686_raw':            '122',       # In MB
    'x86_64_raw':          '117',       # In MB
    # These variables are only necessary to keep fedoraproject.org working
    's390_DVD':            '1.5',
    # Spins
    'i686_Live_KDE':       '1.5',       # In GB
    'x86_64_Live_KDE':     '1.5',       # In GB
    'i686_Live_LXDE':      '1.0',       # In GB
    'x86_64_Live_LXDE':    '1.0',       # In GB
    'i686_Live_LXQt':      '1.0',       # In GB
    'x86_64_Live_LXQt':    '1.0',       # In GB
    'i686_Live_Xfce':      '1.2',       # In GB
    'x86_64_Live_Xfce':    '1.2',       # In GB
    'i686_Live_Mate':      '1.6',       # In GB
    'x86_64_Live_Mate':    '1.6',       # In GB
    'i686_Live_Soas':      '854',       # In MB
    'x86_64_Live_Soas':    '759',       # In MB
    'i686_Live_Cinnamon':   '1.5',       # In GB
    'x86_64_Live_Cinnamon': '1.5',       # In GB
    # Spins prerelease
    'pre_i686_Live_KDE':    '1.5',       # In GB
    'pre_x86_64_Live_KDE':  '1.9',       # In GB
    'pre_i686_Live_LXDE':   '1.3',       # In GB
    'pre_x86_64_Live_LXDE': '1.3',       # In GB
    'pre_i686_Live_Xfce':   '1.5',       # In GB
    'pre_x86_64_Live_Xfce': '1.5',       # In GB
    'pre_i686_Live_Mate':   '1.9',       # In GB
    'pre_x86_64_Live_Mate': '2.0',       # In GB
    'pre_i686_Live_Soas':   '802',       # In MB
    'pre_x86_64_Live_Soas': '856',       # In MB
    'pre_i686_Live_Cinnamon': '1.8',     # In GB
    'pre_x86_64_Live_Cinnamon': '1.8',   # In GB
    'pre_i686_Live_LXQt':    '1.4',      # In GB
    'pre_x86_64_Live_LXQt':  '1.4',      # In GB
    # Labs
    'i686_Live_Security':  '1.2',       # In GB
    'x86_64_Live_Security':'1.2',       # In GB
    'i686_Live_Games':     '3.9',       # In GB
    'x86_64_Live_Games':   '3.9',       # In GB
    'i686_Live_Elab':      '2.5',       # In GB
    'x86_64_Live_Elab':    '2.5',       # In GB
    'i686_Live_Design':    '2.1',       # In GB
    'x86_64_Live_Design':  '2.0',       # In GB
    'i686_Live_Sci-kde':   '2.9',       # In GB
    'x86_64_Live_Sci-kde': '2.9',       # In GB
    'i686_Live_Robotics':  '2.5',       # In GB
    'x86_64_Live_Robotics':'2.6',       # In GB
    'i686_Live_Jam':       '2.0',       # In GB
    'x86_64_Live_Jam':     '2.2',       # In GB
    'i686_Live_Astronomy': '2.6',       # In GB
    'x86_64_Live_Astronomy':'3.0',      # In GB
    'i686_Live_Py_Class':  '1.5',       # In GB
    'x86_64_Live_Py_Class':'1.5',       # In GB
    'libvirt_Py_Class':    '767',     	# In MB
    'virtualbox_Py_Class': '805',   	# In MB
    'ARM_Py_Class':		   '1.0',   	# In GB
    # Labs prerelease
    'pre_i686_Live_Security':  '1.5',   # In GB
    'pre_x86_64_Live_Security':'1.6',   # In GB
    'pre_i686_Live_Games':     '3.9',   # In GB
    'pre_x86_64_Live_Games':   '4.4',   # In GB
    'pre_i686_Live_Elab':      '2.5',   # In GB
    'pre_x86_64_Live_Elab':    '2.5',   # In GB
    'pre_i686_Live_Design':    '2.0',   # In GB
    'pre_x86_64_Live_Design':  '2.2',   # In GB
    'pre_i686_Live_Sci-kde':   '2.9',   # In GB
    'pre_x86_64_Live_Sci-kde': '3.7',   # In GB
    'pre_i686_Live_Robotics':  '2.5',   # In GB
    'pre_x86_64_Live_Robotics':'2.7',   # In GB
    'pre_i686_Live_Jam':       '2.0',   # In GB
    'pre_x86_64_Live_Jam':     '2.6',   # In GB
    'pre_i686_Live_Astronomy': '2.6',   # In GB
    'pre_x86_64_Live_Astronomy':'3.6',  # In GB
    'pre_i686_Live_Python':    '1.7',   # In GB
    'pre_x86_64_Live_Python':  '1.7',   # In GB
    # Server
    'x86_64_server_DVD':   '2.3',       # In GB
    'i386_server_DVD':     '2.4',       # In GB
    'x86_64_server_net':   '511',       # In MB
    'i386_server_net':     '569',       # In MB
    # Server prerelease
    'pre_x86_64_server_DVD': '2.7',     # In GB
    'pre_i386_server_DVD':   '2.5',     # In GB
    'pre_x86_64_server_net': '571',     # In MB
    'pre_i386_server_net':   '525',     # In MB
    # Workstation
    'x86_64_workstation':  '1.5',       # In GB
    'i386_workstation':    '1.6',       # In GB
    'x86_64_workstation_net': '482',    # In MB
    'i386_workstation_net': '566',      # In MB
    # Workstation prerelease
    'pre_x86_64_workstation':  '1.8',   # In GB
    'pre_i386_workstation':    '1.8',   # In GB
    'pre_x86_64_workstation_net': '571',# In MB
    'pre_i386_workstation_net': '525',  # In MB
    # Atomic Workstation
    'x64_atomic_workstation':   '2.2',   # In GB
    # ARM
    'ARM_Workstation':     '1.3',       # In GB
    'ARM_Server':          '537',       # In MB
    'ARM_Minimal':         '434',       # In MB
    'ARM_KDE':             '1.3',       # In GB
    'ARM_Xfce':            '1.1',       # In MB
    'ARM_LXDE':            '943',       # In MB
    'ARM_LXQt':            '1.0',       # In GB
    'ARM_Mate':            '1.5',       # In GB
    'ARM_SoaS':            '713',       # In MB
    'ARM_Python':          '1.0',       # In GB
    # ARM prerelease
    'pre_ARM_Workstation': '1.4',       # In GB
    'pre_ARM_Server':      '479',       # In MB
    'pre_ARM_Minimal':     '352',       # In MB
    'pre_ARM_KDE':         '1.6',       # In GB
    'pre_ARM_Xfce':        '1.3',       # In GB
    'pre_ARM_LXDE':        '1.1',       # In MB
    'pre_ARM_LXQt':        '1.2',       # In MB
    'pre_ARM_Mate':        '1.6',       # In GB
    'pre_ARM_Cinnamon':    '780',       # In MB
    'pre_ARM_SoaS':        '682',       # In MB
    # Cloud
    'raw_x86_64_cloud':    '134',       # In MB
    'raw_i386_cloud':      '143',       # In MB
    'qcow2_x86_64_cloud':  '222',       # In MB
    'qcow2_i386_cloud':    '216',       # In MB
    'VBvag_cloud':         '253',       # In MB
    'libvag_cloud':        '243',       # In MB
    'x86_64_docker':       '48',        # In MB
    'raw_i386_cloud':      '144',       # In MB
    # Note that atomic values here get overwritten by the twoweek script.
    'atomic_raw_cloud':    '???',       # In MB
    'atomic_qcow2_cloud':  '???',       # In MB
    'atomic_VBvag_cloud':  '???',       # In MB
    'atomic_libvag_cloud': '???',       # In MB
    'VBvag_cloud':         '208',       # In MB
    'libvag_cloud':        '199',       # In MB
    'x86_64_docker':       '40',        # In MB
    'atomic_iso':          '918',       # In MB
    # Cloud prerelease
    'pre_raw_x86_64_cloud':    '150',   # In MB
    'pre_raw_i386_cloud':      '172',   # In MB
    'pre_qcow2_x86_64_cloud':  '237',   # In MB
    'pre_qcow2_i386_cloud':    '268',   # In MB
    'pre_VBvag_cloud':         '231',   # In MB
    'pre_libvag_cloud':        '223',   # In MB
    # Note that atomic values here get overwritten by the twoweek script.
    'pre_atomic_raw_cloud':    '???',   # In MB
    'pre_atomic_qcow2_cloud':  '???',   # In MB
    'pre_atomic_VBvag_cloud':  '???',   # In MB
    'pre_atomic_libvag_cloud': '???',   # In MB
    'pre_atomic_iso':          '950',   # In MB
    'pre_x86_64_Container':    '42',    # In MB
    'pre_VBvag_cloud':         '231',   # In MB
    'pre_libvag_cloud':        '223',   # In MB
    # Manual atomic prerelease image sizes go here.
    'manual_pre_atomic_raw_cloud':    '419',   # In MB
    'manual_pre_atomic_qcow2_cloud':  '569',   # In MB
    'manual_pre_atomic_VBvag_cloud':  '555',   # In MB
    'manual_pre_atomic_libvag_cloud': '543',   # In MB
    'manual_pre_atomic_iso':          '950',   # In MB
    # Everything release
    'x86_64_ev':        '508',   #In MB
    'i386_ev':          '566',   #In MB
    's390x_ev':         '425',   #In MB
    'aarch64_ev':       '459',   #In MB
    'ppc64_ev':         '521',   #In MB
    'ppc64le_ev':       '488',   #In MB
    # Everything prerelease
    'pre_x86_64_ev':        '571',   #In MB
    'pre_i386_ev':          '525',   #In MB
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
    region(u'Asia Pacific (Seoul)',            u'Seoul',        u'ap-northeast-2'),
    region(u'Asia Pacific (Mumbai)',           u'Mumbai',       u'ap-south-1')
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
    'us-east-1':        'ami-b6a47fcb',     # Virginia
    'us-west-2':        'ami-a98c17d1',     # Oregon
    'us-west-1':        'ami-224c5d42',     # California
    'eu-west-1':        'ami-4207553b',     # Ireland
    'eu-central-1':     'ami-8b623f60',     # Frankfurt
    'ap-southeast-1':   'ami-b0dc85cc',     # Singapore
    'ap-northeast-1':   'ami-cf4348b3',     # Tokyo
    'ap-southeast-2':   'ami-717bb713',     # Sydney
    'sa-east-1':        'ami-4662352a'      # Sao Paolo
}

pre_GP2_HVM_base_AMI={
    'us-east-1':        'ami-f4a47f89',     # Virginia
    'us-west-2':        'ami-128e156a',     # Oregon
    'us-west-1':        'ami-114a5b71',     # California
    'eu-west-1':        'ami-111d4f68',     # Ireland
    'eu-central-1':     'ami-91613c7a',     # Frankfurt
    'ap-southeast-1':   'ami-51de872d',     # Singapore
    'ap-northeast-1':   'ami-78434804',     # Tokyo
    'ap-southeast-2':   'ami-4775b925',     # Sydney
    'sa-east-1':        'ami-e063348c'      # Sao Paolo
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
    'us-east-1':        'ami-f4ca1189',     # Virginia
    'us-west-2':        'ami-0eba2176',     # Oregon
    'us-west-1':        'ami-0e4f5e6e',     # California
    'eu-west-1':        'ami-da0a58a3',     # Ireland
    'eu-central-1':     'ami-ab623f40',     # Frankfurt
    'ap-southeast-1':   'ami-f9d08985',     # Singapore
    'ap-northeast-1':   'ami-45404b39',     # Tokyo
    'ap-southeast-2':   'ami-b07ab6d2',     # Sydney
    'sa-east-1':        'ami-de6037b2'      # Sao Paolo
}

pre_GP2_HVM_atomic_AMI={
    'us-east-1':        'ami-53c11a2e',     # Virginia
    'us-west-2':        'ami-e5841f9d',     # Oregon
    'us-west-1':        'ami-7a4c5d1a',     # California
    'eu-west-1':        'ami-bb0755c2',     # Ireland
    'eu-central-1':     'ami-539cc1b8',     # Frankfurt
    'ap-southeast-1':   'ami-ced089b2',     # Singapore
    'ap-northeast-1':   'ami-14454e68',     # Tokyo
    'ap-southeast-2':   'ami-a17bb7c3',     # Sydney
    'sa-east-1':        'ami-0062356c'      # Sao Paolo
}
