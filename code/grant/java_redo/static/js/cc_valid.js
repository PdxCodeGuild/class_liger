





let card_number = document.querySelector('#card_number')
let validate = document.querySelector('#validate')
let is_valid = document.querySelector('#is_valid')

validate.onclick = function(){

    let card_num = card_number.value

    // console.log(typeof card_num)

    let card_num_array = Array.from(card_num)

    // console.log(typeof card_num_array)

    let check = card_num_array.pop()

    // console.log(check)

    // console.log(typeof card_num_array)

    card_num_array.reverse()

    // console.log(typeof card_num_array)

    for(let i = 0; i <= card_num_array.length; i++){

        if(i % 2 === 0){

            // console.log(card_num_array[i])

            card_num_array[i] = card_num_array[i] *2

            // console.log(i)

            // console.log(card_num_array)
            
        }

    }    

    console.log(typeof card_num_array)

    for(let i = 0; i <= card_num_array.length; i++){
        
        if(card_num_array[i] > 9){
            
            card_num_array[i] = card_num_array[i] - 9
        }
        
    }
    
    // console.log(typeof card_num_array)    
    
    sum_num = card_num_array.reduce((a, n)=> (a + parseInt(n)), 0) 
    // ^^^    I dont understand how this works completely    ^^^ //
    let last_num = sum_num.toString()

    // console.log(last_num)

    let last = last_num.charAt(last_num.length -1)

    // console.log(last)

    if(last === check){

        // console.log(check)

        is_valid.innerText = 'Card Number: ' + card_num + ' is Valid. '

        // console.log(is_valid.innerText)

    } else {

        is_valid.innerText = 'Card Number: ' + card_num + ' is NOT Valid. '

        // console.log(is_valid.innerText)

    }
}