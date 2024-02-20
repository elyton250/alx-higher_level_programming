#!/usr/bin/node
// This script reads contents from a file

const fs = require('fs');

// Check if the correct number of command line arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./script.js <filepath>');
  process.exit(1);
}

const filepath = process.argv[2];

// Read contents from the file
fs.readFile(filepath, 'utf-8', (err, contents) => {
  if (err) {
    console.log(err);
    process.exit(1);
  }

  console.log(contents);
});
