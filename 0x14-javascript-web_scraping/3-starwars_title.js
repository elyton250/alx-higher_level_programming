#!/usr/bin/node
// This module retrieves data from the Star Wars API

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./script.js <movieId>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error reaching the API:', error.message);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Status code ${response.statusCode}`);
    process.exit(1);
  }

  const movie = JSON.parse(body);
  console.log(movie.title);
});
