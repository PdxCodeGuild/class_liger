





let number = document.querySelector('#number')
// let feet = document.querySelector('#feet')
// let miles = document.querySelector('#miles')
let metres = document.querySelector('#metres')
// let kilos = document.querySelector('#kilos')
let converted_num = document.querySelector('#converted_num')
let convert = document.querySelector('#convert')


convert.onclick = function(){

    let metres = .3048

    console.log(metres)

    let num = number.value

    console.log(num)

    let converted = num * metres

    console.log(converted)

    converted_num.innerText = converted + ' metres'



}