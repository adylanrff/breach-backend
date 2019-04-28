import random
import string
from rest_framework import serializers
from .models import Journey, Place, User, Voucher,PlaceJourneyStatus

class PlaceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Place
    fields = ('id','name','description', 'location', 'image_url', 'is_halal')

class PlaceJourneyStatusSerializer(serializers.ModelSerializer):
  class Meta:
    model = PlaceJourneyStatus
    fields = ('id','place', 'is_visited')

class PlaceJourneyStatusDetailSerializer(serializers.ModelSerializer):
  place = PlaceSerializer(many=False)
  class Meta:
    model = PlaceJourneyStatus
    fields = ('id','place', 'is_visited')
    
# Journey serializers 
class JourneySerializer(serializers.ModelSerializer):
  place = serializers.PrimaryKeyRelatedField(many=True, queryset=Place.objects.all())

  class Meta:
    model = Journey
    fields = ('id','title','author', 'duration', 'place', 'image_url', 'reward_category')


class JourneyDetailSerializer(serializers.ModelSerializer):
  place_status = PlaceJourneyStatusDetailSerializer(many=True)

  class Meta:
    model = Journey
    fields = ('id','title','author', 'duration', 'place_status' ,'image_url', 'reward_category')

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
