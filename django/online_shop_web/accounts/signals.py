from django.db.models.signals import post_save
from django.dispatch import receiver

from . import models as account_models
from cart import models as cart_models


@receiver(post_save, sender=account_models.CustomUser)
def assign_cart(sender, instance: account_models.CustomUser, created, **kwargs):
    if created:
        cart_models.Cart.objects.create(
            customer=instance
        )




