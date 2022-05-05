from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    # define an ImageField for the user's avatar
    avatar = models.ImageField(upload_to='images/avatars/', default='images/avatars/default_avatar.jpg')

    def __str__(self):
        return self.username