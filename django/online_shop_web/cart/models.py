from django.db import models

from accounts import models as account_models


class CartManager(models.Manager):
    def get_queryset(self):
        qs = super(CartManager, self).get_queryset()
        return qs.annotate(total_price=models.Sum('products__price'))


class Cart(models.Model):
    customer = models.OneToOneField(account_models.CustomUser, verbose_name="Customer's cart", on_delete=models.CASCADE)

    objects = CartManager()

    def __str__(self):
        return f"Cart for {self.customer}"







