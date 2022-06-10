from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogposts')
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)

class Comment(models.Model):
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=500)
    email = models.EmailField(max_length=100)
    body = models.CharField(max_length=1000)