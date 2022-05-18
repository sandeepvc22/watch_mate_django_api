from turtle import title
from rest_framework import serializers

from watchlist_app.models import WatchList, StreamPlatform

# Model Serializer
class WatchListSerializer(serializers.ModelSerializer):

  class Meta:
    model = WatchList

    fields = "__all__"
    
    # fields = ['id', 'name', 'description']

    # exclude fields
    #exclude = ['active', 'id']


class StreamPlatformSerializer(serializers.ModelSerializer):
  # watchlist =  WatchListSerializer(many=True, read_only=False)
  # watchlist = serializers.StringRelatedField(many=True)
  watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
  
  class Meta:
    model = StreamPlatform
    fields = "__all__"


# Custom validator
# def check_name_lenth(value):
#   if len(value) < 2:
#     raise serializers.ValidationError("Name is too short.")
#   else:
#     return value

# class MovieSerializer(serializers.Serializer):
#   id = serializers.IntegerField(read_only=True)
#   name = serializers.CharField(validators=[check_name_lenth])
#   description = serializers.CharField()
#   active = serializers.BooleanField()

#   def create(self, validated_data):
#     return Movie.objects.create(**validated_data)
  
#   def update(self, instance, validated_data):
#     instance.name = validated_data.get('name', instance.name)
#     instance.description = validated_data.get('description', instance.description)
#     instance.active = validated_data.get('active', instance.active)

#     instance.save()

#     return instance
  
#   # Object level validation
#   def validate(self, data):
#     if data['name'] == data['description']:
#       raise serializers.ValidationError("Title and Description should be different.")
    
#     else:
#       return data
  
  # # Field level validation
  # def validate_name(self, value):
  #   if len(value) < 2:
  #     raise serializers.ValidationError("Name is too short.")
  #   else:
  #     return value
