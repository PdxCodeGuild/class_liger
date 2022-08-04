//  Rock paper scissors
alert("JS Redo Rock, Paper, Scissors");

var choices = ["rock", "paper", "scissors"];

function RockPaperScissors() {
  let user_choice = prompt("What is your move? \n rock, paper, or scissors?");
  let opponent_choice = choices[Math.floor(Math.random() * choices.length)];
  if (user_choice === opponent_choice) {
    alert("You tied");
  }
  if (user_choice === "rock" && opponent_choice === "paper") {
    alert("Paper beats Rock. Sorry you lost.");
  }
  if (user_choice === "rock" && opponent_choice === "scissors") {
    alert("Your opponent chose Rock beats scissors. You win!");
  }
  if (user_choice === "paper" && opponent_choice === "scissors") {
    alert("Scissors beats paper. Sorry you lost.");
  }
  if (user_choice === "paper" && opponent_choice === "rock") {
    alert("Paper beats rock. You win!");
  }
  if (user_choice === "scissors" && opponent_choice === "rock") {
    alert("Rock beats scissors. Sorry you lost.");
  }
  if (user_choice === "scissors" && opponent_choice === "paper") {
    alert("Scissors beats paper. You win!");
  }
}
