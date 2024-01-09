#!/usr/bin/node
// thsi prinst arguments
const args = process.argv;
if (args[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No arguments');
}
