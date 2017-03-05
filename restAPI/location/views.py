from rest_framework import permissions

from location.models import Appointed, Current
from location.permission import IsOwnerOrReadOnly
from location.serializers import AppointedSerializer, CurrentSerializer
from rest_framework import generics

class AppointedLocationsView(generics.ListCreateAPIView):
    queryset = Appointed.objects.all()
    serializer_class = AppointedSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
            serializer.save(owner=self.request.user)

class CurrentLocationsView(generics.ListCreateAPIView):
    queryset = Current.objects.all()
    serializer_class = CurrentSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
            serializer.save(owner=self.request.user)