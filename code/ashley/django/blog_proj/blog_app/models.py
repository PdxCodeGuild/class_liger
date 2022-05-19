from django.db import models
from users_app.models import User

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField
    date_created = models.DateTimeField(auto_now_add=True)
    date_created = models.DateField(auto_now=True)
