from django.db import models
from django.contrib.auth.models import User

# project directory
from movie.models import Movies


class Review(models.Model):
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    movie=models.ForeignKey(Movies,on_delete=models.CASCADE,blank=True,null=True)
    review=models.TextField(max_length=500)
    rating=models.IntegerField(default=0)
    dateTime=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        
        return f'{self.user}-{self.movie}'
    

class WatchListQueries(models.QuerySet):
    
    def add_in_movie_abscence(self,instance):
        
        watchlist=self.first()
        existing_movies=watchlist.movies.all()
        
        if instance not in existing_movies:
            watchlist.movies.add(instance)
            return watchlist
        
        return None


class WatchListManager(models.Manager):
    
    def get_queryset(self,*args,**kwargs):
        
        return WatchListQueries(self.model,using=self._db)
    
    def add_in_movie_abscence(self,instance):
        
        return self.get_queryset(self).add_in_movie_abscence(instance)
    
    
class watchList(models.Model):
    
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    movies=models.ManyToManyField(Movies,blank=True)
    
    objects=WatchListManager()

    def __str__(self) -> str:
        
        return self.user
    
    
class Comments(models.Model):
    
    review=models.ForeignKey(Review,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=255)
    
    def __str__(self):
        
        return self.comment