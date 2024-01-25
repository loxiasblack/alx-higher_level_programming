#!/usr/bin/node
// function add to numbers
function add (a, b) {
  return a + b;
}
const args = process.argv;
const x = parseInt(args[2]);
const y = parseInt(args[3]);
console.log(add(x, y));
