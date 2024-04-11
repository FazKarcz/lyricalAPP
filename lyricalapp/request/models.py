from django.db import models


class Request(models.Model):
    author = models.CharField(max_length=25)
    song_name = models.CharField(max_length=35)
    date = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.song_name + " - " + self.author

