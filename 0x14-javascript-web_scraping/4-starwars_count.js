#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (error, response) {
  if (error) {
    console.error(error);
  } else {
    let count = 0;
    const obj = JSON.parse(body);
    console.log(obj)
  }
});
