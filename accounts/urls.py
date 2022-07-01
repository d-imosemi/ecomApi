from .views import DetailUser, ListUser, RegisterAPI
from django.urls import path

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/users/', ListUser.as_view(), name='listuser'),
    path('api/users/<int:pk>', DetailUser.as_view(), name='detailuser'),
]