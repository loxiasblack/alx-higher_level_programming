#!/usr/bin/node
const args = process.argv;
const x = parseInt(args[2]);
if (!x) {
  console.log('Missing size');
} else {
  for (let y = 0; y < x; y++) {
    let s = '';
    for (let z = 0; z < x; z++) {
      s += 'X';
    }
    console.log(s);
  }
}
