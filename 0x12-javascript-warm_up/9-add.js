#!/usr/bin/node
// this function adds
function add (a, b) {
  a = parseInt(process.argv[2]);
  b = parseInt(process.argv[3]);
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    const c = a + b;
    console.log(c);
  }
}
add();
