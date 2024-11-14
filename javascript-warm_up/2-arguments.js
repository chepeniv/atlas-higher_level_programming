#!/usr/bin/node

let count = process.argv.slice(2).length;

if (count > 2) {
  count = 2;
}

const cases = [
  'No argument',
  'Argument found',
  'Arguments found'
];

console.log(cases[count]);
