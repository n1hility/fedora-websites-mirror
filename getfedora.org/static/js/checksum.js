var dir_path = '../../static/checksums/';
var dock_path = 'https://dl.fedoraproject.org/pub/alt/atomic/stable/Fedora-Atomic-' + curr_atomic_id + '-' + atomic_composedate + '.0/Container/x86_64/images/';
var atom_path = 'https://dl.fedoraproject.org/pub/alt/atomic/stable/Fedora-' + curr_atomic_id + '-updates-' + atomic_composedate + '/AtomicHost/';
var iso_path = 'https://dl.fedoraproject.org/pub/alt/atomic/stable/Fedora-' + curr_atomic_id + '-updates-' + atomic_composedate + '/AtomicHost/';

var checksums = [];
// Generate dynamic checksum paths
checksums['Fedora-Workstation-Live-x86_64-' + curr_id + '-' + RC_gold + '.iso'] = dir_path + 'Fedora-Workstation-' + curr_id + '-' + RC_gold + '-x86_64-CHECKSUM';
checksums['Fedora-Workstation-netinst-x86_64-' + curr_id + '-' + RC_gold + '.iso'] = dir_path + 'Fedora-Workstation-' + curr_id + '-' + RC_gold + '-x86_64-CHECKSUM';
checksums['Fedora-Workstation-Live-i386-' + curr_id + '-' + RC_gold + '.iso'] = dir_path + 'Fedora-Workstation-' + curr_id + '-' + RC_gold + '-i386-CHECKSUM';
checksums['Fedora-Workstation-netinst-i386-' + curr_id + '-' + RC_gold + '.iso'] = dir_path + 'Fedora-Workstation-' + curr_id + '-' + RC_gold + '-i386-CHECKSUM';
checksums['Fedora-Silverblue-ostree-x86_64-' + curr_id + '-' + RC_gold + '.iso'] = dir_path + 'Fedora-Silverblue-' + curr_id + '-' + RC_gold + '-x86_64-CHECKSUM';
checksums['Fedora-Server-dvd-x86_64-' + curr_server_id + '-' + RC_server_gold + '.iso'] = dir_path + 'Fedora-Server-' + curr_server_id + '-' + RC_server_gold + '-x86_64-CHECKSUM';
checksums['Fedora-Server-netinst-x86_64-' + curr_server_id + '-' + RC_server_gold + '.iso'] = dir_path + 'Fedora-Server-' + curr_server_id + '-' + RC_server_gold + '-x86_64-CHECKSUM';
checksums['Fedora-Server-netinst-aarch64-' + curr_server_id + '-' + RC_server_gold + '.iso'] = dir_path + 'Fedora-Server-disk-' + curr_server_id + '-' + RC_server_gold + '-aarch64-CHECKSUM';
checksums['Fedora-Server-dvd-aarch64-' + curr_server_id + '-' + RC_server_gold + '.iso'] = dir_path + 'Fedora-Server-disk-' + curr_server_id + '-' + RC_server_gold + '-aarch64-CHECKSUM';
checksums['Fedora-Server-' + curr_server_id + '-' + RC_server_gold + '.aarch64.raw.xz'] = dir_path + 'Fedora-Server-' + curr_server_id + '-' + RC_server_gold + '-aarch64-CHECKSUM';
checksums['Fedora-Container-Base-' + curr_id + '-' + RC_gold + '.x86_64.tar.xz'] = dir_path + 'Fedora-Container-' + curr_id + '-' + RC_gold + '-x86_64-CHECKSUM';
checksums['Fedora-AtomicHost-' + curr_atomic_id + '-' + atomic_composedate + '.aarch64.qcow2'] = atom_path + 'aarch64/images/Fedora-AtomicHost-' + curr_atomic_id + '-' + atomic_composedate + '-aarch64-CHECKSUM';
checksums['Fedora-AtomicHost-' + curr_atomic_id + '-' + atomic_composedate + '.ppc64le.qcow2'] = atom_path + 'ppc64le/images/Fedora-AtomicHost-' + curr_atomic_id + '-' + atomic_composedate + '-ppc64le-CHECKSUM';
checksums['Fedora-AtomicHost-' + curr_atomic_id + '-' + atomic_composedate + '.x86_64.qcow2'] = atom_path + 'x86_64/images/Fedora-AtomicHost-' + curr_atomic_id + '-' + atomic_composedate + '-x86_64-CHECKSUM';
checksums['Fedora-AtomicHost-' + curr_atomic_id + '-' + atomic_composedate + '.aarch64.raw.xz'] = atom_path + 'aarch64/images/Fedora-AtomicHost-' + curr_atomic_id + '-' + atomic_composedate + '-aarch64-CHECKSUM';
checksums['Fedora-AtomicHost-' + curr_atomic_id + '-' + atomic_composedate + '.ppc64le.raw.xz'] = atom_path + 'ppc64le/images/Fedora-AtomicHost-' + curr_atomic_id + '-' + atomic_composedate + '-ppc64le-CHECKSUM';
checksums['Fedora-AtomicHost-' + curr_atomic_id + '-' + atomic_composedate + '.x86_64.raw.xz'] = atom_path + 'x86_64/images/Fedora-AtomicHost-' + curr_atomic_id + '-' + atomic_composedate + '-x86_64-CHECKSUM';
checksums['Fedora-AtomicHost-Vagrant-' + curr_atomic_id + '-' + atomic_composedate + '.x86_64.vagrant-libvirt.box'] = atom_path + 'x86_64/images/Fedora-AtomicHost-' + curr_atomic_id + '-' + atomic_composedate + '-x86_64-CHECKSUM';
checksums['Fedora-AtomicHost-Vagrant-' + curr_atomic_id + '-' + atomic_composedate + '.x86_64.vagrant-virtualbox.box'] = atom_path + 'x86_64/images/Fedora-AtomicHost-' + curr_atomic_id + '-' + atomic_composedate + '-x86_64-CHECKSUM';
checksums['Fedora-AtomicHost-ostree-aarch64-' + curr_atomic_id + '-' + atomic_composedate + '.iso'] = iso_path + 'aarch64/iso/Fedora-AtomicHost-' + curr_atomic_id + '-' + atomic_composedate + '-aarch64-CHECKSUM';
checksums['Fedora-AtomicHost-ostree-ppc64le-' + curr_atomic_id + '-' + atomic_composedate + '.iso'] = iso_path + 'ppc64le/iso/Fedora-AtomicHost-' + curr_atomic_id + '-' + atomic_composedate + '-ppc64le-CHECKSUM';
checksums['Fedora-AtomicHost-ostree-x86_64-' + curr_atomic_id + '-' + atomic_composedate + '.iso'] = iso_path + 'x86_64/iso/Fedora-AtomicHost-' + curr_atomic_id + '-' + atomic_composedate + '-x86_64-CHECKSUM';


var fallback = '../../verify.html';

window.onload = function(){
  var path = window.location.toString().split('/');
  var checksum = checksums[path[path.length-1]];
  var links = document.getElementsByClassName('checksum');
  for (var i = 0; i<links.length; i++) {
      links[i].href = (checksum === undefined) ? fallback : checksum;
  }
}
