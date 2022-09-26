# from directory
from movie.serializers import MovieSerializer
from movie.models import Movies

def create_movie(data):
    
    user=data.context['request'].user
    movie=data.validated_data['moviesList']
    
    if not len(movie):return False
    
    movie_exists=Movies.objects.filter(movieId=movie[0]['movieId'],user=user)
    
    if movie_exists:
        movie_exists.create_movie_on_abscence()
    
        return movie_exists.first()
    
    movie_serializer=MovieSerializer
    instance=movie_serializer(data=movie[0],context=data.context)
    
    if instance.is_valid(raise_exception=True):
        instance=instance.save()
    
        return instance
