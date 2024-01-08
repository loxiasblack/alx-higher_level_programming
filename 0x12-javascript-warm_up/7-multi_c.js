#!/usr/bin/node
const args = process.argv;
let x = parseInt(args[2]);
if (!x) {
  console.log('Missing number of occurrences');
} else {
  for (x; x > 0; x--) {
    console.log('C is fun');
  }
}
