from django.urls import path

from . import views

app_name='polls_app'

urlpatterns = [
    path('', views.index, name="index"),
    path('create-question/', views.create_question, name="create_question"),
    path('add-choices/', views.add_choices, name="add_choices"),
    # set up a path with a url parameter
    path('vote/<int:choice_id>', views.vote, name="vote"),
    path('polls/<int:question_id>', views.detail, name='detail'),
    path('polls/edit/<int:question_id>', views.update, name='update'),
    path('polls/delete/<int:question_id>', views.delete, name="delete")
]
