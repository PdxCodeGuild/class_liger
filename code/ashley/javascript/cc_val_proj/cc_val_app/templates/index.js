let ccNumStr = prompt("Please enter credit card number")

// alert("Credit Card Number is" + ccNumStr)

// console.log(ccNumStr)

let ccStrArr = Array.from(ccNumStr)

let ccNumArr = ccStrArr.map(Number)

let checkDigit = ccNumArr.pop()

let ccNumSlice = ccNumArr.slice(0, ccNumArr.length)

let ccNumRev = ccNumSlice.reverse()

// console.log(ccNumRev)

for (let i = 0; i < ccNumRev.length; i++) {
    if (i%2 == 0) {
        ccNumRev[i] = ccNumRev[i]*2
    }
}
// console.log(ccNumRev)

for (let i = 0; i < ccNumRev.length; i++) {
    if (ccNumRev[i] > 9) {
        ccNumRev[i] = ccNumRev[i]-9
    }
}

// console.log(ccNumRev)

let sum = 0

for (let i = 0; i < ccNumRev.length; i++) {
    sum += ccNumRev[i]
}

sum = sum.toString()

if (sum[1] == checkDigit.toString()) {
    console.log('Valid!')
}
else {
    console.log('False!')
}
