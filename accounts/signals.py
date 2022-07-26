from django.db.models.signals import post_save
from django.dispatch import receiver

from ecommapi.models import Address, Cart

from django.contrib.auth import get_user_model


User = get_user_model()


# ADDRESS-------SIGNALS
@receiver(post_save, sender = User)
def create_address(sender, instance, created, **kwargs):
    if created:
        Address.objects.create(user_id=instance)


@receiver(post_save, sender= User)
def save_address(sender, instance, **kwargs):
    instance.address.save()




# CART-------SIGNALS
@receiver(post_save, sender = User)
def create_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)


@receiver(post_save, sender= User)
def save_cart(sender, instance, **kwargs):
    instance.address.save()