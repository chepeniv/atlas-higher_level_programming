#!/usr/bin/node

function main () {
  let numbers = process.argv.slice(2);
  if (numbers.length < 2) {
    console.log(0);
    return;
  }
  numbers = numbers.map((num) => Number(num));
  numbers = numbers.sort((a, b) => a - b);
  console.log(numbers[numbers.length - 2]);
}

main();
