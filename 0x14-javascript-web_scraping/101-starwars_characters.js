#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (err, res, body) {
  if (!err) {
    const chars = JSON.parse(body).characters;
    printChars(chars, 0);
  }
});

function printChars (characters, index) {
  request(characters[index], function (err, res, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printChars(characters, index + 1);
      }
    }
  });
}
