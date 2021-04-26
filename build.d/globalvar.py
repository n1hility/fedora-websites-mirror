#!/usr/bin/python
# -*- coding: utf-8 -*-
# This file defines all variable needed to be edited during the release cycle (alpha, beta...).
release={
    'prev_id':     '33',
    'curr_id':     '34',
    'next_id':     '35',
    'curr_name':   '',
    'next_name':   '',
    'curr_state':  '',           # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_arm_state':  '',       # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_alt_state':  '',       # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_cloud_state':  '',     # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_cloud_AMI_state':  '', # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_server_state':  '',    # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_atomic_state':  '',    # 'Pre-Release' or '' - No Alpha/Beta for Atomic Host
    'prev_arm_id': '33',
    'prev_alt_id': '33',
    'prev_cloud_id': '33',
    'prev_atomic_id': '30',
    'curr_arm_id': '34',
    'curr_alt_id': '34',
    'curr_cloud_id': '34',
    'curr_atomic_id': '30',
    'curr_server_id': '34',
    'curr_cloud_AMI_id': '34',
    'curr_iot_id': '34',
    'curr_silverblue_id': '34',
    'next_silverblue_id': '35',
    'next_arm_id': '35',
    'next_alt_id': '35',
    'next_cloud_id': '35',
    'next_atomic_id': '30',
    'next_server_id': '35',
    'next_cloud_AMI_id': '35',
    'composedate': '20160616',
    'unofficial_compose': '20181029',
    'alt_composedate': '20161118',
    # Fedora Media Writer
    'fmw': '4.1.4',
    # These variables are only necessary to keep fedoraproject.org working
    'curr_ppc64_id': '29',
    'prev_ppc64_id': '28',
    'curr_s390_id': '29',
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
    'RC_gold': '1.2',             # insert the number of the RC version declared GOLD
    'RC_server_gold': '1.2',      # insert the number of the RC version declared GOLD
    'RC_build': '1.2',            # sometimes releng use the RC build
    'RC_gold_aarch64': '1.2',     # RC Gold for aarch64
    'RC_gold_ppc64': '1.2',       # RC Gold for ppc64
    'RC_gold_ppc64le': '1.2',     # RC Gold for ppc64le
    'RC_gold_s390x': '1.2',       # RC Gold for s390x
    'RC_pre_gold': '1.3',         # insert the number of the prerelease RC version declared GOLD
    'RC_pre_build': '1.3',        # sometimes releng use the RC build
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
    'manual_pre_atomic_date': '20180919',
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
    'checksums':       'https://getfedora.org/static/checksums',
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
    'x86_64_DVD':          '1.9',       # In GB
    'i386_DVD':            '4.4',       # In GB
    'source_DVD':          '9.2',       # In GB
    'i686_Live_Desktop':   '922',       # In MB
    'x86_64_Live_Desktop': '953',       # In MB
    'i386_Netinstall':     '357',       # In MB
    'x86_64_Netinstall':   '321',       # In MB
    'PPC64_DVD':           '4.3',       # In GB
    'PPC64_Netinstall':    '340',       # In MB
    'aarch64_Server_DVD':  '2.8',       # In GB
    'aarch64_Server_net':  '552',       # In MB
    'aarch64_Server_raw':  '571',       # In MB
    'aarch64_Cloud_net':   '459',       # In MB
    'aarch64_qcow2':       '313',       # In MB
    'aarch64_raw':         '190',       # In MB
    'aarch64_Container':   '43',        # In MB
    'aarch64_WS':          '2.8',       # In GB
    'aarch64_KDE_live':         '1.9',       # In GB
    'aarch64_KDE_raw':         '4.0',       # In GB
    'aarch64_min':         '412',       # In MB
    'ppc64_Server_DVD':    '3.0',       # In GB
    'ppc64_Server_net':    '597',       # In MB
    'ppc64_Cloud_net':     '520',       # In MB
    'ppc64_qcow2':         '282',       # In MB
    'ppc64_raw':           '158',       # In MB
    'ppc64_Container':     '43',        # In MB
    'ppc64le_Server_DVD':  '1.9',       # In GB
    'ppc64le_Server_net':  '619',       # In MB
    'ppc64le_Cloud_net':   '488',       # In MB
    'ppc64le_qcow2':       '366',       # In MB
    'ppc64le_raw':         '232',       # In MB
    'ppc64le_Container':   '42',        # In MB
    's390x_Server_DVD':    '1.7',       # In GB
    's390x_Server_net':    '484',       # In MB
    's390x_qcow2':         '360',       # In MB
    's390x_raw':           '222',       # In MB
    's390x_Container':     '37',        # In MB
    'i686_sda.qcow2':      '212',       # In MB
    'x86_64_sda.qcow2':    '207',       # In MB
    'i686_raw':            '122',       # In MB
    'x86_64_raw':          '117',       # In MB
    # These variables are only necessary to keep fedoraproject.org working
    's390_DVD':            '1.5',
    # Spins
    'i686_Live_KDE':       '1.3',       # In GB
    'x86_64_Live_KDE':     '1.8',       # In GB
    'i686_Live_LXDE':      '1.3',       # In GB
    'x86_64_Live_LXDE':    '1.3',       # In GB
    'i686_Live_LXQt':      '1.4',       # In GB
    'x86_64_Live_LXQt':    '1.4',       # In GB
    'i686_Live_Xfce':      '1.5',       # In GB
    'x86_64_Live_Xfce':    '1.5',       # In GB
    'i686_Live_Mate':      '2.0',       # In GB
    'x86_64_Live_Mate':    '2.0',       # In GB
    'i686_Live_Soas':      '895',       # In MB
    'x86_64_Live_Soas':    '946',       # In MB
    'i686_Live_Cinnamon':   '2.0',       # In GB
    'x86_64_Live_Cinnamon': '2.1',       # In GB
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
    'i686_Live_Security':  '1.6',       # In GB
    'x86_64_Live_Security':'1.7',       # In GB
    'i686_Live_Games':     '4.0',       # In GB
    'x86_64_Live_Games':   '4.1',       # In GB
    'i686_Live_Elab':      '2.5',       # In GB
    'x86_64_Live_Elab':    '2.5',       # In GB
    'i686_Live_Design':    '2.4',       # In GB
    'x86_64_Live_Design':  '2.4',       # In GB
    'i686_Live_Sci-kde':   '3.4',       # In GB
    'x86_64_Live_Sci-kde': '3.7',       # In GB
    'i686_Live_Robotics':  '2.5',       # In GB
    'x86_64_Live_Robotics':'2.5',       # In GB
    'i686_Live_Jam':       '2.4',       # In GB
    'x86_64_Live_Jam':     '2.5',       # In GB
    'i686_Live_Astronomy': '3.5',       # In GB
    'x86_64_Live_Astronomy':'3.6',      # In GB
    'i686_Live_Py_Class':  '1.7',       # In GB
    'x86_64_Live_Py_Class':'1.8',       # In GB
    'libvirt_Py_Class':    '881',     	# In MB
    'virtualbox_Py_Class': '923',   	# In MB
    'ARM_Py_Class':		   '1.2',   	# In GB
    'libvirt_Scientific':  '2.8',       # In GB
    'virtualbox_Scientific':  '2.9',    # In GB
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
    'x86_64_server_DVD':   '3.0',       # In GB
    'i386_server_DVD':     '2.8',       # In GB
    'x86_64_server_net':   '600',       # In MB
    'i386_server_net':     '536',       # In MB
    # Server prerelease
    'pre_x86_64_server_DVD': '2.7',     # In GB
    'pre_i386_server_DVD':   '2.5',     # In GB
    'pre_x86_64_server_net': '571',     # In MB
    'pre_i386_server_net':   '525',     # In MB
    # Workstation
    'x86_64_workstation':  '1.9',       # In GB
    'i386_workstation':    '1.8',       # In GB
    'x86_64_workstation_net': '600',    # In MB
    'i386_workstation_net': '556',      # In MB
    # Workstation prerelease
    'pre_x86_64_workstation':  '1.8',   # In GB
    'pre_i386_workstation':    '1.7',   # In GB
    'pre_x86_64_workstation_net': '594',# In MB
    'pre_i386_workstation_net': '551',  # In MB
    # Silverblue
    'x64_silverblue':   '2.1',  # In GB
    # ARM
    'ARM_Workstation':     '1.3',       # In GB
    'ARM_Server':          '507',       # In MB
    'ARM_Minimal':         '362',       # In MB
    'ARM_KDE':             '1.4',       # In GB
    'ARM_Xfce':            '1.1',       # In MB
    'ARM_LXDE':            '1.1',       # In MB
    'ARM_LXQt':            '1.0',       # In GB
    'ARM_Mate':            '1.5',       # In GB
    'ARM_SoaS':            '730',       # In MB
    'ARM_Python':          '1.2',       # In GB
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
    'raw_x86_64_cloud':    '195',       # In MB
    'raw_i386_cloud':      '143',       # In MB
    'qcow2_x86_64_cloud':  '319',       # In MB
    'qcow2_i386_cloud':    '216',       # In MB
    'VBvag_cloud':         '279',       # In MB
    'GCP_x86_64_tar':      '263',       # In MB
    'libvag_cloud':        '290',       # In MB
    'x86_64_Container':    '43',        # In MB
    'x86_64_docker':       '43',        # In MB NOTE: this is just to make fedoraproject.org build happy
    'raw_i386_cloud':      '144',       # In MB
    # Note that atomic values here get overwritten by the twoweek script.
    'atomic_raw_cloud':    '???',       # In MB
    'atomic_qcow2_cloud':  '???',       # In MB
    'atomic_VBvag_cloud':  '???',       # In MB
    'atomic_libvag_cloud': '???',       # In MB
    'VBvag_cloud':         '304',       # In MB
    'libvag_cloud':        '294',       # In MB
    'x86_64_Container':    '51',        # In MB
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
    'pre_x86_64_Container':    '43',    # In MB
    'pre_VBvag_cloud':         '231',   # In MB
    'pre_libvag_cloud':        '223',   # In MB
    # Manual atomic prerelease image sizes go here.
    'manual_pre_atomic_raw_cloud':    '493',   # In MB
    'manual_pre_atomic_qcow2_cloud':  '680',   # In MB
    'manual_pre_atomic_VBvag_cloud':  '663',   # In MB
    'manual_pre_atomic_libvag_cloud': '648',   # In MB
    'manual_pre_atomic_iso':          '1054',  # In MB
    # Everything release
    'x86_64_ev':        '601',   #In MB
    'i386_ev':          '556',   #In MB
    's390x_ev':         '445',   #In MB
    'aarch64_ev':       '552',   #In MB
    'ppc64_ev':         '597',   #In MB
    'ppc64le_ev':       '578',   #In MB
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
    region(u'US East (Ohio)',                  u'Ohio',         u'us-east-2'),
    region(u'US West (Oregon)',                u'Oregon',       u'us-west-2'),
    region(u'US West (N. California)',         u'California',   u'us-west-1'),
    region(u'EU West (Ireland)',               u'Ireland',      u'eu-west-1'),
    region(u'EU Central (Frankfurt)',          u'Frankfurt',    u'eu-central-1'),
    region(u'EU West (London)',                u'London',       u'eu-west-2'),
# fedimg fails to upload to eu-west-3 for now
#   region(u'EU West (Paris)',                 u'Paris',        u'eu-west-3'),
    region(u'Asia Pacific SE (Singapore)',     u'Singapore',    u'ap-southeast-1'),
    region(u'Asia Pacific NE (Tokyo)',         u'Tokyo',        u'ap-northeast-1'),
    region(u'Asia Pacific SE (Sydney)',        u'Sydney',       u'ap-southeast-2'),
    region(u'South America East (Sāo Paulo)',  u'Saopaolo',     u'sa-east-1'),
    region(u'Asia Pacific (Seoul)',            u'Seoul',        u'ap-northeast-2'),
    region(u'Asia Pacific (Mumbai)',           u'Mumbai',       u'ap-south-1'),
    region(u'Canada (Central)',                u'Central',      u'ca-central-1')
]

