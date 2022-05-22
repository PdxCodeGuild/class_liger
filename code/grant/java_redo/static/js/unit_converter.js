





let number = document.querySelector('#number')
let metres = document.querySelector('#metres')
let converted_num = document.querySelector('#converted_num')
let convert = document.querySelector('#convert')
// let feet = document.querySelector('#feet')
// let miles = document.querySelector('#miles')
// let kilos = document.querySelector('#kilos')


convert.onclick = function(){

    let metres = .3048

    // console.log(metres)

    let num = number.value

    // console.log(num)

    let converted = num * metres

    // console.log(converted)

    converted_num.innerText = converted + ' metres'

}