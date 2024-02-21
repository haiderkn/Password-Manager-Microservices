"""
Serializers for the userapi view.
"""
from rest_framework import serializers
from django.contrib.auth import (
    get_user_model,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'name')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 5,
            }
        }

    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update and return user."""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Token Generation Pair Serializer"""
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.name
        token['email'] = user.email

        return token


class TokenDecodeSerializer(serializers.Serializer):
    """Token Decode Serializer for other microservices"""
    token = serializers.CharField(required=True)


class ListUserSerializer(serializers.ModelSerializer):
    """Get User Data from models to authenticate other microservices"""

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "name",
            "email",
        ]

    def to_representation(self, instance):
        return super().to_representation(instance)
