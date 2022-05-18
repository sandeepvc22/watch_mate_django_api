from asyncio import mixins
from watchlist_app.models import WatchList, StreamPlatform, Reviews
from watchlist_app.api.serializers import StreamPlatformSerializer, WatchListSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework import status

from rest_framework import mixins
from rest_framework import generics

from rest_framework.views import APIView


class ReviewDetailAV(mixins.RetrieveModelMixin, generics.GenericAPIView):
  queryset = Reviews.objects.all()
  serializer_class = ReviewSerializer

  def get(self, request, *args, **kwargs):
      return self.retrieve(request, *args, **kwargs)

class ReviewListAV(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
  queryset = Reviews.objects.all()
  serializer_class = ReviewSerializer

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)
  
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)


class StreamPlatformAV(APIView):

  def get(self, request):
    platform = StreamPlatform.objects.all()

    serializer = StreamPlatformSerializer(platform, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


  def post(self, request):
    serializer = StreamPlatformSerializer(data=request.data)

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


class StreamPlatformDetailAV(APIView):

  def get(self, request, pk):
    try: 
      stream_platform = StreamPlatform.objects.get(pk=pk)
    except StreamPlatform.DoesNotExist:
      return Response({ 'message': 'Data not found.' }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = StreamPlatformSerializer(stream_platform)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def put(self, request, pk):
    try: 
      stream_platform = StreamPlatform.objects.get(pk=pk)
    except StreamPlatform.DoesNotExist:
      return Response({ 'message': 'Data not found.' }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = StreamPlatformSerializer(stream_platform, data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)

    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

  def delete(self, request, pk):
    try: 
      stream_platform = StreamPlatform.objects.get(pk=pk)
    except StreamPlatform.DoesNotExist:
      return Response({ 'message': 'Data not found.' }, status=status.HTTP_404_NOT_FOUND)
    
    stream_platform.delete()

    return Response({ "message": "watch list deleted." }, status=status.HTTP_204_NO_CONTENT)
