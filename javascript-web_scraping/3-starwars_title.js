#!/usr/bin/node

const request = require('request');
const swapi = 'https://swapi-api.hbtn.io/api/films/';
const episode = process.argv[2];

request(swapi + episode, (err, response, body) => {
  if (err) console.log(err);
  else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
