from rest_framework import serializers
from api.models import Stage, FormatStage


class FormatStagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormatStage
        fields = '__all__'


class StageSerializer(serializers.ModelSerializer):
    FormatId = FormatStagesSerializer(read_only=True)

    class Meta:
        model = Stage
        fields = '__all__'
