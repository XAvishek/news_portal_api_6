from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt import authentication
from rest_framework import permissions
from apis.news.serializers import NewsSerializer
from rest_framework.decorators import api_view
from apis.news.models import News
from rest_framework.response import Response
from rest_framework import status
# from apis.news import permissions as news_permissions
from helpers import permissions as news_permissions

# Create your views here.

class CreateNewsAPIView(generics.CreateAPIView):
    authentication_classes = (authentication.JWTAuthentication,)
    serializer_class = NewsSerializer
    permission_classes = (news_permissions.IsNewsCreator,)

class ListNewsAPIView(generics.ListAPIView):
    serializer_class = NewsSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = News.objects.all()

class DetailNewsAPIView(generics.RetrieveAPIView):
    serializer_class = NewsSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = News.objects.all()


    # def get_queryset(self):
    #     return News.objects.all()
    

class DeleteNewsAPIView(generics.DestroyAPIView):
    authentication_classes = (authentication.JWTAuthentication,)
    serializer_class = NewsSerializer
    permission_classes = (news_permissions.IsNewsModifier,)
    queryset = News.objects.all()


class UpdateNewsAPIView(generics.UpdateAPIView):
    authentication_classes = (authentication.JWTAuthentication,)
    serializer_class = NewsSerializer
    permission_classes = (news_permissions.IsNewsModifier,)
    queryset = News.objects.all()


@api_view(['GET', 'POST'])
def get_category_list(request):
    categories = dict(News.CATEGORY)
    return Response(categories, status=status.HTTP_200_OK)
