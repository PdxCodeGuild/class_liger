const input= document.querySelector('input');
const Button= document.querySelector('.addTodo > button');

Button.addEventListener('click', addTodo);
input.addEventListener('keyup', (event)=>{
    (event.target === 13 ? addTodo(event): null)
})
function addTodo(event){
    const unCompleted = document.querySelector('.unCompleted');
    const Completed = document.querySelector('.Completed');


    const newTodo = document.createElement('li'); 
    const checkTodo = document.createElement('button');
    const delTodo = document.createElement('button');
    
    checkTodo.innerHTML ='<i class="bi bi-check2-circle"></i>'
    delTodo.innerHTML ='<i class="bi bi-trash3-fill"></i>'
    
    if(input.value !== ''){
        newTodo.textContent=input.value;
        input.value='';
        unCompleted.appendChild(newTodo); 
        newTodo.appendChild(checkTodo);
        newTodo.appendChild(delTodo);

    }
    checkTodo.addEventListener('click', function(){
        const paragraph = this.parentNode;
        paragraph.remove();
        Completed.appendChild(paragraph);
        checkTodo.style.display = 'none';

    })
    delTodo.addEventListener('click', function(){
        const paragraph = this.parentNode;
        paragraph.remove();
       

    })
}