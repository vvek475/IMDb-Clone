from django.db.models.signals import post_save
from django.contrib.auth.models import User

# from directory
from watchlist.models import watchList

def add_watchlist(sender,instance,created,**kwargs):
    
    if created:
        
        watchList.objects.create(user=instance)    
    
post_save.connect(add_watchlist,sender=User)