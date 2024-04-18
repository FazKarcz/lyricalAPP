# Generated by Django 4.2.7 on 2024-04-11 13:41

from django.db import migrations
from django.db.migrations import RunPython


def copy_links(apps, schema_editor):
    Song = apps.get_model('song', 'Song')
    for song in Song.objects.all():
        song.video_link = song.link
        song.save()

class Migration(migrations.Migration):

    dependencies = [
        ('song', '0007_song_video_link'),
    ]

    operations = [
        RunPython(copy_links),
    ]
