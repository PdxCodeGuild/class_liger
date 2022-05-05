from django.db import models
from django.contrib.auth import get_user_model


class Pic(models.Model):
    # image displayed with the post
    image = models.ImageField(upload_to='images/pics/')

    # associate the Pic with a user
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='pics')

    # caption describing the Pic
    caption = models.CharField(max_length=1000)


    date_created = models.DateTimeField(auto_now_add=True)

    # likes = models.ManyToManyField()

    def __str__(self):
        return self.user.username + ' - ' + self.image.url