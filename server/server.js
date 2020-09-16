// imports
const path = require('path');
const express = require('express');

// Express app
const app = express();

const p = path.normalize(__dirname + '\\..\\docs\\')

console.log('static public path', p)

app.use(express.static(p));

const server = app.listen(5000);

console.log("end of file");

