from django.urls import path
from . import views


app_name = 'pokedex'

urlpatterns = [

    path('', views.poke_deck, name='poke_deck'),

] 