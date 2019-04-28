import random
import string
from rest_framework import serializers
from .models import Journey, Place, User, Voucher

class PlaceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Place
    fields = ('id','name','description', 'location', 'image_url')

# Journey serializers 
class JourneySerializer(serializers.ModelSerializer):
  place = serializers.PrimaryKeyRelatedField(many=True, queryset=Place.objects.all())

  class Meta:
    model = Journey
    fields = ('id','title','author', 'duration', 'place' ,'image_url')

# Journey serializers 
class JourneyDetailSerializer(serializers.ModelSerializer):
  place = PlaceSerializer(many=True)
  
  class Meta:
    model = Journey
    fields = ('id','title','author', 'duration', 'place' ,'image_url')

#voucher 
class VoucherSerializer(serializers.ModelSerializer):

  class Meta:
    model = Voucher
    fields = ('id', 'name', 'discount', 'description','code','image_url', 'category', 'owner')
    read_only_fields = ('code', )
    
# User serializers
class UserSerializer(serializers.ModelSerializer):
  journey = JourneySerializer(many=True)
  voucher = VoucherSerializer(many=True)

  class Meta:
    model = User
    fields = ('id', 'name', 'journey', 'voucher')

class UserChangeSerializer(serializers.ModelSerializer):
  journey = serializers.PrimaryKeyRelatedField(many=True, queryset=Journey.objects.all())

  class Meta:
    model = User
    fields = ('id', 'name', 'journey', 'voucher')
