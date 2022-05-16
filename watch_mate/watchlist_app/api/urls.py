from django.contrib import admin
from django.urls import path, include

from watchlist_app.api.views import WatchDetailAV, WatchListAV, StreamPlatformAV

urlpatterns = [
  path('list/', WatchListAV.as_view(), name='watch-list'),
  path('<int:pk>', WatchDetailAV.as_view(), name='watch-detail'),
  path('stream/', StreamPlatformAV.as_view(), name='stream-platform'),
]
