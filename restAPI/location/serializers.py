from location.models import Appointed, Current
from rest_framework import serializers

class AppointedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointed
        fields = ('id', 'owner', 'address', 'location')

class CurrentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Current
        fields = ('id', 'owner', 'address', 'location')