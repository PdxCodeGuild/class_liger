from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField


# Create your models here.

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project')
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=300)
    due_date = models.DateField(null=True)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Resource(models.Model):
    name   = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    price  = models.DecimalField(decimal_places=2, max_digits=20)
    url    = models.CharField(max_length=300)
    resources_type = models.CharField(max_length=50)
    date_published = models.DateField(null=True)
    
    # This ManyToManyField will allow many Projects, each user can create many projects.
    subjects = models.ManyToManyField(Project, related_name='resource')

    def __str__(self):
        return self.name



