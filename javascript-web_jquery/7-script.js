#!/usr/bin/node

// fetch the character name from 
// https://swapi-api.hbtn.io/api/people/5/?format=json
// display the name in div#character 
// cannot use document.querySelector
// must use the jquery api
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

$.get(url, (data, stat) => {
	$('div#character').text(data.name);
})
