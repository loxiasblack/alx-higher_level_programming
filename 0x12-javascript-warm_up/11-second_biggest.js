#!/usr/bin/node
function findsecondlargest (arr) {
  let largest = arr[2];
  let secondLargest = -Infinity;
  for (let i = 3; i < arr.length; i++) {
    if (arr[i] > largest) {
      secondLargest = largest;
      largest = arr[i];
    } else if (arr[i] < largest && arr[i] > secondLargest) {
      secondLargest = arr[i];
    }
  }
  return secondLargest;
}
const arg = process.argv;
if (arg.length < 4) {
  console.log(0);
} else {
  console.log(findsecondlargest(arg));
}
