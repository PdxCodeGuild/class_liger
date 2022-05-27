let likeButtons = document.querySelectorAll('.like'),
      csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0]


// shared headers and other config options for axios
const axiosConfig = {
  headers: {
    'Content-Type': 'application/json', // expect JSON data to be returned from the API
    'X-CSRFToken': csrfToken.value // include Django's CSRF Token
  },
  xsrfHeaderName: 'X-CSRFToken' // so axios knows to use this header for csrf token
}


function handleLikeEvent(event){

  // the event parameter is populated when the element is clicked
  // and has info about the event

  // isolate the picId from the clicked like button
  let picId = event.target.id
  // [ "like", "2" ]
  picId = picId.split('-')[1]


  // url for the like request, including the picId
  url = 'http://localhost:8000/like/' + picId

  // axios.post(url, data, config)
  axios.post(url, {}, axiosConfig)
    .then(response=>{
      // grab values out of response object
      const isLiked = response.data.isLiked
      const likeCount = response.data.likeCount

      // target the like button and count container for the clicked element
      const likeButton = document.querySelector(`#like-${picId}`)
      const countSpan = document.querySelector(`#like-count-${picId}`)

      // update the pic's like count
      countSpan.innerText = likeCount

      // render red heart if pic is liked, otherwise render heart outline
      if(isLiked){
        likeButton.classList.remove('bi-heart')
        likeButton.classList.add('bi-heart-fill', 'text-danger')
      } else {
        likeButton.classList.remove('bi-heart-fill', 'text-danger')
        likeButton.classList.add('bi-heart')
      }
    })
    .catch(error=>console.log(error))

}


// add an event listener to each button which will trigger an 
// axios request to like the clicked pic
likeButtons.forEach(likeButton=>{
  likeButton.addEventListener('click', handleLikeEvent)
})