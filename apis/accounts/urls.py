from django.urls import path
from apis.accounts import views

urlpatterns = [
    path("users/create/", views.UserCreateAPIView.as_view(), name="create_uesr" )
]
