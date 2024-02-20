#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const obj = JSON.parse(response.body);
    for (const key in obj) {
      if (key === 'title') {
        console.log(obj[key]);
      }
    }
  }
});
