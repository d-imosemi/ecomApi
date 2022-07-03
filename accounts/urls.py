from .views import DeleteDetailUser, ListUser, UpdateDetailUser
from django.urls import path

urlpatterns = [
    path('users/', ListUser.as_view(), name='listuser'),
    path('update/users/<int:pk>/', UpdateDetailUser.as_view(), name='update_user'),
    path('delete/users/<int:pk>/', DeleteDetailUser.as_view(), name='delete_user'),

]