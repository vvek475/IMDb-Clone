from django.shortcuts import get_object_or_404

# rest framework
from rest_framework import generics,views,status,permissions
from rest_framework.response import Response

# project directory
from .models import Genres
from .pagination import PageNumberPagination
from .serializers import GenreSerializer
from .throttling import AnonRateThrottling

from utility import api_helper as APIHelper


class GenreListView(generics.ListAPIView):
    
    permission_classes=[permissions.AllowAny]
    queryset=Genres.objects.all()
    serializer_class=GenreSerializer
    pagination_class=PageNumberPagination
    throttle_classes=[AnonRateThrottling]
    
    
class GenreBasedMovies(views.APIView):
    
    permission_classes=[permissions.AllowAny]
    throttle_classes=[AnonRateThrottling]
    
    def get(self,request,*args,**kwargs):
        
        pk,page=kwargs.get('genreId'),request.GET.get('page') or 1
        genre=get_object_or_404(Genres,genreId=pk)
        params={'page':page,'with_genres':genre}
        response=APIHelper.get(APIHelper.movies['GENRE'],**params)
        response=response.get('results')
        
        if response:
            
            return Response(response)
        
        else:
            
            return Response({"detail":"Please contact developer"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


genres=GenreListView.as_view()
genere_based_movies=GenreBasedMovies.as_view()