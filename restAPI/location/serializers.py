from location.models import Appointed, Current
from rest_framework import serializers

class AppointedSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Appointed
        fields = ('id', 'owner', 'address', 'location')

class CurrentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Current
        fields = ('id', 'owner', 'address', 'location')