





let card_number = document.querySelector('#card_number')
let validate = document.querySelector('#validate')
let is_valid = document.querySelector('#is_valid')

validate.onclick = function(){

    // let card_num_array = []

    let card_num = card_number.value

    console.log(typeof card_num)

    let card_num_array = Array.from(card_num)

    console.log(typeof card_num_array)

    let check = card_num_array.pop()

    console.log(check)

    console.log(typeof card_num_array)

    card_num_array.reverse()

    console.log(typeof card_num_array)

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
    
    console.log(typeof card_num_array)
    
    
    
    sum_num = card_num_array.reduce((a, n)=> (a + parseInt(n)), 0) 
        // I dont understand how this works //
    console.log(sum_num)
    console.log(typeof sun_num)

    // for(i = 0; i < sum_num.length; i++){
    //     console.log(sum_num[i])
    // }

    let sum = Array.from(sum_num)

    console.log(sum)
    console.log(typeof sum)

    // total = sum[1]

    // console.log(typeof total)
    // console.log(total)

    // if(total === check){


    // }
    // console.log(check)
    // console.log(sum[1])
    // console.log(total === check)
    
    // for(i = 0; i < card_num_array.length; i++){
        
    //     sum += card_num_array[i]
    //     // sum = num + num
    //     console.log(sum)
    //     // console.log(sum)

        
    // }
    

   
}



// Sum all values.
// Take the second digit of that sum.
// If that matches the check digit, the whole card number is valid.
// For example, the worked out steps would be:

// 1. 4556737586899855
// 2. 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
// 3. 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
// 4. 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
// 5. 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
// 6. 85
// 7. 5
