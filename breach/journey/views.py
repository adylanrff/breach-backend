import random
import string 
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from journey.models import Journey, Place, Voucher, User, PlaceJourneyStatus
from journey.serializers import JourneySerializer,JourneyDetailSerializer, PlaceSerializer, VoucherSerializer, UserSerializer, UserChangeSerializer, PlaceJourneyStatusSerializer
from rest_framework import viewsets

class JourneyViewSet(viewsets.ModelViewSet):
  queryset = Journey.objects.all()
  serializer_class = JourneySerializer

  def get_serializer_class(self):
    if self.action == 'list':
      return JourneyDetailSerializer
    if self.action == 'retrieve':
      return JourneyDetailSerializer
    if self.action == 'create':
      return JourneySerializer
    if self.action == 'update':
      return JourneySerializer
    return JourneyDetailSerializer

  def perform_create(self, serializer):
    data = serializer.data
    places = data.pop('place')
    journey = Journey.objects.create(**data)
    for p in places:
      place = Place.objects.get(pk=p)
      place_status = PlaceJourneyStatus.objects.create(place=place)
      journey.place_status.add(place_status)
    journey.save()
    return journey

class PlaceViewSet(viewsets.ModelViewSet):
  queryset = Place.objects.all()
  serializer_class = PlaceSerializer

class VoucherViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
  
  queryset = Voucher.objects.all()
  serializer_class = VoucherSerializer
  def perform_create(self, serializer):
    alphanumeric = string.ascii_lowercase + ''.join([str(i) for i in range(10)])
    code = ''.join(random.choice(alphanumeric) for i in range(10))
    serializer.save(code = code)

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def get_serializer_class(self):
    if self.action == 'list':
        return UserSerializer
    if self.action == 'retrieve':
        return UserSerializer
    if self.action == 'create':
        return UserChangeSerializer
    if self.action == 'update':
        return UserChangeSerializer
    return UserSerializer

class PlaceJourneyStatusViewSet(viewsets.ModelViewSet):
  queryset = PlaceJourneyStatus.objects.all()
  serializer_class = PlaceJourneyStatusSerializer