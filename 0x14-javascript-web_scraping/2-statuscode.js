#!/usr/bin/node
// Shows the status code of the passed URL

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./script.js <url>');
  process.exit(1); // Exit with an error code
}

const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.error(`Error requesting URL: ${error.message}`);
    process.exit(1);
  }

  console.log(`code: ${response.statusCode}`);
});
