#!/usr/bin/node

const fs = require('fs');
const process = require('process');
const conTent1 = fs.readFileSync(process.argv[2], 'utf-8');
const conTent2 = fs.readFileSync(process.argv[3], 'utf-8');

const concatenatContent = conTent1 + conTent2;

fs.writeFileSync(process.argv[4], concatenatContent, 'utf-8');
