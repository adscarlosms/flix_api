from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse




urlpatterns = [
 

    path('admin/', admin.site.urls),

    path('api/v1/', include('authentication.urls')),
    
    path('api/v1/', include('genres.urls')),

    path('api/v1/', include('movies.urls')),

    path('api/v1/', include('actors.urls')),

    path('api/v1/', include('reviews.urls')),


]
