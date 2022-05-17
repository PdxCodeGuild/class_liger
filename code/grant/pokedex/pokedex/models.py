from django.db import models

# Create your models here.



class PokemonType(models.Model):

    name = models.CharField(max_length=70)

    # def __self__(self):

        # return f'{self.name.capitalize()} Type Pokemon'

    def __str__(self):

        return f'{self.name.capitalize()}'

# -----------------------------------------------------------


class Pokemon(models.Model):

    name = models.CharField(max_length=70)

    number = models.IntegerField()

    height = models.FloatField()

    weight = models.FloatField()

    image_front = models.CharField(max_length=70)

    image_back = models.CharField(max_length=70)

    types = models.ManyToManyField(PokemonType, related_name='type')

    def __str__(self):

        return f'{self.name.capitalize()}'

    def __self__(self):

        return f'{self.name.capitalize()}'
    class Meta:
        verbose_name_plural = 'Pokemon'


# class Url(models.Model):

    

#     def __str__(self):

#         return f'audio/{{pokemon.name}}-cry.mp3'