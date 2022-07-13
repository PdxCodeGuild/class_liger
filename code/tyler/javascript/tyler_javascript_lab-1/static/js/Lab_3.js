// ROT 13
alert(" JS Redo ROT13")
function rot13() {
    let encrypted_message = ''
    let user_message = prompt(" What message are you encrypting?")
    let encrypt_strength = prompt(" How strong is the encryption? (Please use an integer)")
    console.log(user_message, encrypt_strength)
}