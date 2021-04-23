from rest_framework import serializers
from api.models import Stage, FormatStage

class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = '__all__'


class FormatStagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormatStage
        fields = '__all__'