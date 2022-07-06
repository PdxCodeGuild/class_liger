
// arlet is use to create a popup notification in the browser
// alert('Hello World')

let units = {
    feet: 0.3048,
    mile: 1609.34,
    meter: 1,
    kilometers: 1000,

}

let distance = document.querySelector("Enter a distance in feet (ft)?\n")

let distance_input = int(distance)

const total = distance_input * units["meter"]

let measurement = document.querySelector("Enter a distance in units; feet, miles meter & kilometer.\n")

const result = units[measurement] * distance

    // alert(result)

