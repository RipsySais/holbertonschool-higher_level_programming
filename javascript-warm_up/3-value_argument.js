#!/usr/bin/env node
// Script qui affiche le premier argument passé ou "No argument" si aucun argument

// Récupère le premier argument (indice 2 dans process.argv)
const premierArgument = process.argv[2];

// Vérifie si l'argument est undefined (non fourni)
if (premierArgument === undefined) {
  console.log('No argument');
} else {
  console.log(premierArgument);
}
