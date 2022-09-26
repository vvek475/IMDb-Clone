# rest framework
from rest_framework import serializers

# from directory
from .models import Genres


class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Genres
        fields='__all__'

        
