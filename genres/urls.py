from django.urls import path

from .views import *


urlpatterns=[
    
    path('',genres,name='genres'),
    path('<int:genreId>',genere_based_movies,name='genere_based_movies')
    
]