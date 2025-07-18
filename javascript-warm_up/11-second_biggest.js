#!/usr/bin/node
// Trouve le deuxième plus grand nombre parmi les arguments

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  const sorted = [...new Set(args)].sort((a, b) => b - a);
  console.log(sorted.length > 1 ? sorted[1] : 0);
}
