#!/usr/bin/node

const preSquare = require('./5-square.js');

class Square extends preSquare {
  charPrint (c = 'X') {
    c = c.repeat(this.width);
    for (let i = 0; i < this.width; i++) {
      console.log(c);
    }
  }
}

module.exports = Square;
