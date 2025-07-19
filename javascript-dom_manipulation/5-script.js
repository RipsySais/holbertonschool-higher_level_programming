// Select the update button and header elements
const updateHeader = document.querySelector('#update_header');
const header = document.querySelector('header');

// Add click event listener to the update button
updateHeader.addEventListener('click', function() {
  // Update the header text content
  header.textContent = 'New Header!!!';
});
