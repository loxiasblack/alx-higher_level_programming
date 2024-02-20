#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const title = process.argv[2];
request.get(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    for (const obj in data) {
      if (obj === 'results') {
        for (let index = 0; index < data[obj].length; index++) {
          if (index === parseInt(title) - 1) {
            const movie = data[obj][index];
            for (const data in movie) {
              if (data === 'characters') {
                for (let item = 0; item < movie[data].length; item++) {
                  request.get(movie[data][item], function (error, response, body) {
                    const core = JSON.parse(body);
                    for (const key in core) {
                      if (key === 'name') {
                        console.log(core[key]);
                      }
                    }
                  });
                }
              }
            }
          }
        }
      }
    }
  }
});
