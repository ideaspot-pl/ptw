// index.js
for (let lang of ["pl", "en", "de"]) {
  const { sayHello, sayBye } = require(`./${lang}.js`);
  sayHello("Artur");
  sayBye("Artur");
}
