from django.shortcuts import render

from pokedex.models import PokemonType, Pokemon

# Create your views here.



def poke_deck(request):

    context = {
        'poke_ball':Pokemon.objects.all(),
        'pokemon_types': PokemonType.objects.all()
    }

    return render(request, 'pokedex/poke_deck.html', context)