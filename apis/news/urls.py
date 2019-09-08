from django.urls import path
from apis.news import views


urlpatterns = [
    path("create/", views.CreateNewsAPIView.as_view(), name="create_news" )
]
