from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ShortUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username']

class ShortProfileSerialiser(serializers.ModelSerializer):
    user = ShortUserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = "user", "photo"

class ProfileSerializer(serializers.ModelSerializer):
    user = ShortUserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "photo"