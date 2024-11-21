#!/usr/bin/node

// read and print the contents of a file
// do so in utf-8 mode
// if an error occurs during reading print the error object
// usage: ./0-readme.js filename.ext
const fs = require('node:fs');
const buffer = require('node:buffer');

const filename = process.argv[2];
const readBuffer = buffer.Buffer.alloc(512);

try {
  const fd = fs.openSync(filename, 'r');
  fs.readSync(fd, readBuffer);
  const fileString = readBuffer.toString();
  console.log(fileString);
} catch (error) {
  console.log(error);
}
