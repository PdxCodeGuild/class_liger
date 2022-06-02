from django.db import models

# Create your models here.
# Create an app pokedex and add two models to store our pokemon, Pokemon and PokemonType.


class PokemonType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    height = models.FloatField(default=0.0)
    weight = models.FloatField(default=0.0)
    image_front = models.CharField(max_length=300)
    image_back = models.CharField(max_length=300)
    urls = models.CharField(max_length=300)

    types = models.ManyToManyField(PokemonType, related_name='pokemons')

    def __str__(self):
        return self.name
