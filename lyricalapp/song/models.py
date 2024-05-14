from django.db import models
from artist.models import Artist
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField


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
    album_cover = models.ImageField(upload_to='album_covers/', null=True, blank=True)

    def __str__(self):
        return self.album_name


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)  # Po ID z tabeli artist
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, default=0)  # Domyślna wartość dla pola genre
    album = models.ForeignKey(Album, on_delete=models.CASCADE, default=0)
    song_name = models.CharField(max_length=50)
    lyrics = models.TextField()
    video_link = EmbedVideoField(null=True)
    release_date = models.DateField()  # Data wydania
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.song_name


class Comment(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.content

