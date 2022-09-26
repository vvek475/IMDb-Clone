from rest_framework import throttling


class AnonRateThrottling(throttling.AnonRateThrottle):
    
    rate="12/min"
    scope='list'