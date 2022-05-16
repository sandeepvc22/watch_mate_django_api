from watchlist_app.models import WatchList, StreamPlatform
from watchlist_app.api.serializers import StreamPlarformSerializer, WatchListSerializer
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView

class StreamPlatformAV(APIView):

  def get(self, request):
    platform = StreamPlatform.objects.all()

    serializer = StreamPlarformSerializer(platform, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


  def post(self, request):
    serializer = StreamPlarformSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()

      return Response(serializer.data, status=status.HTTP_200_OK)
    
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class WatchListAV(APIView):
  
  # GET => Get all movies list
  def get(self, request):
    watch_list = WatchList.objects.all()

    serializer = WatchListSerializer(watch_list, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def post(self, request):
    serializer = WatchListSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()

      return Response(serializer.data, status=status.HTTP_200_OK)
    
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchDetailAV(APIView):

  def get(self, request, pk):
    try: 
      watch_list = WatchList.objects.get(pk=pk)
    except WatchList.DoesNotExist:
      return Response({ 'message': 'Data not found.' }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = WatchListSerializer(watch_list)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def put(self, request, pk):
    try: 
      watch_list = WatchList.objects.get(pk=pk)
    except WatchList.DoesNotExist:
      return Response({ 'message': 'Data not found.' }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = WatchListSerializer(watch_list, data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)

    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

  def delete(self, request, pk):
    try: 
      watch_list = WatchList.objects.get(pk=pk)
    except WatchList.DoesNotExist:
      return Response({ 'message': 'Data not found.' }, status=status.HTTP_404_NOT_FOUND)
    
    watch_list.delete()

    return Response({ "message": "watch list deleted." }, status=status.HTTP_204_NO_CONTENT)

