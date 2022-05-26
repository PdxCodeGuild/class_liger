const quantityInputs = document.querySelectorAll('.update-quantity-form')
const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0]
const cartTotalDisplay = document.querySelector('#cart-total-price')

const cartItemCountDisplay = document.querySelector('#cart-item-count')

const axiosConfig = {
  headers: {
    'X-CSRFToken': csrfToken.value,
    'Content-Type': 'application/json'
  },
  xsrfTokenName: 'X-CSRFToken'
}

quantityInputs.forEach(quantityInput => {
  quantityInput.addEventListener('input', event => {
    // get the new item quantity from the changed form
    let newQuantity = event.target.value

    // if the quantity is blank, make the quantity 1
    if (!newQuantity) {
      newQuantity = 1
    }

    // get the cartItemId from the changed form
    let cartItemId = event.target.id
    cartItemId = cartItemId.split('-')[1]

    // build the url with the cartItemId from the changed form
    const url = 'http://localhost:8000/update-cart-item/' + cartItemId

    // instantiate new form data
    const data = new FormData()

    // add the quantity to the FormData
    data.append('quantity', newQuantity)

    axios
      .post(url, data, axiosConfig)
      .then(response => {
        const subtotalDisplay = document.querySelector(
          `#itemsubtotal-${cartItemId}`
        )

        const newSubtotal = response.data.itemSubtotal
        const cartTotal = response.data.cartTotal
        const cartItemCount = response.data.cartItemCount

        subtotalDisplay.innerText = `$${newSubtotal}`
        cartTotalDisplay.innerText = `$${cartTotal}`
        cartItemCountDisplay.innerText = `(${cartItemCount})`
      })
      .catch(error => console.log(error.response))
  })
})
