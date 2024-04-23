#!/usr/bin/node

const process = require('process');
const request = require('request');
const fs = require('fs');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  }
  fs.writeFile(process.argv[3], body, 'utf-8', (error) => {
    if (error) {
      console.error(error);
    }
  });
});
