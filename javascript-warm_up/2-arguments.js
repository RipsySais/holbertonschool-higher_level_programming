#!/usr/bin/node
// Cette ligne indique que le script doit être exécuté avec Node.js

// Récupère les arguments passés au script en ignorant les deux premiers éléments de process.argv
// process.argv contient :
// - process.argv[0] : le chemin vers l'exécutable Node.js
// - process.argv[1] : le chemin vers le script en cours d'exécution
// - process.argv[2...] : les arguments passés par l'utilisateur

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
