"""
Views for the user api
"""
import jwt
from app import settings
from django.contrib.auth import get_user_model
from user.serializers import (
    UserSerializer,
    MyTokenObtainPairSerializer,
    TokenDecodeSerializer,
    ListUserSerializer,
)
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated


class CreateUserView(APIView):
    """Please Create a new user in the system."""

    serializer_class = UserSerializer

    def post(self, request):
        """Create a new user."""
        complex_data = request.data
        serializer = self.serializer_class(data=complex_data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class ManageUserView(APIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Retrieve the authenticated user."""
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)

    def put(self, request):
        """Update the authenticated user."""
        serializer = self.serializer_class(
            request.user,
            data=request.data,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def patch(self, request):
        """Update the authenticated user."""
        serializer = self.serializer_class(
            request.user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class MyTokenObtainPairView(TokenObtainPairView):
    """Get token-pair view"""
    serializer_class = MyTokenObtainPairSerializer


class TokenDecode(APIView):
    """Token Decoder View for other microservices"""

    serializer_class = TokenDecodeSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        token = request.data.get('token', None)
        if token:
            try:
                payload = jwt.decode(
                    token,
                    settings.SECRET_KEY,
                    algorithms=['HS256'],
                )
            except Exception as err:
                raise AuthenticationFailed(F'Unauthenticated: {err}')
            user = get_user_model().objects.get(id=payload['user_id'])
            serializer = ListUserSerializer(instance=user)
            return Response(serializer.data)
        raise AuthenticationFailed('Unauthenticated')
