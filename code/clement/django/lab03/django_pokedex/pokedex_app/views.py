from django.shortcuts import render
from .models import PokemonType, Pokemon
from django.db.models import Q


# Create your views here.
def index(request):
    pokemons = Pokemon.objects.all()

    # Applying various filters base on my form data
    # And pull values out from the form data

    pokemon_search = request.POST.get('pokemon-search') or ''

    if pokemon_search:
        # Using Q object to search within the name & types fields for pokemon_search
        pokemons = Pokemon.objects.filter(
            Q(name__icontains=pokemon_search) | Q(
                types__name__icontains=pokemon_search)
        )

    pokemon_options = {
        'pokemons': [pokemon.types for pokemon in Pokemon.objects.all()],
        'search_by_option': [
            {'label': 'name(A-Z)', 'value': 'name'},
            {'label': 'type(A-Z)', 'value': 'type'},

        ]
    }

    form_data = {
        'pokemon_search': pokemon_search,
        'pokemon_option': pokemon_options,

    }

    context = {
        'pokemon_search': pokemon_search,
        'pokemons': pokemons,
        'form_data': form_data,
        'pokemon_option': pokemon_options,

    }

    return render(request, 'pokedex/index.html', context)
