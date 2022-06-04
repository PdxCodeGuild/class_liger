const BASE_URL = 'http://localhost:8000/api'
const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0]

const axiosConfig = {
  headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': csrfToken.value
  },
  xsrfTokenName: 'X-CSRFToken'
}

const app = new Vue({
  el: '#grocery-list-app',
  delimiters: ['[[', ']]'],
  data: {
    headerText: 'Grocery List',
    groceryItems: [],
    loading: false,
    newItemText: '',
    newItemQuantity: 1
  },

  methods: {
    // delete the item with the given groceryItemId
    deleteGroceryItem: function (groceryItemId) {
      axios
        .delete(
          BASE_URL + `/grocery-items/delete/${groceryItemId}`,
          axiosConfig
        )
        .then(response => {
          // update the array of groceryItems
          this.groceryItems = response.data.groceryItems
        })
        .catch(error => console.log(error.response.data))
    },

    // create a new grocery item
    createGroceryItem: function () {
      axios
        .post(
          BASE_URL + '/grocery-items/create/',
          {
            name: this.newItemText,
            quantity: this.newItemQuantity
          },
          axiosConfig
        )
        .then(response => {
          this.groceryItems = response.data.groceryItems
        })
        .catch(error => console.log(error))
    },

    // update quantity or inCart status of a groceryItem
    updateGroceryItem: function (groceryItem, action) {
      // copy the contents of the groceryItem object
      // to avoid changing the DOM before the API request is made
      const updatedData = { ...groceryItem }

      switch (action) {
        case 'decrement':
          if (updatedData.quantity > 0) {
            updatedData.quantity--
          }
          break
        case 'increment':
          updatedData.quantity++
          break
        case 'toggleInCart':
          updatedData.in_cart = !updatedData.in_cart
          break
      }

      // send the updated data to the API
      axios
        .put(
          BASE_URL + `/grocery-items/update/${groceryItem.id}`,
          {
            ...updatedData
          },
          axiosConfig
        )
        .then(response => {
          this.groceryItems = response.data.groceryItems
        })
        .catch(error => console.log(error.response.data))
    }
  },

  // when the component loads, fetch the grocery list items
  created: function () {
    this.loading = true
    axios
      .get(BASE_URL + '/grocery-items/')
      .then(response => {
        console.log(response.data.groceryItems)
        this.groceryItems = response.data.groceryItems
        this.loading = false
      })
      .catch(error => error.response.data)
  }
})
