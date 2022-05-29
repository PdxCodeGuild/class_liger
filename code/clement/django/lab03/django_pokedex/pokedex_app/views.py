from django.shortcuts import render
from .models import PokemonType, Pokemon
from django.db.models import Q



# Create your views here.
def index (request):
    pokemons = Pokemon.objects.all()

    # Applying various filters base on my form data
    # And pull values out from the form data
    if request.POST:
        pokemon_search =request.POST.get('pokemon-search') or [pokemon.types for pokemon in Pokemon.objects.all()]
        pokemons =request.POST.getlist('pokemons') or ''


        if pokemon_search:
            # Using Q object to search within the title & discription fields for pokemon_search
            pokemons = pokemons.filter(
                Q(title_icontains=pokemon_search) | Q(discription_icontains=pokemon_search)
                )


    pokemons=pokemons.filter(name_type_in=pokemons)

   
    pokemon_search = {
        'pokemons': [pokemon.types for pokemon in Pokemon.objects.all()]
    }

    form_data = {
       ' pokemon_search':pokemon_search, 
       ' pokemons': pokemons
    }


    context = {
        'pokemon_search':pokemon_search,
        'pokemons':pokemons,
        'form_data':form_data,
    }


    return render(request, 'poked_app/base.html', context)



