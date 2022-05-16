from django.contrib import admin
from django.urls import path, include

from watchlist_app.views import movies_list, movie_detail

urlpatterns = [
  path('list/', movies_list, name='movies-list'),
  path('<int:pk>', movie_detail, name='movie-detail'),
]
