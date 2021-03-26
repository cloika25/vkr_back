from rest_framework import serializers
from api.models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class ShortEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "FullName", "DateStart", "DateClose", "PhotoPreview"