let ascii = []

for (let i = 32; i < 127; i++) {
    ascii.push(String.fromCharCode(i))
}

// console.log(ascii)

// console.log(randIndex, ascii[randIndex])

let i = 0

const password = []

while (i < 10) {
    let randIndex = Math.floor(Math.random() * ascii.length)
    // console.log(randIndex)
    i++
    password.push(ascii[randIndex])
    // console.log(password)
}

const password_string = password.join('')

console.log(password_string)
