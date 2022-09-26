from django.contrib.auth.models import User

# rest framework
from rest_framework import serializers


class UserModelSerializer(serializers.ModelSerializer):
    
    password=serializers.CharField(write_only=True)
    
    class Meta:
        model=User
        fields=['username','password']