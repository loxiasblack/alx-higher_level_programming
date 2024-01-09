#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let world = '';
      for (let j = 0; j < this.width; j++) {
        world += 'X';
      }
      console.log(world);
    }
  }
}

module.exports = Rectangle;
