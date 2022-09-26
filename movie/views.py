# rest framework
from rest_framework import generics,permissions,mixins,viewsets,views
from rest_framework.response import Response

# project directory
from .mixins import UserAndAnonThrottleRateMixin
from .models import Movies
from .pagination import PageNumberPagination
from .serializers import MovieSerializer
from .throttling import UserRateThrottle
from watchlist.serializers import ReviewSerializer
from watchlist.models import Review

from utility import api_helper as APIHelper


class ListMovies(UserAndAnonThrottleRateMixin,views.APIView):
    
    permission_classes=[permissions.AllowAny]
    
    def get(self,request,*args,**kwargs):
        
        url=kwargs.get('title')
        response = APIHelper.get(APIHelper.movies[url])
        
        return Response(response)
    
    
class RetrieveMovie(UserAndAnonThrottleRateMixin,views.APIView):
    
    queryset=Movies.objects.all()
    permission_classes=[permissions.AllowAny]

    def get(self,request,*args,**kwargs):
        id,url=kwargs.get('movieId'),request.GET.get('title')
        url=APIHelper.movies['MOVIE'](id,url)
        response = APIHelper.get(url)
        movie=Movies.objects.filter(movieId=id).first()
        
        if movie:
            
            valid_data=ReviewSerializer(Review.objects.filter(movie=movie).first())
            response['reviews']=valid_data.data
            
        return Response(response)


class InteractedMovies(generics.ListCreateAPIView):
    
    queryset=Movies.objects.all()
    serializer_class=MovieSerializer
    throttle_classes=[UserRateThrottle]
    pagination_class=PageNumberPagination
    
    def get_queryset(self):
        
        return super().get_queryset().order_by('-dateTime')
    
    def perform_create(self, serializer):
        
        id=serializer.validated_data['movieId']
        movie_exists = Movies.objects.filter(movieId=id,user=self.request.user)
        
        if movie_exists.create_movie_on_abscence():
            
            return
        
        return super().perform_create(serializer)


list_movies=ListMovies.as_view()
retrieve_movie=RetrieveMovie.as_view()
interacted_movie=InteractedMovies.as_view()