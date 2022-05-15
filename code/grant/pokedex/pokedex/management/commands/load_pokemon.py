import requests

from django.core.management.base import BaseCommand

from pokedex.models import Pokemon, PokemonType

import json
class Command(BaseCommand):

    def handle(self, *args, **options):

        Pokemon.objects.all().delete()

        PokemonType.objects.all().delete()

        f = open('pokemon.json')

        poke_balls = json.load(f)

        for pokemon in poke_balls['pokemon']:
        
            name = pokemon['name']
            number = int(pokemon['number'])
            height = float(pokemon['height'])
            weight = float(pokemon['weight'])
            image_front = pokemon['image_front']
            image_back = pokemon['image_back']

            
            for o in pokemon['types']:

                types = o

                print(types)
        
            pokemon = Pokemon.objects.create(

                number = number,
                name = name,
                height = height,
                weight = weight,
                image_front = image_front,
                image_back = image_back,
            
            )

            pokemon_type, created = PokemonType.objects.get_or_create(name=types)

            pokemon.types.add(pokemon_type)

            print(pokemon_type)

            f.close()




# ----------------------------------------------------






