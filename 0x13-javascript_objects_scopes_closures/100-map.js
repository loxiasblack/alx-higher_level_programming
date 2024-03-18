#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const newList = list.map(function (element, index) {
  return element * index;
});
console.log(newList);
