from rest_framework import throttling


class AnonRateThrottling(throttling.AnonRateThrottle):
    
    rate="2/min"
    scope='post'