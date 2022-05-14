from user_app.models import CustomUser





from django.db import models

class BlogPost(models.Model):

    title = models.CharField(max_length=50)

    body = models.TextField()

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')

    public = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True)

    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f" {self.title} by {self.user}"

# ---------------------------------------------------------


