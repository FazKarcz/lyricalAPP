from django.db import models


class Artist(models.Model):
    nickname = models.CharField(max_length=256, unique=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    origin = models.CharField(max_length=20)
    date_of_birth = models.DateField()
