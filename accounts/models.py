from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Email should be provided'))

        email = self .normalize_email(email)
        
        new_user=self.model(email=email,**extra_fields)

        new_user.set_password(password)

        new_user.save()
        return new_user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser should have is_staff as True'))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser should have is_superuser as True'))

        if extra_fields.get('is_active') is not True:
            raise ValueError(_('Superuser should have is_active as True'))
        
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    GENDER = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female')
    )
    gender = models.CharField(choices=GENDER, max_length=20, null=True, blank=True)
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=80, unique=True)
    phone_number = PhoneNumberField(null=False, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'phone_number']
    
    objects = CustomUserManager()

    def __str__(self):
        return f"User {self.email}"




@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="My Ecomm"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@MiniEcomm.local",
        # to:
        [reset_password_token.user.email]
    )