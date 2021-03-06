from django.contrib import admin
from django.urls import path, include

from knox import views as knox_views
from accounts.views import LoginAPI,  ChangePasswordView, MainUser, RegisterAPI

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Ecomm API",
      default_version='v1',
      description="A Rest API for a mini Ecommerce API",
      contact=openapi.Contact(email="imosemij@gmail.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/v1/', include('ecommapi.urls')),
   path('auth/', include('accounts.urls')),
   
   path('auth/register/', RegisterAPI.as_view(), name='register'),
   path('auth/login/', LoginAPI.as_view(), name='login'),

   
   path('auth/main_user/', MainUser.as_view()),
   path('auth/logout/', knox_views.LogoutView.as_view(), name='logout'),
   path('auth/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),


   path('auth/change-password/', ChangePasswordView.as_view(), name='change-password'),
   path('auth/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),


   path('swagger<format>.json|.yaml', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]