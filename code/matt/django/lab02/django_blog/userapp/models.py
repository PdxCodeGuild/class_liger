from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField


class User(AbstractUser):
    def __str__(self) -> str:
        return self.username
