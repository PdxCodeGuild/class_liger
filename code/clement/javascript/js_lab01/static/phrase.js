const form = document.getElementById('form')
const numberInput = document.getElementById('numberInput')
const phraseResult = document.getElementById('phraseResult')

const ones = {
    0:"zero",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen",
    
}

const prefixesValue = {
    2:"twenty",
    3:"thirty",
    4:"fourty",
    5:"fifty",
    6:"sixty",
    7:"seventy",
    8:"eighty",
    9:"ninety",
}

form.addEventListener('submit', function(event){
    event.preventDefault()

    if(+numberInput.value in ones){

        phraseResult.innerHTML=ones[ numberInput.value]

    }

    let arrayNumber = numberInput.value.split("")
    if(arrayNumber.length === 2  && +numberInput.value > 19){
        phraseResult.innerHTML = prefixesValue[arrayNumber[0]]

    }
    if(arrayNumber.length === 2 && numberInput.value % 10 !==0 && +numberInput.value > 19){
        phraseResult.innerHTML = prefixesValue[arrayNumber[0]]
         + " " + ones[arrayNumber[1]]

    }
   

    if(arrayNumber.length === 3){
        if(+arrayNumber[1] === 0 && numberInput.value % 100 !==0 ){
            phraseResult.innerHTML = ones[arrayNumber[0]]
             + ' hundred ' + " " + ones[arrayNumber[2]]
        }
        else if(+arrayNumber[1] === 0 && numberInput.value % 100 ===0 ){
            phraseResult.innerHTML = ones[arrayNumber[0]]
             + ' hundred '
        }
        
        else if(+arrayNumber[1] < 2){
            phraseResult.innerHTML = ones[arrayNumber[0]] + ' hundred ' + " "  + ones[+([arrayNumber[1],arrayNumber[2]]).join("")];

        }

        else{
            phraseResult.innerHTML = ones[arrayNumber[0]] + ' hundred ' + prefixesValue[arrayNumber[1]] + " " + ones[arrayNumber[2]]
    
        }
    }

    if(arrayNumber.length === 4){
        if(+arrayNumber[1] === 0 && numberInput.value % 1000 ===0){
            phraseResult.innerHTML = ' thousand ' + " "
        }
        else if(+arrayNumber[1] < 2){
            phraseResult.innerHTML = ' thousand ' + ones[arrayNumber[1]]
              + ' hundred ' + " "  + ones[+([arrayNumber[2],arrayNumber[3]]).join("")];

        }

        else{
            phraseResult.innerHTML = ones[arrayNumber[0]]
             + ' thousand ' +  ones[arrayNumber[1]]  + ' hundred ' + prefixesValue[arrayNumber[2]] + " " + ones[arrayNumber[3]]
    
        }
    }

    if(arrayNumber.length === 5 && numberInput.value % 10000 ===0){
        if(+arrayNumber[1] === 0){
            phraseResult.innerHTML = ' ten thousand '
        }
       
    }

   
})