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
  const result = data.results;
  result.forEach(element => {
    const character = element.characters;
    character.forEach(element => {
      if (characterUrl === element) {
        count++;
      }
    });
  });
  console.log(count);
});
