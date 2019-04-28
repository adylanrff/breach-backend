from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from journey.models import Journey, Place, Voucher
from journey.serializers import JourneySerializer,JourneyDetailSerializer, PlaceSerializer, VoucherSerializer
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
  
class PlaceViewSet(viewsets.ModelViewSet):
  queryset = Place.objects.all()
  serializer_class = PlaceSerializer

class VoucherViewSet(viewsets.ModelViewSet):
  queryset = Voucher.objects.all()
  serializer_class = VoucherSerializer