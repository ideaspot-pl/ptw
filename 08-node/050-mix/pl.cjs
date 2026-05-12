//pl.cjs
const sayHello = (name) => {
  console.log(`Cześć ${name}!`)
}

const sayBye = (name) => {
  console.log(`Pa ${name}!`)
}

module.exports = {
  sayHello,
  sayBye,
}
