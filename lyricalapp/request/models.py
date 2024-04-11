from django.db import models
from django.contrib.auth.models import User

class Request(models.Model):

    PENDING = 'Nie rozpatrzony'
    ACCEPTED = 'Przyjęty'
    DECLINED = 'Odrzucony'
    STATUS_CHOICES = [
        (PENDING, 'Nie rozpatrzony'),
        (ACCEPTED, 'Przyjęty'),
        (DECLINED, "Odrzucony")
    ]
    author = models.CharField(max_length=25)
    song_name = models.CharField(max_length=35)
    date = models.DateField(auto_now=True)
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default=PENDING,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-status']

    def __str__(self):
        return self.song_name + " - " + self.author + " - " + self.status
