# project directory
from .throttling import UserRateThrottle,AnonRateThrottle

class UserAndAnonThrottleRateMixin:
    
    throttle_classes=[UserRateThrottle,AnonRateThrottle]    
