from django.contrib.auth.models import User

# rest framework
from rest_framework import generics


# project directory
from .permissions import OnlyAllowAnon
from .serializers import UserModelSerializer
from .throttling import AnonRateThrottling


class CreateUser(generics.CreateAPIView):
    
    queryset=User.objects.all()
    serializer_class=UserModelSerializer
    permission_classes=[OnlyAllowAnon]
    throttle_classes=[AnonRateThrottling]
    
    
create_user=CreateUser.as_view()