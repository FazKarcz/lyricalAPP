# Generated by Django 4.2.11 on 2024-03-21 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0002_genre_album_song_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='song.genre'),
        ),
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='song.genre'),
        ),
    ]