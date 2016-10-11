$(function() {
  // Don't forget the break statement when adding here!
  switch(Detectizr.os.name) {
    case 'windows':
      $('.fmw-generic').addClass('hidden');
      $('.fmw-windows').removeClass('hidden');
      $('.fmw-all').removeClass('hidden');
      break;
    case 'linux':
      $('.fmw-generic').addClass('hidden');
      $('.fmw-linux').removeClass('hidden');
      $('.fmw-all').removeClass('hidden');
      break;
    case 'mac os':
      $('.fmw-generic').addClass('hidden');
      $('.fmw-macos').removeClass('hidden');
      $('.fmw-all').removeClass('hidden');
      break;
    default:
      // Do nothing. We show .fmw-generic by default already.
      $('.fmw-generic').removeClass('hidden');
      break;
  }
});
