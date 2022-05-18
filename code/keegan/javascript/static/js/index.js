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
let a = 5, // number
  b = 10.5, // number
  c = 'Hello', // string
  d = true, // boolean
  e = false, // boolean
  f = null, // null - defined with no value
  g = undefined, // undefined - not yet defined
  fruits = ['apple', 'banana', 'mango'] // Array

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

// ================================================================= //

let game_on = false

// python: not game_on
// js: ! means 'not'
// console.log(!game_on) // true

// equality operators change in JS

// beware of 'type coersion'
// == vs ===

// == allows type coersion
// console.log(5 == '5') // true
// console.log(0 == false) // true

// === does not allow type coersion
// console.log(5 === '5') // false
// console.log(0 === false) // false

// checking inequality
a = 3
b = 5
// console.log(a !== b) // true

// logical operators
// and -> &&
// console.log(a === 3 && b === 5) // true
// or -> ||
// console.log(a === 10 || b === 5) // true

//conditionals
let number = 7,
  target = 10

if (number < target) {
  // insert a value into the output using string templating with backticks ``
  // console.log(`${number} is less than ${target}`)
}

let temp = 90

if (temp < 60) {
  // console.log('cold')
} else if (temp < 80) {
  // console.log('warm')
} else {
  // console.log('hot')
}

// strings
let string1 = 'ABCDEFG'

// use an index to get a value
// console.log(string1[1]) // B

string1 = string1.concat(' ', 'HIJK')
// console.log(string1) // ABCDEFG HIJK

// find index of substring
// console.log(string1.indexOf('CDE')) // 2

// find if substring exists in string
// console.log(string1.includes('CDE')) // true
// console.log(string1.includes('XYZ')) // false

// uppercase/lowercase
// console.log('ABC'.toLowerCase()) // abc
// console.log('xyz'.toUpperCase()) // XYZ

// return a substring
// console.log(string1.slice(1, 4)) // 'BCD'
// console.log(string1.substring(1, 4)) // 'BCD'


// Arrays
let colors = [
  'red',
  'green',
  'blue'
]

// get the value at an index
// console.log(colors[1]) // green

// change value at index
colors[1] = 'yellow'
// console.log(colors) // [ "red", "yellow", "blue" ]

// get the length of the array
// console.log(colors.length) // 3

// add a color to the end of the array
// colors.push('purple')
// console.log(colors) // [ "red", "yellow", "blue", "purple" ]

// .concat returns a new array with the added object at the end
colors = colors.concat('purple')
// console.log(colors) // [ "red", "yellow", "blue", "purple" ]


// add a color to the beginning of the array
colors.unshift('pink')
// console.log(colors) // [ "pink", "red", "yellow", "blue", "purple" ]

// remove element from the end of the array
colors.pop()
// console.log(colors) //[ "pink", "red", "yellow", "blue" ]

// remove from the beginning of the array
colors.shift()
// console.log(colors) // [ "red", "yellow", "blue" ]

// join elements into a string
// console.log(colors.join(', ')) // red, yellow, blue

// sort the array in ascending order
// console.log(colors.sort()) // [ "blue", "red", "yellow" ]

// copy arrays with the 'spread' operator (...)
let colors2 = [...colors, 'teal', 'purple']
// console.log(colors2) // [ "red", "yellow", "blue", "teal", "purple" ]
// =============================================================== //

// function add(a, b){
//   return a + b
// }

// console.log(add(2, 10)) // 12


// const add = function(a, b){
//   return a + b
// }



// arrow functions
// const add = (a, b) => {
//   return a + b
// }

// the return value is implied if no curly brackets are used
// const add = (a, b) => a + b
