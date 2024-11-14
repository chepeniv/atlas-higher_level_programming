#!/usr/bin/node

function factorial (n) {
  if (n < 2) {
    return 1;
  }
  return n * factorial(n - 1);
}

let n = process.argv[2];
n = parseInt(n);
if (isNaN(n)) {
  n = 1;
}
n = factorial(n);
console.log(n);
