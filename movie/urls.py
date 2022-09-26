from django.urls import path

# project directory
from .views import *

urlpatterns=[
    
    path('<str:title>',list_movies,name='ListMovies'),
    path('detail/<int:movieId>',retrieve_movie,name='RetrieveMovie'),
    path('interacted',interacted_movie,name='InteractedMovies')

]