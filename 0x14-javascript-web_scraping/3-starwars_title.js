#!/usr/bin/node

const request = require('request');
const process = require('process');

const episode = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${episode}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
