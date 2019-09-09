from django.urls import path
from apis.news import views


urlpatterns = [
    path("", views.ListNewsAPIView.as_view(), name="list_news" ),
    path("<int:pk>/", views.DetailNewsAPIView.as_view(), name="single_news" ),
    path("<int:pk>/delete/", views.DeleteNewsAPIView.as_view(), name="delete_news" ),
    path("<int:pk>/update/", views.UpdateNewsAPIView.as_view(), name="update_news" ),
    path("create/", views.CreateNewsAPIView.as_view(), name="create_news" ),
    path("categories/", views.get_category_list, name="list_categories" )
]
