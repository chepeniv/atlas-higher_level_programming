#!/usr/bin/node

let message = 'Not a number';
let first = process.argv[2];

first = parseInt(first);
if (!isNaN(first)) {
  message = 'My number: ' + first;
}

console.log(message);
