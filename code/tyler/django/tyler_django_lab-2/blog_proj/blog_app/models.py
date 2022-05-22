from django.db import models
from django.forms import CharField

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length= 30)
    body = models.TextField