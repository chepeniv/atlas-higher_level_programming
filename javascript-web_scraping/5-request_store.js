#!/usr/bin/node

const fs = require('node:fs');
const request = require('request');

const url = process.argv[2];
const filename = process.argv[3];

request(url, (err, response, body) => {
  if (err) console.log(err);
  else {
    fs.writeFile(filename, body, 'utf8',
      (err) => {
        if (err) console.log(err);
      });
  }
});
