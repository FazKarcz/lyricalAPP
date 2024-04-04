from django.db import models


class Artist(models.Model):
    nickname = models.CharField(max_length=256, unique=True)
    origin = models.CharField(max_length=20)

    def __str__(self):
        return self.nickname
