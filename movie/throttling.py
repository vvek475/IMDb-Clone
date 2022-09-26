# rest framework
from rest_framework import throttling

class UserRateThrottle(throttling.UserRateThrottle):
    
    rate='12/min'
    scope='movies-list'
    
    
class AnonRateThrottle(throttling.AnonRateThrottle):
    
    rate='5/min'
    scope='movies-list'