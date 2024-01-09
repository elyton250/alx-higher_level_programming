#!/usr/bin/node
// this number
const num = parseInt(process.argv[2]);
if (typeof (num) !== 'number' || isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
