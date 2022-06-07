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
    loading: false
  },

  methods: {
    deleteGroceryItem: function (groceryItemId) {
      axios.delete(
        BASE_URL + `/grocery-items/delete/${groceryItemId}`,
        axiosConfig
      )
      .then(response=>{

        // update the array of groceryItems
        this.groceryItems = response.data.groceryItems

      })
      .catch(error=>console.log(error.response.data))
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
