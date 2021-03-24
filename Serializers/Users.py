from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'