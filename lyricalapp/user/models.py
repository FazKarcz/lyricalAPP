from django.db import models
from song.models import Song, Artist
from django.contrib.auth.models import User


class Favorite(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.song} - {self.user.username}'
