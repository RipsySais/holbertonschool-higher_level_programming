// Get the toggle button and header elements
const toggleHeader = document.querySelector('#toggle_header');
const header = document.querySelector('header');

// Add click event listener to the toggle button
toggleHeader.addEventListener('click', function() {
  // Check current class and toggle
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
  }
});
