#!/usr/bin/node
// this prints argum
let count = 0;
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
