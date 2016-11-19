var dir_path = '../../static/checksums/';
var atom_path = 'https://dl.fedoraproject.org/pub/alt/atomic/stable/Fedora-Atomic-' + curr_atomic_id + '-' + atomic_composedate + '.0/CloudImages/x86_64/images/';
var dock_path = 'https://dl.fedoraproject.org/pub/alt/atomic/stable/Fedora-Atomic-' + curr_atomic_id + '-' + atomic_composedate + '.0/Docker/x86_64/images/';
var iso_path = 'https://dl.fedoraproject.org/pub/alt/atomic/stable/Fedora-Atomic-' + curr_atomic_id + '-' + atomic_composedate + '.0/Atomic/x86_64/iso/';

var checksums = [];
// Generate dynamic checksum paths
checksums['Fedora-Workstation-Live-x86_64-' + curr_id + '-' + RC_gold + '.iso'] = dir_path + 'Fedora-Workstation-' + curr_id + '-' + RC_gold + '-x86_64-CHECKSUM';
checksums['Fedora-Workstation-netinst-x86_64-' + curr_id + '-' + RC_gold + '.iso'] = dir_path + 'Fedora-Workstation-' + curr_id + '-' + RC_gold + '-x86_64-CHECKSUM';
checksums['Fedora-Workstation-Live-i386-' + curr_id + '-' + RC_gold + '.iso'] = dir_path + 'Fedora-Workstation-' + curr_id + '-' + RC_gold + '-i386-CHECKSUM';
checksums['Fedora-Workstation-netinst-i386-' + curr_id + '-' + RC_gold + '.iso'] = dir_path + 'Fedora-Workstation-' + curr_id + '-' + RC_gold + '-i386-CHECKSUM';
checksums['Fedora-Server-dvd-x86_64-' + curr_id + '-' + RC_gold + '.iso'] = dir_path + 'Fedora-Server-' + curr_id + '-' + RC_gold + '-x86_64-CHECKSUM';
checksums['Fedora-Server-netinst-x86_64-' + curr_id + '-' + RC_gold + '.iso'] = dir_path + 'Fedora-Server-' + curr_id + '-' + RC_gold + '-x86_64-CHECKSUM';
checksums['Fedora-Docker-Base-' + curr_atomic_id + '-' + atomic_composedate + '.0.x86_64.tar.xz'] = dock_path + 'Fedora-Docker-' + curr_atomic_id + '-' + atomic_composedate + '.0-x86_64-CHECKSUM';
checksums['Fedora-Atomic-' + curr_atomic_id + '-' + atomic_composedate + '.0.x86_64.qcow2'] = atom_path + 'Fedora-CloudImages-' + curr_atomic_id + '-' + atomic_composedate + '.0-x86_64-CHECKSUM';
checksums['Fedora-Atomic-' + curr_atomic_id + '-' + atomic_composedate + '.0.x86_64.raw.xz'] = atom_path + 'Fedora-CloudImages-' + curr_atomic_id + '-' + atomic_composedate + '.0-x86_64-CHECKSUM';
checksums['Fedora-Atomic-Vagrant-' + curr_atomic_id + '-' + atomic_composedate + '.0.x86_64.vagrant-libvirt.box'] = atom_path + 'Fedora-CloudImages-' + curr_atomic_id + '-' + atomic_composedate + '.0-x86_64-CHECKSUM';
checksums['Fedora-Atomic-Vagrant-' + curr_atomic_id + '-' + atomic_composedate + '.0.x86_64.vagrant-virtualbox.box'] = atom_path + 'Fedora-CloudImages-' + curr_atomic_id + '-' + atomic_composedate + '.0-x86_64-CHECKSUM';
checksums['Fedora-Atomic-dvd-x86_64-' + curr_atomic_id + '-' + atomic_composedate + '.0.iso'] = iso_path + 'Fedora-Atomic-' + curr_atomic_id + '-' + atomic_composedate + '.0-x86_64-CHECKSUM';

var fallback = '../../verify.html';

window.onload = function(){
  var path = window.location.toString().split('/');
  var checksum = checksums[path[path.length-1]];
  var links = document.getElementsByClassName('checksum');
  for (var i = 0; i<links.length; i++) {
      links[i].href = (checksum === undefined) ? fallback : checksum;
  }
}