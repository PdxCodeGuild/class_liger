from django.db import models

STATUS_CHOICES = [
    ('open', 'Open'),
    ('closed', 'Closed')
]

class Question(models.Model):
    # add a field for the question text
    text = models.CharField(max_length=200)

    # auto_now_add = True will populate this field
    # with the current date/time when a Question object is created in the database
    pub_date = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=6, choices=STATUS_CHOICES, default='open')

    def __str__(self):
        return f"{self.text} - {self.status}"


class Choice(models.Model):
    # ForeignKey(Model, on_delete_option)
    # models.CASCADE means that when a question is deleted,
    # the deletion 'cascades' onto any Choice objects belonging to it
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")

    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    def __str__(self):
        '''The return value from this method will be used 
        when a string representation of a Choice object is needed'''
        return f"{self.question.text} - {self.text}"

