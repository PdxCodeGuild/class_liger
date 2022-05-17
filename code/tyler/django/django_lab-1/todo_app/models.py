from tkinter import CASCADE
from django.db import models
from django.forms import CharField

priority_options = {
    ('high', 'High'),
    ('medium', 'Medium'),
    ('low', 'Low')
}

# Create your models here.


class Priority(models.Model):
    name = models.CharField(max_length=6, choices=priority_options)

    def __str__(self):
        return self.name


class TodoItem(models.Model):
    text = models.CharField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    def __str__(self):
        return self.text
