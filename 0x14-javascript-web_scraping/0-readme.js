#!/usr/bin/node

const process = require('process');
const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  }
  console.log(data);
});
