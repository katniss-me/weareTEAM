from django.shortcuts import render
from location.models import Location
from location.serializers import LocationSerializer
from rest_framework import generics

# Create your views here.
class ListCreateLocations(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer