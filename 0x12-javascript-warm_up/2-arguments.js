#!/usr/bin/node
// this prints arguments
const args = process.argv.length - 2;
if (args === 0) {
  console.log('No arguments');
} else if (args === 1) {
  console.log('One argument found');
} else {
  console.log('Arguments found');
}
