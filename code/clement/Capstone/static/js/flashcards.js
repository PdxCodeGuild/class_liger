
// ======== JSONFILE ===============//
const questions = [
    {
        "question": "What is 4*4?",
        "answer": "16"
    },
    {
        "question": "What is 2+2?",
        "answer": "4"
    },
    {
        "question": "What is 4*5?",
        "answer": "20"
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
    cleanUp()
    questionContainerElement.style.display = 'inline'
    showAns.addEventListener('click', ()=>{
        showAnswer(currentQuestionIndex)
    })
    showQuestion()
}

function cleanUp() {
    shuffledQuestions = questions.sort(()=> Math.random() - .5)
}


function showQuestion(){
    let question = shuffledQuestions[currentQuestionIndex]
    questionElement.innerText = question.question

    yes.addEventListener('click', ()=>{
        body.style.backgroundColor = "#00ff7f"
        displayNext()
    })
    no.addEventListener('click', ()=>{
        body.style.backgroundColor = "#d40000"
        displayNext()
    })
}
nextQtn.addEventListener('click', ()=> {
    currentQuestionIndex++
    resetState()
})

function displayNext() {
    nextQtn.style.display = "inline"
    
} 

function resetState(){
    // =========================== //
    if (currentQuestionIndex > questions.length - 1){
        nextButton.classList.remove('hide')

    }else{
        startButton.innerText = 'Restart'
        startButton.classList.remove('hide')
    }
    
    // =========================== //
    showAns.innerText = "Show Answer"
    optionContainer.style.display = "none"
    nextQtn.style.display = "none"
    scoreWasIncreased = false
    showQuestion()
    body.style.backgroundColor = "#ff8f00" 
}

function showAnswer() { 
    console.log(currentQuestionIndex)
    showAns.innerHTML = shuffledQuestions[currentQuestionIndex].answer
    optionContainer.style.display = "inline"
}

function incrementScore(){
    if (!scoreWasIncreased){
        score += 10
        scoreWasIncreased = true
        scoreText.innerHTML = score
        
        
    }
}


