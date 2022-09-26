# rest_framework
from rest_framework import generics,viewsets,mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# project directory
from .mixins import CreateMovieMixin
from .models import *
from .pagination import PageNumberPagination
from .serializers import *
from .throttling import UserRateThrottle


class ListCreateWatchList(CreateMovieMixin,generics.ListCreateAPIView):
    
    # create a custom queryset that returns all user model
    queryset=watchList.objects.all()
    serializer_class=ListWatchListSerializers
    permission_classes = (IsAuthenticated,)
    pagination_class=PageNumberPagination
    throttle_classes=[UserRateThrottle]

    def get_queryset(self,):
        
        qs=super().get_queryset()
        
        return qs.filter(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        
        watchlist=watchList.objects.filter(user=request.user)
        watchlist.add_in_movie_abscence(self.create_movie(request.data.get('movies')))
        
        return Response({'detail':'watchlist updated','data':ListWatchListSerializers(watchlist.first()).data})


class UpdateWatchList(mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    
    # we're using mixins here as retrieve is not needed
    serializer_class=EditWatchlistSerializer
    lookup_field='pk'
    queryset=watchList.objects.all()
    throttle_classes=[UserRateThrottle]
    
    def perform_update(self, serializer,*args,**kwargs):
        
        movie=serializer.initial_data.get('movieId')
        instance=serializer.save()
        instance.movies.remove(movie)
        
        return
    
    def perform_destroy(self, instance):
        
        instance.movies.clear()
        
        
class ListCreateReview(CreateMovieMixin,generics.ListCreateAPIView):
    
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    pagination_class=PageNumberPagination
    throttle_classes=[UserRateThrottle]
    
    def create(self, request, *args, **kwargs):
        
        request.data['movie']=self.create_movie(request.data.get('movie_data')).id
        
        return super().create(request,*args,**kwargs)


class ListCreateComment(generics.ListCreateAPIView):
    
    queryset=Comments.objects.all()
    serializer_class=CommentSerializer
    pagination_class=PageNumberPagination
    throttle_classes=[UserRateThrottle]
    
    
class RetriveComments(generics.ListAPIView):
    
    queryset=Review.objects.all()
    serializer_class=CommentSerializer
    lookup_field='pk'
    throttle_classes=[UserRateThrottle]
    
    def get(self,request,*args,**kwargs):
        
        qs=self.get_queryset()
        pk=kwargs.get('reviewId')
        comments=qs.get(pk=pk).comments_set.all()
        qs=CommentSerializer(list(comments),many=True)
        
        return Response(qs.data)
        

watchlist=ListCreateWatchList.as_view()
update_watchlist=UpdateWatchList.as_view({'put':'update','delete':'destroy'})
review=ListCreateReview.as_view()
comment=ListCreateComment.as_view()
retrieve_comments=RetriveComments.as_view()