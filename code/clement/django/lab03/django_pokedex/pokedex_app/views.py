from django.shortcuts import render
from .models import PokemonType, Pokemon


# Create your views here.
def index(request):
    pokemons = Pokemon.objects.all()

    # Applying various filters base on my form data
    # And pull values out from the form data

    pokemon_search = request.POST.get('pokemon-search') or ''

    if pokemon_search:
        # Using object to search within the name & types fields for pokemon_search
        pokemons = Pokemon.objects.filter(name__icontains=pokemon_search)

    context = {
        'pokemon_search': pokemon_search,
        'pokemons': pokemons,
    }

    return render(request, 'pokedex/index.html', context)
