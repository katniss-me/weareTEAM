from django.contrib import admin
from location.models import Appointed, Current

@admin.register(Appointed)
class AppointedLocationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'address', 'created_at', 'modified_at')

@admin.register(Current)
class CurrentLocationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'address', 'created_at', 'modified_at')