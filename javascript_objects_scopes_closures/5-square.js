#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  print () {
    let xline = 'X';
    xline = xline.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(xline);
    }
  }

  rotate () {
    const hold = this.width;
    this.width = this.height;
    this.height = hold;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Square;
