from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework import permissions
from apis.accounts.serializers import UserCreateSerializer
from rest_framework.views import APIView

# Create your views here.

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]
