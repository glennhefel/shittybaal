from django.urls import path, include
from django.contrib import admin

from media.views import *
#from .views import add_media, homepage, media_detail

app_name = 'media'

urlpatterns = [
    path("", homepage, name="homepage"),
    path("media/<int:pk>/", media_detail, name="m_detail"),
    path("add_media/", add_media, name="add_media"),
    
]
