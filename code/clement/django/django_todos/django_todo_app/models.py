from telnetlib import STATUS
from venv import create
from django.db import models

PRIORITY_CHOICES= [
    ('high', 'High'),
    ('medium', 'Medium'), 
    ('low', 'Low')
]

class Priority(models.Model):

    text = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='low')

# Create your models here.
class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, related_name="TodoItem")

 
    def __str__(self):
        return self.text
