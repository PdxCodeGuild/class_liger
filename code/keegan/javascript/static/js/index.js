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



// switch statements
let choice = 'no'
switch(choice){
  case 'yes':
    // console.log('You chose yes!')
    break

  case 'no':
    // console.log('You chose no!')
    break

  default:
    // console.log('invalid selection!')
}


// ternary if statements
// if condition ? do this : (else) do this
let q = 8
let result = q % 2 === 0 ? 'even' : 'odd'
// console.log(result)

const data = {
  'username': 'user1'
}

const username = data.username
// if the value for password doesn't exist, provide a default
const password = data.password ? data.password : 'defaultPassword'

// console.log(username, password)

q = null
result = q ? q : 10
// console.log(result) // 10

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


// ============================================== //

// LOOPS

// while loop
let i = 0
while (i < 10){
  i++
  // console.log(i)
}


// for loops
// for(initialization; condition; increment){}
for(let j = 0; j < 10; j++){
  // console.log(j)
}

// count down from 10->1
for(let k = 10; k > 0; k--){
  // console.log(k)
}

// iterate over a string or array

const string = 'ABCDEFG'
i = 0
while(i < string.length){
  // console.log(string[i])
  i++
}

for (j = 0; j < string.length; j++){
  // console.log(string[j])
}

// get a NodeList of all the divs with the class 'box'
let boxes = document.querySelectorAll('.box')
let boxArray = Array.from(boxes)

// console.log(boxes)                   // [ div.box, div.box, div.box, div.box, div.box, div.box, div.box, div.box, div.box, div.box ]
// console.log(Array.isArray(boxes))    // false
// console.log(boxArray)                // [ div.box, div.box, div.box, div.box, div.box, div.box, div.box, div.box, div.box, div.box ]
// console.log(Array.isArray(boxArray)) // true

// loop through the box divs and size each
// based on its position in the array
for(k = 0; k<boxes.length; k++){
  let box = boxes[k]

  box.style.height = `${10 * k}px`
  box.style.width = `${10 * k}px`
  box.style.backgroundColor = 'black'
  box.style.margin = '10px'
}


// for-in will iterate over the indices of the sequence
for(i in string) {
  // console.log(i, string[i])
}

// for-of will iterate over the elements in the sequence
for(let char of string){
  // console.log(char, string.indexOf(char))
}


// Array methods .forEach, .map, .filter, .reduce

// Array.forEach() will loop through the array
// and call the callback function with each element

let numbers = [1,2,3,4,5,6,7,8,9]
let squares = []

result = numbers.forEach((number)=>{
  squares.push(number ** 2)
})

// console.log(result) // undefined
// console.log(squares) // [ 1, 4, 9, 16, 25, 36, 49, 64, 81 ]


// .map() calls the callback function with each element and 
// returns from the callback the new value for the element
squares = numbers.map((number)=>{
  return number ** 2
})

// console.log(squares) //  [ 1, 4, 9, 16, 25, 36, 49, 64, 81 ]

// use the spread operator to place all the characters in an array
let letters = [...string]
// console.log(letters) // [ "A", "B", "C", "D", "E", "F", "G" ]

letters = letters.map(letter=>{
  return letter + letter
})
// console.log(letters) // [ "AA", "BB", "CC", "DD", "EE", "FF", "GG" ]

letters = letters.join('')
// console.log(letters) // AABBCCDDEEFFGG


// .filter() calls the callback function with each element and 
// returns from the callback a boolean indicating if the element is to be kept or not

numbers = [ 1, 4, 9, 16, 25, 36, 49, 64, 81 ]
// numbers = numbers.filter((number)=>{
//   evenOrOdd = number % 2

//   if(evenOrOdd === 0){
//     return true
//   } else {
//     return false
//   }
// })

// use the arrow function's intrinsic return value 
// to return the boolean that's the result of the modulus comparison
const evens = numbers.filter(number => number % 2 === 0)
const odds = numbers.filter((number) => number % 2 === 1)


// console.log(evens, odds)

// .reduce() - combine the elements in the array based on a condition
const sum = numbers.reduce((previousValue, currentValue,)=>{
  // console.log(previousValue, currentValue)
  return previousValue + currentValue
})

// console.log(sum) // 285

numbers.map((number,index,arr)=>{
  // console.log(number)
  // console.log(index)
  // console.log(arr)
  // console.log()
})

