from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = (
            'artist',
            'genre',
            'album',
            'song_name',
            'lyrics',
            'link',
            'release_date',
            'update_date'
        )
