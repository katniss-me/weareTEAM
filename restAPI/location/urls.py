from django.conf.urls import url
from location.views import ListCreateLocations

urlpatterns = [
    url(r'^appointed/', ListCreateLocations.as_view(), name='list_locations'),
]
