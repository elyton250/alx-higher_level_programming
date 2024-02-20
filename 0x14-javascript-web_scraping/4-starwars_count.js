#!/usr/bin/node
// This script uses an ID to filter an API

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./script.js <api-url>');
  process.exit(1);
}

const url = process.argv[2];
// create the function to get the character from the people api
const character = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (error, response, body) => {
  if (error) {
    console.error('Error reaching the API:', error.message);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Status code ${response.statusCode}`);
    process.exit(1);
  }

  const content = JSON.parse(body);

  // console.log(content.results)

  // console.log(content.results.length);

  let count = 0;

  for (let i = 0; i < content.results.length; i++) {
    for (let j = 0; j < content.results[i].characters.length; j++) {
      // console.log(`checking: ${content.results[i].characters[j]} against ${character}`);
      if (content.results[i].characters[j] === character) {
        count++;
      }
    }
  }

  // console.log(count);

  // Check each character in the results array
  //   let i = 0
  //   content.results.forEach(result => {
  //     if (result[i].characters === character) {
  //       count++;
  //     }
  //     count++;
  //   });

  console.log(count);
});
