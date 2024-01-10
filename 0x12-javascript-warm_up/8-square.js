#!/usr/bin/node
// this function prints a sqaure
const size = parseInt(process.argv[2]);
if (typeof (size) !== 'number' || isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('x'.repeat(size));
  }
}
