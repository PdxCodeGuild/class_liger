from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    # define an ImageField for the user's avatar
    avatar = models.ImageField(upload_to='images/avatars/', default='images/avatars/default_avatar.jpg')

    # 'self' - relates this model to itself
    # blank=True - allow a user to have 0 followers
    # related_name='following' - allow access to the list of users that a particular user is following
    # symmetrical=False - User A can follow User B without User B following User A
    followers = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='following')

    def __str__(self):
        return self.username