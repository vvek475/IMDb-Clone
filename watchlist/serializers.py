# rest framework
from rest_framework import serializers

# project directory
from movie.serializers import MovieSerializer
from .models import *

class ListWatchListSerializers(serializers.ModelSerializer):
    
    user=serializers.CharField(source='user.username',read_only=True)
    movie=MovieSerializer(source='movies.all',many=True,read_only=True)
    movies=MovieSerializer(write_only=True)
    
    class Meta:
        
        model = watchList
        fields=['movie','user','movies']
        read_only_fields=['user']
        
    def create(self,validated_data):
        
        validated_data['user']=self.context.get('request').user
        
        return super().create(validated_data)
    

class EditWatchlistSerializer(serializers.ModelSerializer):
    
    movieId=serializers.IntegerField(write_only=True)
    
    class Meta:
        model=watchList
        fields=['movieId']
        
    
class ReviewSerializer(serializers.ModelSerializer):
    
    replies=serializers.IntegerField(source='comments_set.all.count',read_only=True)
    movie_data=MovieSerializer(write_only=True)
    reviewed_user=serializers.CharField(source='user.username',read_only=True)
    
    class Meta:
        
        model=Review
        fields=['review','movie','rating','id','reviewed_user','replies','movie_data']
        read_only_fields=['dateTime','id']
        
    def create(self,validated_data):
        
        validated_data.pop('movie_data')
        validated_data['user']=self.context.get('request').user
        
        return super().create(validated_data)
        
        
class CommentSerializer(serializers.ModelSerializer):
    
    user_field=serializers.CharField(source='user.username',read_only=True)
    
    class Meta:
        
        model=Comments
        fields=['review','user','comment','user_field']