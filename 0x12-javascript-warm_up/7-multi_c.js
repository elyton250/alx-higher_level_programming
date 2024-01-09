#!/usr/bin/node
// prints x times
const fiArg = parseInt(process.argv[2]);
if (typeof fiArg !== 'number' || isNaN(fiArg)) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < fiArg; i++) {
  console.log('C is fun');
}
