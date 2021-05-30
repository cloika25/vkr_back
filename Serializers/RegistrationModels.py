from rest_framework import serializers
from api.models import RegistrationsModal
from .Events import ShortEventSerializer
from .Stages import StageSerializer
from .Users import ProfileSerializer


class ListParticipants(serializers.ModelSerializer):
    UserId = ProfileSerializer(read_only=True)
    StageId = StageSerializer(read_only=True)
    EventId = ShortEventSerializer(read_only=True)

    class Meta:
        model = RegistrationsModal
        fields = ['Fields', 'id', 'UserId', 'StageId', 'EventId']
