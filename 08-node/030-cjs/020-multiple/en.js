//en.js
module.exports.sayHello = (name) => {
  console.log(`Hello ${name}!`)
}

const sayBye = (name) => {
  console.log(`Bye ${name}!`)
}
module.exports.sayBye = sayBye;
