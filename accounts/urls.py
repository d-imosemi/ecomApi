from .views import DetailUser, ListUser, RegisterAPI
from django.urls import path

urlpatterns = [
    path('users/', ListUser.as_view(), name='listuser'),
    path('users/<int:pk>', DetailUser.as_view(), name='detailuser'),
]