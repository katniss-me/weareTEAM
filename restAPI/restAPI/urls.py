from django.conf.urls import include, url
from django.contrib import admin

from location.views import ListCreateLocations

urlpatterns = [
    # Examples:
    # url(r'^$', 'restAPI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/locations', ListCreateLocations.as_view(), name='list_locations')
]
