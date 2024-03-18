#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};

for (const object in dict) {
  const reverseKey = dict[object];
  if (!newDict[reverseKey]) newDict[reverseKey] = [];
  newDict[reverseKey].push(object);
}
console.log(newDict);
