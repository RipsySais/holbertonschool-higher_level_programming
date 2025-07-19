// Get the add item button and the list elements
const addItem = document.querySelector('#add_item');
const myList = document.querySelector('ul.my_list');

// Add click event listener to the button
addItem.addEventListener('click', function() {
  // Create a new list item element
  const newItem = document.createElement('li');
  
  // Set its text content
  newItem.textContent = 'Item';
  
  // Append it to the list
  myList.appendChild(newItem);
});
