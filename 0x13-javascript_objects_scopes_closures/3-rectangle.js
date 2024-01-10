#!/usr/bin/node
// This class defines a rectangle
class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('x'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
