#!/usr/bin/node

const process = require('process');
const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  let i = 1;
  const dictionary = {};
  while (i < 11) {
    let count = 0;
    data.forEach(element => {
      if (element.userId === i && element.completed === true) {
        count++;
      }
    });
    dictionary[i] = count;
    i++;
  }
  console.log(dictionary);
});
