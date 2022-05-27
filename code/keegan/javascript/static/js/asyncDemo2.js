let h1 = document.querySelector('#result'),
button = document.querySelector('#button')

const headers = {
  Accept: 'application/json'
}

const url = 'https://icanhazdadjoke.com/lalalala'

// let promise = new Promise((resolve, reject)=>{
//   let number = 3

//   // simulate an API call or other async operation
//   setTimeout(()=>{
//     if(number % 2 === 0){
//       resolve(`Yay! ${number} is even!!!`)
//     } else {
//       reject(`Oops! ${number} is odd!!!`)
//     }
//   }, 2000)
// })

// console.log(promise)

// promise
//   .then(result=>{
//     return result
//   })
//   .catch(error=>console.error(error))


// =========================================================


function isEven(number){
  return new Promise((resolve, reject)=>{
      // simulate an API call or other async operation
      setTimeout(()=>{
        if(number % 2 === 0){
          resolve(`Yay! ${number} is even!!!`)
        } else {
          reject(`Oops! ${number} is odd!!!`)
        }
      }, 2000)
    })
}

function checkEven() {
// generate random number
let number = Math.floor(Math.random() * 100)

// show loading state when the promise is pending
h1.style.color = 'black'
h1.innerText = 'Thinking...'

// isEven returns a promise
isEven(number)
  .then(result=>{
    // if the promise resolves, set the h1 to the resulting text
    h1.style.color = 'green'
    h1.innerText = result
  })
  .catch(error=>{
    // if the promise is rejected, set the h1 to the error text
    h1.style.color = 'red'
    h1.innerText = error
  })
}












// check the original response and handle errors as they occur
// (only required with fetch() API, not axios)
function CheckError(response) {
  if (response.status >= 200 && response.status <= 299) {
    return response.json();
  } else {
    throw Error(response.statusText);
  }
}

function fetchDadJoke() {
  // fetch(url, options)
  fetch(url, {
    method: 'GET',
    headers: headers
  })
  .then(response=>response.json()) // get the json data from the response
  .then(data=>{
    // pull the joke text from the resulting data and make it the text of the h1
    h1.innerText = data.joke
  })
}











function axiosDadJoke(){

  axios.get(url, {
    headers: headers
  })
  .then(response=>{
    h1.innerText = response.data.joke
  })
  .catch(error=>{
    h1.innerText = 'Oops! ' + error.response.data.message
  })
}




button.addEventListener('click', ()=>{
  // checkEven()
  fetchDadJoke()
  // axiosDadJoke()
})