from django.urls import path
from video import views

urlpatterns = [
    path('', views.index, name='index'),
    path('video/', views.video_download, name='video_download'),
    path('playlist-downloader/', views.playlist_download, name='playlist_download'),
]