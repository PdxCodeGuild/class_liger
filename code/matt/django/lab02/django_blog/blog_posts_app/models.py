from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField

# Create your models here.


class BlogPosts(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=200)
    user = models.ForeignKey(
        get_user_model(), on_delete=CASCADE, related_name="blogposts"
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
