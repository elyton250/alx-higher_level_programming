#!/usr/bin/node

// This script fetches content from a webpage and stores it in a file

const request = require('request');
const fs = require('fs');

if (process.argv.length !== 4) {
  console.error('Usage: ./script.js <web-url> <output-file>');
  process.exit(1);
}

const webUrl = process.argv[2];
const filepath = process.argv[3];

request(webUrl, (error, response, body) => {
  if (error) {
    console.error(`Error making the request: ${error}`);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Status code ${response.statusCode}`);
    process.exit(1);
  }

  if (body) {
    fs.writeFile(filepath, body, 'utf-8', (err) => {
      if (err) {
        console.error(`Error writing to file: ${err.message}`);
        process.exit(1);
      }

    //   console.log('Content has been written to the file successfully.');
    });
  }
});
