// Sélectionne l'élément avec l'ID 'red_header'
const redHeaderElement = document.querySelector('#red_header');

// Ajoute un écouteur d'événement pour le clic
redHeaderElement.addEventListener('click', function() {
  // Sélectionne l'élément header
  const headerElement = document.querySelector('header');
  
  // Ajoute la classe 'red' au header
  headerElement.classList.add('red');
});
