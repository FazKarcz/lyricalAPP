from rest_framework import serializers
from .models import Song,Album


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

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = (
            'album_name',
            'artist',
            'genre',
            'release_date',
            'number_of_songs',
            'duration',
        )