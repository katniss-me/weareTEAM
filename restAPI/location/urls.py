from django.conf.urls import url
from location.views import AppointedLocationsView, CurrentLocationsView

urlpatterns = [
    url(r'^appointed/', AppointedLocationsView.as_view(), name='list_appointed'),
    url(r'^current/', CurrentLocationsView.as_view(), name='list_current'),
]
