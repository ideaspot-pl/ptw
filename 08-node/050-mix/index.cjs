// index.cjs
console.log('a');
const { sayHello } = require("./en.mjs");
const { sayBye } = require("./pl.cjs");

sayHello("Artur");
sayBye("Artur");
