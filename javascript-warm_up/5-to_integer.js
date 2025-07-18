#!/usr/bin/node
// Script qui vérifie si le premier argument est un nombre entier

const arg = process.argv[2];
const num = parseInt(arg);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
