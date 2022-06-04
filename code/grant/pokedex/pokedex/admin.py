from django.contrib import admin

from .models import PokemonType, Pokemon

# Register your models here.
admin.site.register([Pokemon, PokemonType])