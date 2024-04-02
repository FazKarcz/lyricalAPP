from django.db import models
from artist.models import Artist


class Genre(models.Model):
    name = models.CharField(max_length=255, default='Brak')

    def __str__(self):
        return self.name


class Album(models.Model):
    album_name = models.CharField(max_length=255)
    number_of_songs = models.IntegerField()
    duration = models.FloatField()
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)  # Po ID z tabeli artist
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, default=0)  # Domyślna wartość dla pola genre

    def __str__(self):
        return self.album_name


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)  # Po ID z tabeli artist
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, default=0)  # Domyślna wartość dla pola genre
    album = models.ForeignKey(Album, on_delete=models.CASCADE, default=0)
    song_name = models.CharField(max_length=20)
    lyrics = models.TextField()
    link = models.CharField(max_length=255, default=None)
    release_date = models.DateField()  # Data wydania
    update_date = models.DateField()

    def __str__(self):
        return self.song_name