from django.contrib import admin

# project directory
from .models import *

admin.site.register(watchList)
admin.site.register(Review)
admin.site.register(Comments)