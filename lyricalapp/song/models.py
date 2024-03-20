from django.db import models
from artist.models import Artist


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)  # Po ID z tabeli artist
    song_name = models.CharField(max_length=20)
    lyrics = models.TextField()
    link = models.CharField(max_length=255,default = None)
    release_date = models.DateField()  # Data wydania
    update_date = models.DateField()
