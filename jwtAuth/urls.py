from django.urls import path


# rest framework
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# project directory
from .views import *

urlpatterns = [
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register',create_user,name='register_user')
    
]