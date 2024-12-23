#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) console.log(err);
  else {
    const data = JSON.parse(body).results;
    let wedgeAntilles = [];
    for (const movie in data) {
      const characters = data[movie].characters;
      const appearance = characters.filter(
        (entry) => entry.endsWith('/18/'));
      wedgeAntilles = wedgeAntilles.concat(appearance);
    }
    console.log(wedgeAntilles.length);
  }
});
