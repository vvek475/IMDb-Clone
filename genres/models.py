from django.db import models

# Create your models here.
class Genres(models.Model):
    
    title=models.CharField(max_length=25)
    genreId=models.IntegerField()
    
    def __str__(self) -> str:
        return self.title