"""IMDb_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# rest framework
from rest_framework import permissions

# swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    
   openapi.Info(
       
      title="Open Db API",
      default_version='v1',
      description="IMDb rip-off",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="vickfreeindia@gmail.com"),
      license=openapi.License(name="BSD License"),
      schemes=['https','http']
   ),
   url='https://imdb-clone-production.up.railway.app/swagger/',

   public=True,
   permission_classes=[permissions.AllowAny],
   
)


from django.contrib import admin
from django.urls import path,include,re_path

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('genres/',include('genres.urls')),
    path('movies/',include('movie.urls')),
    path('watchlist/',include('watchlist.urls')),
    path('auth/',include('jwtAuth.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
]
