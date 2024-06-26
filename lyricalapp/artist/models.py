from django.db import models


class Artist(models.Model):
    nickname = models.CharField(max_length=50)
    origin = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    artist_poster = models.ImageField(upload_to='artist_posters/', null=True, blank=True)

    def __str__(self):
        return self.nickname
