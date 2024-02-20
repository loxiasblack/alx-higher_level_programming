#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const film = JSON.parse(body);
  const charactersUrls = film.characters;

  const charactersPromise = charactersUrls.map(url => new Promise((resolve, reject) => {
    request(url, function (error, response, body) {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  }));
  Promise.all(charactersPromise)
    .then(characters => {
      characters.forEach(Element => console.log(Element));
    })
    .catch(error => console.error(error));
});
