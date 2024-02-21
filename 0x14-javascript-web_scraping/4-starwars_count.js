#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const obj = JSON.parse(body).results;
    let count = 1;
    obj.forEach(element => {
      for (const item in element) {
        if (item === 'characters') {
          const characters = element[item];
          characters.forEach(names => {
            if (names === 'https://swapi-api.alx-tools.com/api/people/18/') {
              count++;
            }
          });
        }
      }
    });
    console.log(count);
  }
});
