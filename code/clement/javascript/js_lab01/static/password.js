var button = document.getElementById('button');
var chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()/><;{}[]";


button.addEventListener('click', function(){
    gentPassword();
})


function gentPassword(){
    var passwordLength = 20;
    var password = "";
    for (var i=0; i<passwordLength; i++){
        var randomNumber = Math.floor(Math.random()*chars.length);
        password += chars.substring(randomNumber, randomNumber+1);
       
    }
    document.getElementById('text-input').value = password;
    
}
