// select DOM elements
const addBoxButton = document.querySelector('#add-box-button')
const plusSign = document.querySelector('#plus-sign')
const boxDemoContainer = document.querySelector('#events-demo-2')

// generate a random number between two numbers
function randomInt (low, high) {
  return Math.floor(Math.random() * (1 + high - low) + low)
}


// apply the 'grow' class to the button when the mouse is over it
// and remove it when the mouse leaves
addBoxButton.addEventListener('mouseenter', function () {
  plusSign.classList.add('grow')
})
addBoxButton.addEventListener('mouseleave', function () {
  plusSign.classList.remove('grow')
})

addBoxButton.addEventListener('click', function () {
  // create an empty div
  let box = document.createElement('div')

  // add the .box class to the box
  box.classList.add('box')

  // apply styles to the box
  box.style.height = '250px'
  box.style.width = '250px'
  box.style.display = 'flex'
  box.style.justifyContent = 'center'
  box.style.alignItems = 'center'
  
  // apply random background color
  let r = randomInt(0, 255),
  g = randomInt(0, 255),
  b = randomInt(0, 255)
  box.style.backgroundColor = `rgba(${r}, ${g}, ${b}, .5)`

  // remove the box when it is clicked
  box.addEventListener('click', function(){
    boxDemoContainer.removeChild(box)
  })

  // when the mouse moves inside the box,
  // display the mouse's coordinates in the box
  box.addEventListener('mousemove', function(event){
    box.innerHTML = `<h1>x: ${event.screenX}, <br/>y: ${event.screenY}</h1>`
  })
  box.addEventListener('mouseleave', function(event){
    box.innerHTML = ''
  })

  // scroll the window to the bottom of the screen
  window.scrollTo(0, document.body.scrollHeight)

  // add the box to the container
  boxDemoContainer.appendChild(box)
})

// delete all boxes when the escape key is pressed 
window.addEventListener('keyup', function(event){
  // if the escape is pressed
  if(event.key === 'Escape'){
    // target all the boxes
    let boxes = document.querySelectorAll('.box')
    
    // remove all boxes
    for(let box of boxes){
      boxDemoContainer.removeChild(box)
    }
  }
})