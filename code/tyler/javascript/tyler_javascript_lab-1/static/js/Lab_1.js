alert("Password generator")

console.log("Hello Javascript World!");


function generate_password() {
  let characters =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  let Password = "";
  let length = prompt("How long will your password be? (Please use integers)");
  for (let i = 0; i < length; i++) {
    Password += characters.charAt(
      Math.floor(Math.random() * characters.length)
    );
  }
    text = "Your password is: " + "(" + Password + ")";
  document.getElementById("password").innerHTML = text
}
