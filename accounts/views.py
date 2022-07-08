from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema 

from .serializers import (
    LoginSerializer, 
    MainUserSerializer,
    UpdateUserSerializer,
    UserSerializer, 
    RegisterSerializer, 
    ChangePasswordSerializer,
)

from django.contrib.auth import get_user_model


User = get_user_model()


# USER API VIEW

class ListUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class DeleteDetailUser(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class UpdateDetailUser(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    http_method_names = ['get', 'post', 'put']
    permission_classes = [permissions.IsAdminUser]



# REGISTERATION API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    @swagger_auto_schema(operation_summary="Endpoint for a user SignUp")
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": MainUserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


# Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    @swagger_auto_schema(operation_summary="Endpoint for a user Login")
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
        })


# User API
class MainUser(generics.RetrieveUpdateDestroyAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'put', 'delete']
    serializer_class = MainUserSerializer

    def get_object(self):
        return self.request.user

 
# Change Password API
class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post', 'put']

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


