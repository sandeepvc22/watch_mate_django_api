from re import L
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.views import APIView

class MovieListAV(APIView):
  
  # GET => Get all movies list
  def get(self, request):
    movies = Movie.objects.all()

    serializer = MovieSerializer(movies, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def post(self, request):
    serializer = MovieSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()

      return Response(serializer.data, status=status.HTTP_200_OK)
    
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailAV(APIView):

  def get(self, request, pk):
    try: 
      movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
      return Response({ 'message': 'Data not found.' }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def put(self, request, pk):
    try: 
      movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
      return Response({ 'message': 'Data not found.' }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = MovieSerializer(movie, data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)

    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

  def delete(self, request, pk):
    try: 
      movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
      return Response({ 'message': 'Data not found.' }, status=status.HTTP_404_NOT_FOUND)
    
    movie.delete()

    return Response({ "message": "movie delete having id {pk}." }, status=status.HTTP_204_NO_CONTENT)

