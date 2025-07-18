#!/usr/bin/env node
// Script qui affiche deux arguments sous la forme "arg1 is arg2"

// Récupère les deux premiers arguments
const arg1 = process.argv[2];
const arg2 = process.argv[3];

// Affiche au format demandé
console.log(`${arg1} is ${arg2}`);
