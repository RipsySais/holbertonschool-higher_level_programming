// Sélectionne l'élément avec l'ID 'red_header'
const redHeaderElement = document.getElementById('red_header');

// Ajoute un écouteur d'événement pour le clic
redHeaderElement.addEventListener('click', function() {
  // Sélectionne l'élément header
  const headerElement = document.querySelector('header');
  
  // Change la couleur du texte en rouge
  headerElement.style.color = '#FF0000';
});
