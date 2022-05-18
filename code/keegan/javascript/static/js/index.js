// single-line comments start with double forward slash
// alert('hello world!') // creates a popup in the browser

// "print" something in the browser console
// console.log('hello from external js file!')

// in JS, variables must be 'declared'

// const - cannot use the same variable name twice (can't be redefined)
const x = 5
// const x = 5 // cannot 'redeclare' 'x'

// let - scoped to the current block
let y = 10

if (x === 5) {
  let y = 8
  // console.log(y) // 8 - y is only 8 inside the if statement
}

// console.log(y) // 10 - y is 10 outside the if statement

// var - creates a variable in the global scope
var z = 3

if (x === 5) {
  var z = 7
  // console.log(z) // 7 - z is redefined because 'var' makes it global
}

// console.log(z) // 7

// ======================================================================== //

// Datatypes
let a = 5 // number
let b = 10.5 // number
let c = 'Hello' // string
let d = true // boolean
let e = false // boolean
let f = null // null - defined with no value
let g = undefined // undefined - not yet defined
let fruits = ['apple', 'banana', 'mango'] // Array

// console.log(fruits[0]) // apple

// JS 'objects' are like Python dictionaries
let person = {
  firstName: 'John',
  lastName: 'Doe',
  age: 46,
  address: {
    street: '123 Faux St.',
    city: 'Portland'
  }
}

// access values within objects
const key = 'firstName'
// console.log(person['firstName']) // John
// console.log(person[key]) // John
// console.log(person.firstName) // John - access object attributes with dot notation
// console.log(person.address.city) // Portland


// ==========================================================================

// all math operators are the same as Python
// JS doesn't have floor division

// JS has ++ and -- instead of += 1 and -= 1

// ++ increment
a = 10
// console.log(a)
// // post-increment
// console.log('post-increment: ', a++) // 10
// console.log(a) // 11
// // pre-increment
// console.log('pre-increment: ', ++a) // 12

// // -- decrement
// console.log('post-decrement', a--) // 12
// console.log(a) // 11
// console.log('pre-decrement', --a) // 10

// ======================================================================== //

// Math object
// console.log(7/3) // 2.3333333333333335
// console.log(Math.floor(7/3)) // 2

// generate a random number between 0 and 1
// console.log(Math.random())

// generate a random number between 0 and 100
// console.log(Math.random() * 100)

// generate a random number between 50 and 100
// console.log(50 + (Math.random() * 50))

// random element from an array
fruits = ['apple', 'banana', 'mango']

// generate a random index
let randomIndex = Math.floor(Math.random() * fruits.length)
// console.log(randomIndex, fruits[randomIndex])

