#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printChars(characters, 0);
  }
});
// the function that recurses
function printChars (characters, index) {
  request(characters[index], function (error, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printChars(characters, index + 1);
      }
    }
  });
}
