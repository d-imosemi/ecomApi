from .views import DetailAdminUser, DetailUser, ListAdminUser, ListUser, RegisterAPI
from django.urls import path

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/user/', ListUser.as_view(), name='listuser'),
    path('api/user/<int:pk>', DetailUser.as_view(), name='detailuser'),


    path('api/adminuser/', ListAdminUser.as_view(), name='listadminuser'),
    path('api/adminuser/<int:pk>', DetailAdminUser.as_view(), name='detailadminuser'),
]