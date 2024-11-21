#!/usr/bin/node

const fs = require('node:fs');
const filename = process.argv[2];
const fileData = process.argv[3];

fs.writeFile(filename, fileData, 'utf8',
  (err) => {
    if (err) console.log(err);
  });
