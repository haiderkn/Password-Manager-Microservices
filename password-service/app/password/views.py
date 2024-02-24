"""
views for the passwords APIs
"""
from rest_framework import status
from password import serializers
from core.models import LoginCredential
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LoginCredentialSerializer
from rest_framework.permissions import IsAuthenticated


class CredentialCreate(APIView):
    """POST operation"""
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        complex_data = request.data
        serializer = serializers.LoginCredentialSerializer(data=complex_data)
        if serializer.is_valid():
            serializer.save(user_id=self.request.user.id)
            res = {"message": "successfully saved."}
            return Response(res, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class CredentialList(APIView):
    """POST operation"""
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        print(request)
        complex_data = LoginCredential.objects.filter(
                                     user_id=self.request.user.id)
        serializer = serializers.LoginCredentialSerializer(
                                     complex_data, many=True)
        return Response(serializer.data)


class CredentialEdit(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        print(request)
        complex_data = LoginCredential.objects.get(id=pk)
        serializer = serializers.LoginCredentialSerializer(complex_data)
        return Response(serializer.data)

    def put(self, request, pk=None, format=None):
        id = request.data['id']
        new_instance = request.data
        old_instance = LoginCredential.objects.get(id=id)
        serializer = LoginCredentialSerializer(old_instance, data=new_instance)
        if serializer.is_valid():
            serializer.save()
            response = {'message': 'updated'}
            return Response(response)

    def patch(self, request, pk=None, format=None):
        id = request.data['id']
        new_instance = request.data
        old_instance = LoginCredential.objects.get(id=id)
        serializer = LoginCredentialSerializer(old_instance,
                                               data=new_instance,
                                               partial=True)
        if serializer.is_valid():
            serializer.save()
