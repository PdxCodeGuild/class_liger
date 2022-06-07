const app = new Vue({
  // define the app's container element
  el: '#vue-app',

  // define custom 'delimiters' to avoid conflict with Django's Jinja syntax
  delimiters: ['[[', ']]'],

  // data attribute is the app's "state"
  data: {
    headerText: 'Welcome to Vue JS!!!',
    counter: 0,
    randomNumber: null,
    generatedNumbers: [],
    userData: null
  },

  // methods attribute will define functions that the app can call internally
  methods: {
    increment: function(){
      this.counter++
    },
    decrement: function() {
      this.counter--
    },
    generateRandomNumber: function(){
      // if the random number is not null, add it to the array of numbers
      if(this.randomNumber){
        this.generatedNumbers.push(this.randomNumber)
      }

      // generate a new number 1-10
      this.randomNumber = Math.round(Math.random()*10) + 1
    }
  },

  // lifecycle methods happen at various stages of the app's time on the screen
  created: function(){
    console.log('Created!');

    setTimeout(()=>{
      axios.get('https://jsonplaceholder.typicode.com/users/1')
      .then(response=>{
        this.userData = response.data
      })
    }, 2000)
  },
  updated: function(){
    console.log('Updated!')
  }
})

// console.log(app)