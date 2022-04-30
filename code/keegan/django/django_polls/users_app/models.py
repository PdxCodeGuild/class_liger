from django.db import models

# import the AbstractUser model from which our User model will inherit
from django.contrib.auth.models import AbstractUser

# Define a custom User model off of the AbstractUser model
class User(AbstractUser):

    # add additional user fields here...

    def __str__(self):
        return self.username