from rest_framework import serializers
from .models import UserProfile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'first_name', 'last_name', 'passport_photo', 'prava_photo', 'balance', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = UserProfile.objects.create(**validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Custom claims
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name

        return token
