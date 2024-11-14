#!/usr/bin/node

let message = 'C is fun';
let number = process.argv[2];

number = parseInt(number);
if (isNaN(number)) {
  number = 1;
  message = 'Missing number of occurrances';
}

for (let i = 0; i < number; i++) {
  console.log(message);
}
