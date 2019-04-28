from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from journey.models import Journey, Place
from journey.serializers import JourneySerializer, PlaceSerializer
from rest_framework import viewsets

class JourneyViewSet(viewsets.ModelViewSet):
  queryset = Journey.objects.all()
  serializer_class = JourneySerializer

class PlaceViewSet(viewsets.ModelViewSet):
  queryset = Place.objects.all()
  serializer_class = PlaceSerializer