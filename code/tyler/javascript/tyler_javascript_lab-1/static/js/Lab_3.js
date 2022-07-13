// Unit Converter
alert(" JS Redo Unit Converter");
let foot = 0.3048
function convert() {
  let distance = prompt("What is the distance in feet?")
  let units = distance*foot
  text = "The distance is " + units + "meters."
  document.getElementById("Units").innerHTML = text
}
