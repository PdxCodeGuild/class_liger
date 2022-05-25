from django.db import models
from django.forms import BooleanField, CharField
from users_app.models import CustomUser

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    public = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
