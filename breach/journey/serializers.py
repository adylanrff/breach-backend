from rest_framework import serializers
from .models import Journey, Place, User, Voucher

# User serializers
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'name')

# Journey serializers 
class JourneySerializer(serializers.ModelSerializer):
  place = serializers.PrimaryKeyRelatedField(many=True, queryset=Place.objects.all())
  
  class Meta:
    model = Journey
    fields = ('id','title','author', 'duration', 'place' ,'image_url')

class PlaceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Place
    fields = ('id','name','description', 'location', 'image_url')

#voucher 
class VoucherSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.name')
  class Meta:
    model = Voucher
    fields = ('id', 'name', 'discount', 'description', 'user')
