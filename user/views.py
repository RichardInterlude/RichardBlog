from . serializers import *
from . models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import login, logout, authenticate
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class RegisterationView(APIView):
    def post(self, request):
        try:
            serializers = RegisterationSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self, request):
        self.permission_classes = [IsAuthenticated]
        self.authentication_classes = [JWTAuthentication]
        try:
            profile = get_object_or_404(profile, user=request.user)
            serializers = ProfileSerializer(profile, data=request.data, partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class LoginView(APIView):
    authentication_classes = [JWTAuthentication]
    def post(self, request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class LogoutView(APIView):
    def post(self, request):
        try:
            logout(request)
            return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        try:
            profile = get_object_or_404(Profile, user=request.user)
            serializers = ProfileSerializer(profile)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class DeleteUserView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def delete(self,request):
        try:
            user = request.user
            user.delete()
            return Response({'message':'User Deleted Successfully'},status=status.HTTP_200_OK) 
        except Exception as e:
            return Response({'Error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)