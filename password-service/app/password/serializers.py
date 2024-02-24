from rest_framework import serializers
from core.models import LoginCredential


class LoginCredentialSerializer(serializers.ModelSerializer):
    """Serializer for LoginCredential objects."""

    class Meta:
        model = LoginCredential
        fields = "__all__"
        extra_kwargs = {
            "user_id": {"read_only": True},
        }
