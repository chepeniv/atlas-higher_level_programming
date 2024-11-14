#!/usr/bin/node

let size = process.argv[2];
const x = 'X';
let message = 'Missing size';

size = parseInt(size);
if (isNaN(size)) {
  size = 1;
} else {
  message = x.repeat(size);
}

for (let i = 0; i < size; i++) {
  console.log(message);
}
