# Generated by Django 4.2.11 on 2024-05-30 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0010_album_album_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
