# project directory
from movie.serializers import MovieSerializer
from movie.models import Movies


class CreateMovieMixin():
    
    def create_movie(self,data):
        
        movieId=data.get('movieId')
        
        if not movieId:
           
            return
        
        movie=self.movie_exists(data['movieId'])
        
        if movie:
            
            return movie.first()
            
        movie_serializer=MovieSerializer
        movie=movie_serializer(data=data,context={'request':self.request})
        
        if movie.is_valid(raise_exception=True):
            movie=movie.save()
            
            return movie
        
    def movie_exists(self,movieId):
        
        return Movies.objects.filter(movieId=movieId,user=self.request.user)
    
