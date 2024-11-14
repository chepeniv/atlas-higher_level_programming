#!/usr/bin/node

let message = process.argv[2];

if (message === undefined) {
  message = 'No argument';
}

console.log(message);
