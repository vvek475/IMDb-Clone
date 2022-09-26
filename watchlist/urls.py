from django.urls import path

# project directory
from .views import *

urlpatterns=[

    path('',watchlist,),
    path('<int:watchlistId>',update_watchlist),
    path('review',review),
    path('comment',comment),
    path('comment/<int:reviewId>',retrieve_comments) 

]