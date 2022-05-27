const form = document.getElementsByTagName('form')[0]
const textInputField = document.querySelector('#text-input')
const submittedTextSpan = document.querySelector('#submitted-text')


form.addEventListener('submit', function (event) {
  // the 'event' parameter will be populated automatically
  // with data about the click event that was triggered
  // event.preventDefault() will cancel the default operations that happen
  // when a form is submitted
  event.preventDefault()

  // assign the value from the input field
  // as the innerText of the span
  submittedTextSpan.innerText = textInputField.value

  // clear the input field
  textInputField.value = ''
})