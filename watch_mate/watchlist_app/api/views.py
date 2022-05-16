from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])

def movie_list(request):

  # Get list of movies
  if request.method == 'GET':

    movies = Movie.objects.all()

    serializer = MovieSerializer(movies, many=True)

    return Response(serializer.data)
  
  # Create new movie entry
  if request.method == 'POST':
    serializer = MovieSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()

      return Response(serializer.data)
    
    else:
      return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
  
  # Get movies list
  if request.method == 'GET':
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
  
  # Update a movie by id
  if request.method == 'PUT':
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie, data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)

    else:
      return Response(serializer.data)
  
  # Delete a movie by id
  if request.method == 'DELETE':
     movie = Movie.objects.get(pk=pk)
     movie.delete()

     return Response({ "message": "movie delete having id {pk}." })





