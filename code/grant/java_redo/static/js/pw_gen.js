





let len_pw = document.querySelector('#len_pw')
let gen = document.querySelector('#gen')
let new_ps = document.querySelector('#new_ps')

const choices = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',+'1','2','3','4','5','6','7','8','9','0','!','@','#','%','^','&','*'] 

gen.onclick = function(){

    let len = len_pw.value;    

    let password = ''
    
    for(let i = len; i > 0; i--){
        
        let char = Math.floor(Math.random() * choices.length )
        
        // console.log(i)
        // console.log(char)
        
        password = password.concat(choices[char])
        
        new_ps.innerText = 'Password: ' + password
        
    }
}