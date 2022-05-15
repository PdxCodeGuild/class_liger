from django.db import models
from django.forms import CharField

# Create your models here.



class PokemonType(models.Model):

    name = models.CharField(max_length=70)

    def __self__(self) -> str:

        return f' {self.name.capitalize} Type Pokemon'

# -----------------------------------------------------------


class Pokemon(models.Model):

    name = models.CharField(max_length=70)

    number = models.IntegerField()

    height = models.FloatField()

    weight = models.FloatField()

    image_front = models.CharField(max_length=70)

    image_back = models.CharField(max_length=70)

    types = models.ManyToManyField(PokemonType, related_name='type')

    def __self__(self) -> str:

        return f'{self.name.capitalize}'
    class Meta:
        verbose_name_plural = 'Pokemon'