#!/usr/bin/node
// this calculates factorial
function factorial (a) {
  if (isNaN(a)) {
    console.log('1');
  } else {
    const result = calculateFactorial(a);
    console.log(result);
  }
}

function calculateFactorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * calculateFactorial(n - 1);
  }
}

factorial(parseInt(process.argv[2]));
