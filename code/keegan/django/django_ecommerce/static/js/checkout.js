const checkoutButton = document.querySelector('#checkout-button')

const BASE_URL = 'http://localhost:8000/payments'

/**
 * 
 * @returns Promise which will either resolve with the Stripe publicKey or reject with an error
 */
function fetchStripeConfig () {
  return axios
    .get(BASE_URL + '/config/')
    .then(response => response.data)
    .catch(error => error)
}

checkoutButton.addEventListener('click', () => {
    fetchStripeConfig()
      .then(stripeConfig=>{

        const publicKey = stripeConfig.publicKey
        const stripe = Stripe(publicKey)

        // call Django to create and return a Stripe session id
        axios.get(BASE_URL + '/checkout/')
          .then(response=>{
            const sessionId = response.data.sessionId

            // redirect to the stripe checkout session
            stripe.redirectToCheckout({sessionId: sessionId})
          })
          .catch(error=>console.log(error))
      })
      .catch(error=>console.log(error))
})
