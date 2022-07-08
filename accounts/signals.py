from django.db.models.signals import post_save
from django.dispatch import receiver

from ecommapi.models import Profile

from django.contrib.auth import get_user_model


User = get_user_model()

# PROFILE-------SIGNALS

@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user_id=instance)


@receiver(post_save, sender= User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()