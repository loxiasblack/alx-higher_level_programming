#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const myDictionary = {};
    const data = JSON.parse(body);
    data.forEach(item => {
      // Check if the task is completed
      if (item.completed) {
        // If the userId exists in myDictionary, increment, else initialize to 1
        if (myDictionary[item.userId]) {
          myDictionary[item.userId]++;
        } else {
          myDictionary[item.userId] = 1;
        }
      }
    });
    console.log(myDictionary);
  }
});
