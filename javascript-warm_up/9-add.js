#!/usr/bin/node

function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  console.log(a + b);
}

const first = process.argv[2];
const second = process.argv[3];
add(first, second);
