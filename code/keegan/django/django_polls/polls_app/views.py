from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Question, Choice

def index(request):
    # get all the questions from the database
    # through the Question model's 'objects' manager
    questions = Question.objects.all()

    context = {
        'questions': questions
    }

    return render(request, 'polls/index.html', context)


# When the new question form is submitted,
# call this view to create a Question object
# and redirect to the add_choices page 
# to populate the choices for the Question
def create_question(request):

    # the form data is available through the request object
    form = request.POST

    # grab the values from the form
    question_text = form.get('question-text')
    choice_count = int(form.get('choice-count'))

    # # create the new question in the database
    # new_question = Question()

    # # set the question text
    # new_question.text = question_text

    # # save the object to the database
    # new_question.save()

    # shorthand version to create a database object
    # .create() saves automatically so .save() isn't required
    new_question = Question.objects.create(
        text=question_text
    )

    context = {
        'question': new_question,
        'choice_count': [number for number in range(1, choice_count + 1)]
    }

    return render(request, 'polls/add-choices.html', context)




def add_choices(request):

    form = request.POST

    # use the question id to retrieve the 
    # question with that id from the database
    
    # Pull the question_id out of the form data
    question_id = form.get('question-id')
    # find the Question object in the database with the question_id
    question = Question.objects.get(id=question_id)


    # loop through all the choices in the form
    for key in form:
        if key.startswith('choice'):
            # get the choice text for the specific choice form field
            choice_text = form.get(key)

            # create a Choice object in the database
            # associate the Choice object with the question
            Choice.objects.create(text=choice_text, question=question)


    # redirect to the index url for the polls_app
    # to reuse the logic from the index() view
    return redirect(reverse('polls_app:index'))

# choice_id will come from the link that is clicked to vote for the choice
def vote(request, choice_id):
    # get the choice from the database using the choice_id from the url parameter
    choice = Choice.objects.get(id=choice_id)

    # increment the vote count for the clicked vote
    choice.votes += 1

    # save the changes
    choice.save()

    # redirect to the index url for the polls_app
    # to reuse the logic from the index() view
    return redirect(reverse('polls_app:index'))