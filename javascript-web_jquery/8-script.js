#!/usr/bin/node

// fetch and list the title for all movies in the ul#list_movies tag
// from the url https://swapi-api.hbtn.io/api/films/?format=json
// document.querySelector is not allowed
// use the jquery api
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

$.get(url, (data, stat) => {
  for (movie of data.results) { 
    const title = `<li>${movie.title}</li>`;
    $(title).appendTo('ul#list_movies');
  }
});
