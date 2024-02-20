#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const myDictionary = {};
    let userId = 1;
    const data = JSON.parse(body);
    while (userId < 11) {
      let tasKcounter = 0;
      for (let index = 0; index < data.length; index++) {
        for (const item in data[index]) {
          if (data[index][item] === userId && data[index].completed === true) {
            tasKcounter++;
          }
        }
      }
      myDictionary[String(userId)] = tasKcounter;
      userId++;
    }
    console.log(myDictionary);
  }
});
