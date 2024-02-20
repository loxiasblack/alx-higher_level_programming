#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (error, response) {
  if (error) {
    console.error(error);
  } else {
    let count = 0;
    const obj = JSON.parse(response.body);
    for (let key in obj) {
      if (key === 'results') {
        const data = obj[key];
        for (let index = 0; index < data.length; index++) {
          for (key in data[index]) {
            if (key === 'characters') {
              const characters = data[index][key];
              for (let index = 0; index < characters.length; index++) {
                if (characters[index] === 'https://swapi-api.alx-tools.com/api/people/18/') {
                  count++;
                }
              }
            }
          }
        }
      }
    }
    console.log(count);
  }
});
