#!/usr/bin/node
const factorial = (n) => {
    if (isNaN(n) || n === 0) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
};
const num = parseInt(arg, 10);
console.log(factorial(num));
