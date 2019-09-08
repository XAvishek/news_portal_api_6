from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt import authentication
from rest_framework import permissions
from apis.news.serializers import NewsSerializer


# Create your views here.

class CreateNewsAPIView(generics.CreateAPIView):
    authentication_classes = (authentication.JWTAuthentication,)
    serializer_class = NewsSerializer
    permission_classes = (permissions.IsAuthenticated,)

        
