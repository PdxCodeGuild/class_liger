from django.db import models

from django.contrib.auth.models import AbstractUser
from django.forms import EmailField



class CustomUser(AbstractUser):
    
    username = models.CharField(max_length=23, unique = True)

    USERNAME_FIELD = 'username'

    email = models.EmailField()

    EMAIL_FIELD = 'email'

    def __str__(self):

        return self.username