#!/usr/bin/node

const process = require('process');
const request = require('request');

const url = process.argv[2];
const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
let count = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  const results = data.results;
  results.forEach(result => {
    const characters = result.characters;
    characters.forEach(character => {
      if (character === characterUrl) {
        count++;
      }
    });
  });
  console.log(count);
});
