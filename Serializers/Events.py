from rest_framework import serializers
from api.models import Event
from .Users import ShortProfileSerialiser


class EventSerializer(serializers.ModelSerializer):
    AuthorUserId = ShortProfileSerialiser(read_only=True)

    def create(self, validated_data):
        validated_data.AuthorUserId = self.initial_data.AuthorUserId
        return Event.objects.create(validated_data)

    class Meta:
        model = Event
        fields = '__all__'


class ShortEventSerializer(serializers.ModelSerializer):
    AuthorUserId = ShortProfileSerialiser(read_only=True)

    class Meta:
        model = Event
        fields = ["id", "FullName", "DateStart", "DateClose", "PhotoPreview", "AuthorUserId"]


class SaveEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'
