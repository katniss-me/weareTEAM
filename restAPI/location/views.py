from location.models import Appointed, Current
from location.serializers import AppointedSerializer, CurrentSerializer
from rest_framework import generics

# Create your views here.
class AppointedLocationsView(generics.ListCreateAPIView):
    queryset = Appointed.objects.all()
    serializer_class = AppointedSerializer

class CurrentLocationsView(generics.ListCreateAPIView):
    queryset = Current.objects.all()
    serializer_class = CurrentSerializer