





from django.db import models

IMPORTANCE = [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High')
]

class Priority(models.Model):

    name = models.CharField(max_length=10, choices=IMPORTANCE)

    def __str__(self):
        return self.name
    
# Create your models here.
class Todo(models.Model):

    text = models.CharField(max_length=150)

    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, related_name="Priority")

    created_date =  models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text




