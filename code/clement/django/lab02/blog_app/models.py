from django.db import models

from usersystem_app.models import Usersystem


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=200)
    user = models.ForeignKey(Usersystem, on_delete=models.CASCADE, related_name="blogposts")
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    public = models.BooleanField(max_length=200, default=True)

    def __str__(self):
        return self.title














 
   