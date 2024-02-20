#!/usr/bin/node
// This module writes to a file

const fs = require('fs');

// Check if the minimum number of command line arguments is provided
if (process.argv.length < 4) {
  console.error('Usage: ./script.js <filepath> <contents>');
  process.exit(1); // Exit with an error code
}

const filepath = process.argv[2];
const contents = process.argv[3];

fs.writeFile(filepath, contents, 'utf-8', (err) => {
  if (err) {
    console.error(`Error writing to file: ${err.message}`);
    process.exit(1);
  }

  // console.log('Content has been written to the file successfully.');
});
