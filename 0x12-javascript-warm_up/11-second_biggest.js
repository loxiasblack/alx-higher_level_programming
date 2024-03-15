#!/usr/bin/node
const process = require('process');
if (process.argv.length < 3) {
  console.log(0);
} if (process.argv.length > 2) {
  const array = [];
  let x = 0;
  let i = 0;
  for (let index = 2; index < process.argv.length; index++) {
    x = parseInt(process.argv[index]);
    array.push(x);
  }
  array.sort(function (a, b) { return a - b; });
  while (i < array.length) {
    if (i === array.length - 2) {
      console.log(array[i]);
      break;
    }
    i++;
  }
}
