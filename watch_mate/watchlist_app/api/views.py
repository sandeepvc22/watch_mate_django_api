from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])

def movie_list(request):

  # Get list of movies
  if request.method == 'GET':

    movies = Movie.objects.all()

    serializer = MovieSerializer(movies, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
  
  # Create new movie entry
  if request.method == 'POST':
    serializer = MovieSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()

      return Response(serializer.data, status=status.HTTP_200_OK)
    
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
  
  try: 
    movie = Movie.objects.get(pk=pk)
  except Movie.DoesNotExist:
    return Response({ 'message': 'Data not found.' }, status=status.HTTP_404_NOT_FOUND)
  
  # Get movies list
  if request.method == 'GET':
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  # Update a movie by id
  if request.method == 'PUT':
    serializer = MovieSerializer(movie, data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)

    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  # Delete a movie by id
  if request.method == 'DELETE':
     movie.delete()

     return Response({ "message": "movie delete having id {pk}." }, status=status.HTTP_204_NO_CONTENT)






