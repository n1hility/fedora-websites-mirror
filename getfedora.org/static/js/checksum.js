var dir_path = '../../static/checksums/';
var atom_path = 'https://dl.fedoraproject.org/pub/alt/atomic/stable/Cloud-Images/x86_64/Images/';
var iso_path = 'https://dl.fedoraproject.org/pub/alt/atomic/stable/Cloud_Atomic/x86_64/iso/';

var checksums = [];
// Generate dynamic checksum paths
checksums['Fedora-Workstation-Live-x86_64-' + curr_id + '-' + RC_gold + '.iso'] = dir_path + 'Fedora-Workstation-' + curr_id + '-x86_64-CHECKSUM';
checksums['Fedora-Workstation-netinst-x86_64-' + curr_id + '-' + RC_gold + '.iso'] = dir_path + 'Fedora-Workstation-' + curr_id + '-x86_64-CHECKSUM';
checksums['Fedora-Workstation-Live-i386-' + curr_id + '-' + RC_gold + '.iso'] = dir_path + 'Fedora-Workstation-' + curr_id + '-i386-CHECKSUM';
checksums['Fedora-Workstation-netinst-i386-' + curr_id + '-' + RC_gold + '.iso'] = dir_path + 'Fedora-Workstation-' + curr_id + '-i386-CHECKSUM';
checksums['Fedora-Server-dvd-x86_64-' + curr_id + '-' + RC_gold + '.iso'] = dir_path + 'Fedora-Server-' + curr_id + '-x86_64-CHECKSUM';
checksums['Fedora-Server-netinst-x86_64-' + curr_id + '-' + RC_gold + '.iso'] = dir_path + 'Fedora-Server-' + curr_id + '-x86_64-CHECKSUM';
checksums['Fedora-Server-dvd-i386-' + curr_id + '-' + RC_gold + '.iso'] = dir_path + 'Fedora-Server-' + curr_id + '-i386-CHECKSUM';
checksums['Fedora-Server-netinst-i386-' + curr_id + '-' + RC_gold + '.iso'] = dir_path + 'Fedora-Server-' + curr_id + '-i386-CHECKSUM';
checksums['Fedora-Cloud-Base-' + curr_id + '-' + RC_gold + '.x86_64.qcow2'] = dir_path + 'Fedora-Cloud_Images-x86_64-' + curr_id + '-CHECKSUM';
checksums['Fedora-Cloud-Base-' + curr_id + '-' + RC_gold + '.x86_64.raw.xz'] = dir_path + 'Fedora-Cloud_Images-x86_64-' + curr_id + '-CHECKSUM';
checksums['Fedora-Cloud-Base-Vagrant-' + curr_id + '-' + RC_gold + '.x86_64.vagrant-libvirt.box'] = dir_path + 'Fedora-Cloud_Images-x86_64-' + curr_id + '-CHECKSUM';
checksums['Fedora-Cloud-Base-Vagrant-' + curr_id + '-' + RC_gold + '.x86_64.vagrant-virtualbox.box'] = dir_path + 'Fedora-Cloud_Images-x86_64-' + curr_id + '-CHECKSUM';
checksums['Fedora-Cloud-Base-' + curr_id + '-' + RC_gold + '.i386.qcow2'] = dir_path + 'Fedora-Cloud_Images-i386-' + curr_id + '-CHECKSUM';
checksums['Fedora-Cloud-Base-' + curr_id + '-' + RC_gold + '.i386.raw.xz'] = dir_path + 'Fedora-Cloud_Images-i386-' + curr_id + '-CHECKSUM';
checksums['Fedora-Docker-Base-' + curr_id + '-' + RC_gold + '.x86_64.tar.xz'] = dir_path + 'Fedora-Docker-x86_64-' + curr_id + '-CHECKSUM';
checksums['Fedora-Cloud-Atomic-' + curr_id + '-' + atomic_composedate + '.x86_64.qcow2'] = atom_path + 'Fedora-Cloud-Images-x86_64-' + curr_id + '-CHECKSUM';
checksums['Fedora-Cloud-Atomic-' + curr_id + '-' + atomic_composedate + '.x86_64.raw.xz'] = atom_path + 'Fedora-Cloud-Images-x86_64-' + curr_id + '-CHECKSUM';
checksums['Fedora-Cloud-Atomic-Vagrant-' + curr_id + '-' + atomic_composedate + '.x86_64.vagrant-libvirt.box'] = atom_path + 'Fedora-Cloud-Images-x86_64-' + curr_id + '-CHECKSUM';
checksums['Fedora-Cloud-Atomic-Vagrant-' + curr_id + '-' + atomic_composedate + '.x86_64.vagrant-virtualbox.box'] = atom_path + 'Fedora-Cloud-Images-x86_64-' + curr_id + '-CHECKSUM';
checksums['Fedora-Cloud_Atomic-x86_64-' + curr_id + '-' + atomic_composedate + '.iso'] = iso_path + 'Fedora-Cloud_Atomic-' + curr_id + '-x86_64-CHECKSUM';

var fallback = '../../verify.html';

window.onload = function(){
  var path = window.location.toString().split('/');
  var checksum = checksums[path[path.length-1]];
  var links = document.getElementsByClassName('checksum');
  for (var i = 0; i<links.length; i++) {
      links[i].href = (checksum === undefined) ? fallback : checksum;
  }
}