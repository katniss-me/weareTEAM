from django.contrib.gis.db import models

# Create your models here.
class Appointed(models.Model):

    owner = models.ForeignKey('auth.User', related_name='location_Appointed')
    address = models.CharField(max_length=255)
    location = models.PointField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)

class Current(models.Model):

    owner = models.ForeignKey('auth.User', related_name='location_Current')
    address = models.CharField(max_length=255)
    location = models.PointField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)