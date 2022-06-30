from django.db import models
from django.contrib.auth.models import User



#=============== Projects models===============

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=300)
    due_date = models.DateField(null=True)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title


#=============== Resources models===============
class Resource(models.Model):
    name   = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    price  = models.DecimalField(decimal_places=2, max_digits=20)
    url    = models.CharField(max_length=300)
    resources_type = models.CharField(max_length=50)
    date_published = models.DateField(null=True)
    
    # This ManyToManyField will allow many Projects, each user can create many projects.
    projects = models.ManyToManyField(Project, related_name='resources')

    def __str__(self):
        return self.name


#=============== Flash Cards models===============

class FlashCard(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='flashcards')
    question   = models.CharField(max_length=250)
    answer   = models.CharField(max_length=250)

    def __str__(self):
        return self.answer



