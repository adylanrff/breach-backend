from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JourneyViewSet, PlaceViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'journey', JourneyViewSet)
router.register(r'place', PlaceViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]