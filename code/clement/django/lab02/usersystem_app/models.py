from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class Usersystem (AbstractUser):
    
    
    def __str__(self):
        return self.username
