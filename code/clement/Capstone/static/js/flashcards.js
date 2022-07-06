
// ======== JSONFILE ===============//
const questions = [
    {
        "question": "What is 4*4?",
        "answer": "16"
    },
    {
        "question":"What type of animal was Harambe, who was shot after a child fell into it&#039;s enclosure at the Cincinnati Zoo?",
        "answer":"Gorilla",
    },
    {
        "question": "What is 2+2?",
        "answer": "4"
    },
    {
        "question": "What is 4*5?",
        "answer": "20"
    },
    {
        "question":"What is the defining characteristic of someone who is described as hirsute?","answer":"Hairy",
    },
    {
        "question":"What is the weight of a Gold Bar in Fallout: New Vegas?",
        "answer": "35 Pounds"
    },
    {
        "question": "Which of these is the name of a Japanese system of alternative medicine, literally meaning &quot;finger pressure&quot;?",
        "answer":"Shiatsu",
    }
    
]

const startDiv = document.getElementById("control")
const startButton = document.getElementById('start-btn')
const showAns = document.getElementById('show-ans')
const scoreText = document.getElementById('score')
const nextButton = document.getElementById('next-btn')
const body = document.getElementById('body')
const yes = document.getElementById('yes')
const no = document.getElementById('no')
const nextQtn = document.getElementById('next-question')
const questionContainerElement = document.getElementById('question-container')
const optionContainer = document.getElementById('post-response')
const questionElement = document.getElementById('question')
const answerButtonsElement = document.getElementById('answer-buttons')
let shuffledQuestions, currentQuestionIndex
startButton.addEventListener('click', startGame)
nextButton.addEventListener('click', ()=>{  
})
let score = 10
let scoreWasIncreased = false



// ======== FUNCTIONS FOR THE FLASHCARDS GAME========//
function startGame(){
    console.log('started')
    startButton.classList.add('hide')
    currentQuestionIndex = 0
    score = 0
    scoreText.innerHTML = score
    scoreWasIncreased = false
    shuffledQuestions = questions.sort(()=> Math.random() - .5)
    questionContainerElement.style.display = 'inline'
    nextButton.classList.remove('hide')
    showQuestion()
}

showAns.addEventListener('click', ()=>{
showAns.innerHTML = shuffledQuestions[currentQuestionIndex].answer
optionContainer.style.display = "inline"
})

yes.addEventListener('click', ()=>{
    body.style.backgroundColor = "#00755e"
    nextQtn.style.display = "inline"
    incrementScore()
})
no.addEventListener('click', ()=>{
    body.style.backgroundColor = "#ae2029"
    nextQtn.style.display = "inline"
})


function showQuestion(){
    let question = shuffledQuestions[currentQuestionIndex]
    questionElement.innerText = question.question

    
}
nextQtn.addEventListener('click', resetState)
function resetState(){
    currentQuestionIndex += 1
    // =========================== //
    if (currentQuestionIndex > questions.length - 1){
        nextButton.classList.add('hide')
        startButton.innerText = 'Restart'
        startButton.classList.remove('hide') 

    }else{
        showAns.innerText = "Show Answer"
        optionContainer.style.display = "none"
        nextQtn.style.display = "none"
        scoreWasIncreased = false
        body.style.backgroundColor = "#414a4c" 
        nextButton.classList.remove('hide')
        showQuestion()
    }
    
    // =========================== //
}


function incrementScore(){
    if (!scoreWasIncreased){
        score += 10
        scoreWasIncreased = true
        scoreText.innerHTML = score       
    }
}


