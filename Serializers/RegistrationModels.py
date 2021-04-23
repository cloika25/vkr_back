from rest_framework import serializers
from api.models import RegistrationsModal
from .Events import ShortEventSerializer
from .Stages import StageSerializer, FormatStagesSerializer
from .Users import CabinetSerializer


class ListParticipants(serializers.ModelSerializer):
    UserId = CabinetSerializer(read_only=True)
    StageId = StageSerializer(read_only=True)
    EventId = ShortEventSerializer(read_only=True)

    class Meta:
        model = RegistrationsModal
        fields = ['Fields', 'id', 'UserId', 'StageId', 'EventId']
