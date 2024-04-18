from rest_framework import serializers
from .models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = (
            'nickname',
            'name',
            'surname',
            'origin',
            'date_of_birth'
        )