# regions where aarch64 EC2 instances are available
aarch64_EC2_regions = [
    region(u'US East (N. Virginia)',           u'Virginia',     u'us-east-1'),
    region(u'US East (Ohio)',                  u'Ohio',         u'us-east-2'),
    region(u'US West (Oregon)',                u'Oregon',       u'us-west-2'),
    region(u'US West (N. California)',         u'California',   u'us-west-1'),
    region(u'EU West (Ireland)',               u'Ireland',      u'eu-west-1'),
    region(u'EU Central (Frankfurt)',          u'Frankfurt',    u'eu-central-1'),
    region(u'Asia Pacific NE (Tokyo)',         u'Tokyo',        u'ap-northeast-1'),
    region(u'Asia Pacific SE (Sydney)',        u'Sydney',       u'ap-southeast-2'),
    region(u'Asia Pacific (Mumbai)',           u'Mumbai',       u'ap-south-1'),
]

path_stats={
    'path': 'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2',
}
_path_template = 'home?region={code}#LaunchInstanceWizard:ami='
for _, short, code in EC2_regions:
    path_stats[short] = _path_template.format(code=code)


# EC2 AMI IDs
# values populated by searching datagrepper during website build
AARCH64_base_AMI={
}
X86_64_base_AMI={
}
# EC2 AMI IDs PRERELEASE!!!
pre_AARCH64_base_AMI={
}
pre_X86_64_base_AMI={
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

AARCH64_GP2_HVM_atomic_AMI={}

pre_HVM_atomic_AMI={
    'eu-west-2':       'ami-0dd9376c148025bda',
    'ap-northeast-1':  'ami-0c8c3a243f8fa9389',
    'eu-central-1':    'ami-0ba7d4f7df3adecd4',
    'us-west-1':       'ami-0455c73d39bb9d922',
    'us-west-2':       'ami-08494e1090a21e688',
    'ap-southeast-2':  'ami-04544eb8e7d88954e',
    'ca-central-1':    'ami-0039a676512a0794e',
    'ap-southeast-1':  'ami-0a0efd1bb6204159e',
    'sa-east-1':       'ami-05851e0e3ba8fa569',
    'ap-northeast-2':  'ami-0f516fa511f7f5e73',
    'eu-west-1':       'ami-025df16716016af3a',
    'ap-south-1':      'ami-007c9eb1578a4688d',
    'us-east-1':       'ami-03630244e374b092b'
}

pre_GP2_HVM_atomic_AMI={
    'eu-west-2':       'ami-0ab7b595091a81399',
    'ap-northeast-1':  'ami-0751c7e8531851ba0',
    'eu-central-1':    'ami-0716bdf9a47a23af4',
    'us-west-1':       'ami-09f6c41ffc8c38a92',
    'us-west-2':       'ami-0e640910b38a99ad6',
    'ap-southeast-2':  'ami-00383f891422b1ed2',
    'ca-central-1':    'ami-075e5b73667dedb33',
    'ap-southeast-1':  'ami-0ab9ca1d8d1e8353f',
    'sa-east-1':       'ami-03952c6395be8a35d',
    'ap-northeast-2':  'ami-02d3a759042127f7a',
    'eu-west-1':       'ami-0ed1063c442c97e39',
    'ap-south-1':      'ami-0ca9ba91af3aa6d22',
    'us-east-1':       'ami-0be45426d63c7cf4a'
}
