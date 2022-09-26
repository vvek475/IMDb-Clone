from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


class MoviesQueries(models.QuerySet):
    
    def create_movie_on_abscence(self):
        
        if len(self):
            
            movie=self.first()
            movie.dateTime=datetime.datetime.now(tz=timezone.utc)
            movie.save()
            
            return True 
        
        return

class MoviesManager(models.Manager):
    
    def get_queryset(self,*args,**kwargs):
        
        return MoviesQueries(self.model,using=self._db)
    
    def create_movie_on_abscence(self):
        
        return self.get_queryset(self).create_movie_on_abscence()
    
class Movies(models.Model):
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    movieId=models.IntegerField()
    poster_path=models.CharField(max_length=255)
    vote_average=models.FloatField()
    dateTime=models.DateTimeField(auto_now_add=True)
    
    @property
    def get_poster(self):
        
        return f'https://image.tmdb.org/t/p/w500{self.poster_path}'

    objects=MoviesManager()
    
    def __str__(self):
        
        return f'{self.id}'