from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from location.views import ListCreateLocations

router = DefaultRouter()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/locations', ListCreateLocations.as_view(), name='list_locations'),
    url(r'^location/', include('location.urls')),
    url(r'^users/', include('users.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
