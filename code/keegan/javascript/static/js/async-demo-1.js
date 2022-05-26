
// ready() will trigger when the document is loaded
$(document).ready(()=>{

  const    container = $('.container')

  const     username = $('#username')
  const     fullName = $('#full-name')
  const        email = $('#email')
  const        phone = $('#phone')
  const      address = $('#address')
  const  websiteLink = $('#website-link')

  const        modal = $('.modal')
  const       button = $('#button')
  // hide the container and then fade it in over 1 second
  // container.hide().fadeIn(1000)

  /**
   * 
   * @param {object} userData 
   * 
   * Apply the userData from the API call to the DOM elements and hide the loading modal
   */
  function setContent(userData){
    username.text(userData.username)
    fullName.text(userData.name)
    email.text(userData.email)
    phone.text(userData.phone)
    websiteLink.text(userData.website)
    
    address.html(`
    <p>
    ${userData.address.street} <br/>
    ${userData.address.suite} <br/>
    ${userData.address.city} <br/>
    ${userData.address.zipcode} <br/>
    <p>
    `)
    
    // close the modal when the API call comes back
    modal.css('display', 'none');
  }

  /**
   * 
   * @param {number} userId 
   * 
   * Fetch the data for the user with the given
   * userId parameter
   */
  function fetchUser(userId){
    // use setTimeout to emulate a longer response time from the API
    setTimeout(()=>{

      const url = `https://jsonplaceholder.typicode.com/usrs/${userId}` 
      $.ajax({
        url: url,
        method: 'GET',
        // use a named function as the success callback
        success: setContent,
        error: function(error){
          modal.css('color', 'red')
          modal.html(`<h1>${error.status}! ${error.statusText}!</h1>`)
        }
      })
    }, 1000)
  }



  // When the button is clicked, generate a random userId, 
  // show the loading modal, and call the API
  button.click(()=>{
    // generate random userId 1 - 10
    const userId = Math.floor(Math.random() * 10) + 1

    // popup the modal
    modal.css('display', 'block');

    // call the API with the random userId
    fetchUser(userId)
  })


  // load initial data
  fetchUser(1)


})














// // console.log('A');

// setTimeout(()=>{
//   // console.log('B')
// }, 3000)

// // console.log('C');
// // ==============================================================//


// // console.log('A');
// setTimeout(()=>{

//   // console.log('B')

//   setTimeout(()=>{
//     // console.log('C');
//   }, 1000)

// }, 1000)

// // console.log('D')

// // ==============================================================//

// // call the callback repeatedly after the given interval
// let count = 0;

// const timer = setInterval(()=>{
//   console.log(count);
//   count++

//   // delete the interval when the count is greater than 10
//   if(count > 10){
//     console.log('END!')
//     clearInterval(timer)
//   }
// }, 1000)
