// Fetch the list of Star Wars movies
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    const movies = data.results; // Get the array of movies
    const listMovies = document.getElementById('list_movies');
    
    // Loop through each movie and add its title to the list
    movies.forEach(movie => {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      listMovies.appendChild(listItem);
    });
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });
  