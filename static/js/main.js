// navbar script
function toggleOffcanvas() {
  var offcanvas = document.querySelector('.offcanvas');
  var hamoverlay = document.querySelector('.hamoverlay');

  offcanvas.style.display = (offcanvas.style.display === 'flex') ? 'none' : 'flex';
  hamoverlay.style.display = (hamoverlay.style.display === 'block') ? 'none' : 'block';
}