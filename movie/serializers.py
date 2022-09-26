# rest framework
from rest_framework import serializers

# project directory
from .models import Movies

class ListTMDBMoviesSerializer(serializers.Serializer):
    
    title=serializers.CharField(required=False)
    name=serializers.CharField(required=False)
    overview=serializers.CharField(required=False)
    id=serializers.IntegerField()
    poster_path=serializers.CharField(write_only=True)
    poster=serializers.SerializerMethodField()
    media_type=serializers.CharField(required=False)
    vote_average=serializers.FloatField(required=False)
    release_date=serializers.CharField(required=False)
    first_air_date=serializers.CharField(required=False)
    
    
    def get_poster(self,instance):
        
        poster_path=instance.get('poster_path')
        
        return f'https://image.tmdb.org/t/p/w500{poster_path}'
    

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Movies
        fields = ['movieId','title','poster_path','dateTime','vote_average','id']
        read_only_fields=['id']
        
        
    def create(self, validated_data):
        
        validated_data['user']=self.context.get('request').user
        return super().create(validated_data)