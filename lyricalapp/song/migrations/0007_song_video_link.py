# Generated by Django 4.2.7 on 2024-04-11 13:40

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='video_link',
            field=embed_video.fields.EmbedVideoField(null=True),
        ),
    ]
