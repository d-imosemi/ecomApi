from .views import DeleteDetailUser, ListUser, UpdateDetailUser
from django.urls import path

urlpatterns = [
    path('users/', ListUser.as_view(), name='listuser'),
    path('update/user/<int:pk>/', UpdateDetailUser.as_view(), name='update_user'),
    path('delete/user/<int:pk>/', DeleteDetailUser.as_view(), name='delete_user'),

]