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
        
            name = pokemon.get('name')
            number = int(pokemon.get('number'))
            height = float(pokemon.get('height'))
            weight = float(pokemon.get('weight'))
            image_front = pokemon.get('image_front')
            image_back = pokemon.get('image_back')

            pokemon_obj = Pokemon.objects.create(

                number = number,
                name = name,
                height = height,
                weight = weight,
                image_front = image_front,
                image_back = image_back,

            
            )
            
            for p_types in pokemon['types']:

                # types = p_types

                pokemon_type, created = PokemonType.objects.get_or_create(name=p_types)

                pokemon_obj.types.add(pokemon_type)



                print(pokemon_obj)
                print(pokemon_obj.name)
                print(pokemon_obj.types)
                print(pokemon_obj.types.name)

                print(pokemon_type)
                print(pokemon_type.name)
                print(pokemon_type.type)
                print(pokemon_type.type.name)



            f.close()




# ----------------------------------------------------






