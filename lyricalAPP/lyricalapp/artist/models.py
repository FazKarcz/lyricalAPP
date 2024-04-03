<<<<<<< Updated upstream:lyricalAPP/lyricalapp/artist/models.py
from django.db import models


class Artist(models.Model):
    nickname = models.CharField(max_length=256, unique=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    origin = models.CharField(max_length=20)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name + ' ' + self.surname
=======
from django.db import models


class Artist(models.Model):
    nickname = models.CharField(max_length=256, unique=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    origin = models.CharField(max_length=20)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name + ' ' + self.surname
>>>>>>> Stashed changes:lyricalapp/artist/models.py
