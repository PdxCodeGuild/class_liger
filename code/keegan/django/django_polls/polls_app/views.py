from django.shortcuts import render

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
    choice_count = form.get('choice-count')

    # create the new question in the database
    new_question = Question()

    # set the question text
    new_question.text = question_text

    # save the object to the database
    new_question.save()

    # shorthand version to create a database object
    # new_question = Question.objects.create(
    #     text=question_text
    # )



    questions = Question.objects.all()

    context = {
        'questions': questions
    }
    return render(request, 'polls/index.html', context)





def add_choices(request):

    context = {
        "choice_count": [0,1,2]
    }

    return render(request, 'polls/add-choices.html', context)