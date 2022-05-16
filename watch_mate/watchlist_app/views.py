from django.shortcuts import render
from django.http import JsonResponse
from watchlist_app.models import Movie

# Create your views here.

def movies_list(request):
  query_set = Movie.objects.all()

  data = {
    "movies": list(query_set.values())
  }

  return JsonResponse(data)

def movie_detail(request, pk):
  movie = Movie.objects.get(pk=pk)

  data = {
    'name': movie.name,
    'description': movie.description,
    'active': movie.active
  }

  return JsonResponse(data)



