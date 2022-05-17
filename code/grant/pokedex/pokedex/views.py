from django.shortcuts import render

from pokedex.models import PokemonType, Pokemon

from django.db.models import Q

# Create your views here.



def poke_deck(request):

    poke_ball = Pokemon.objects.all()

    form = request.POST

    search = form.get('search') or ''

    if search:
        
        poke_ball = poke_ball.filter(
            Q(name__icontains=search) 
        )

    context = {
        'poke_ball':poke_ball,
        'pokemon_types': PokemonType.objects.all(),
        'form':form,
    }


    # default_per_page = 10
    # default_page_number = 1

    # page_number = request.GET.get('page_number') or default_page_number
    # per_page = request.GET.get('per_page') or default_per_page

    return render(request, 'pokedex/poke_deck.html', context)