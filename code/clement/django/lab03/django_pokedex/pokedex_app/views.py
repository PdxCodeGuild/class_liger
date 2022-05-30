from django.shortcuts import render
from .models import PokemonType, Pokemon
from django.db.models import Q



# Create your views here.
def index (request):
    pokemons = Pokemon.objects.all()

    # Applying various filters base on my form data
    # And pull values out from the form data
   
    pokemon_search =request.POST.get('pokemon-search') or [pokemon.types for pokemon in Pokemon.objects.all()]
    pokemons =request.POST.getlist('pokemons') or ''


    if pokemon_search:
        # Using Q object to search within the title & discription fields for pokemon_search
        pokemons = pokemons.filter(
            Q(title__icontains=pokemon_search) | Q(discription__icontains=pokemon_search)
            )

    pokemons=Pokemon.objects.filter(types__name__in=PokemonType)

    pokemon_search_option = {
        'pokemons': [pokemon.types for pokemon in Pokemon.objects.all()],
        'search_by_option': [
            {'label': 'name(A-Z)', 'value':'type'},
            {'label': 'name(A-G)', 'value':'type'},
            {'label': 'name(H-N)', 'value':'type'},
            {'label': 'name(O-T)', 'value':'type'},
            {'label': 'name(U-Z)', 'value':'type'},
            {'label': 'name(Z-A)', 'value':'-type'},

        ]
    }
   
    pokemon_search = {
        'pokemons': [pokemon.types for pokemon in Pokemon.objects.all()]
    }

    form_data = {
       'pokemon_search':pokemon_search, 
       'pokemons': pokemons,
       'pokemon_search_option': pokemon_search_option
    }


    context = {
        'pokemon_search':pokemon_search,
        'pokemons':pokemons,
        'form_data':form_data,
        'pokemon_search_option': pokemon_search_option,
    }


    return render(request, 'pokedex/index.html', context)



