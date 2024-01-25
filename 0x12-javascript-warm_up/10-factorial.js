#!/usr/bin/node
// factorial function
function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const args = process.argv;
let x = parseInt(args[2]);
if (!x) {
  x = 1;
}
console.log(factorial(x));
