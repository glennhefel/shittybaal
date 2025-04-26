from django.urls import path, include
from .views import homepage, media_detail

app_name = 'media'

urlpatterns = [
    path("", homepage, name="homepage"),
    path("media/<int:pk>/", media_detail, name="m_detail"),
]
