import requests
from django.core.management.base import BaseCommand
from pokedex_app.models import Pokemon, PokemonType
import json


class Command(BaseCommand):

    # You may want to delete all the existing records for Pokemon and PokemonType so each time you run it, you start with a clean slate.

    Pokemon.objects.all().delete()
    PokemonType.objects.all().delete()


    def handle(self, *args, **options):
        # write the code here
        url = "https://raw.githubusercontent.com/PdxCodeGuild/class_liger/main/3%20Django/labs/03%20Pokedex/pokemon.json"
        response = requests.get(url)
        data = response.json()
        pokemons= data['pokemon']

        # loop through the dictionaries and create database objects for each pokemon and their types

        for pokemon in pokemons:

            number = pokemon.get('number')
            name = pokemon.get('name')
            height = pokemon.get('height')
            weight = pokemon.get('weight')
            image_front = pokemon.get('image_front')
            image_back = pokemon.get('image_back')
            types = pokemon.get('types')
            url = pokemon.get('url')


            pokemon = Pokemon.objects.create(
                number = number,
                name = name,
                height = height,
                weight = weight,
                image_front = image_front,
                image_back = image_back,
                urls = url,
            )

            # loop through the list of strings named types. 
            for name in types:
                
                # run the get_or_create method with each type string to get that PokemonType object from the database or create it if it doesn't exist
                pokemontype, created = PokemonType.objects.get_or_create(name=name)

                # still inside the loop, add the PokemonType object to the list of types for the current Pokemon object in the pokemon variable
                print(pokemontype.name, created)
                pokemon.types.add(pokemontype)



                






