from django.contrib import admin
from django.urls import path, include

from watchlist_app.api.views import WatchDetailAV, ReviewCreateAV, WatchListAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewListAV, ReviewDetailAV

urlpatterns = [
  path('list/', WatchListAV.as_view(), name='watch-list'),
  path('<int:pk>', WatchDetailAV.as_view(), name='watch-detail'),
  path('stream/', StreamPlatformAV.as_view(), name='stream-platform'),
  path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-platform-detail'),
  #path('review', ReviewListAV.as_view(), name='review-list'),
  path('stream/<int:pk>/review-create', ReviewCreateAV.as_view(), name='review-list'),
  path('stream/<int:pk>/review', ReviewListAV.as_view(), name='review-list'),
  path('stream/review/<int:pk>', ReviewDetailAV.as_view(), name='review-detail'),
]
