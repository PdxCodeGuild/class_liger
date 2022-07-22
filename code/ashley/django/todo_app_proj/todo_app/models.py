from django.db import models
from django.forms import CharField

PRIORITY_CHOICES = [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High')
]

# Create your models here.
class Priority(models.Model):
    # name = models.CharField(max_length=10, null=True)

    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Low')


class TodoItem(models.Model):
    text = models.CharField(max_length=100, null=True)
    
    pub_date = models.DateField(auto_now_add=True)

    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)



