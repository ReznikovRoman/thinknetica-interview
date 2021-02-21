from django.db import models

from accounts import models as account_models


class CartManager(models.Manager):
    def get_queryset(self):
        base_queryset = super(CartManager, self).get_queryset()
        qs = base_queryset.annotate(
            total_price=models.Sum('products__price')
        )
        return qs


class Cart(models.Model):
    customer = models.OneToOneField(account_models.CustomUser, verbose_name="Customer's cart", on_delete=models.CASCADE)

    objects = CartManager()

    def cart_total_price(self):
        print(self.total_price)

    def __str__(self):
        return f"Cart for {self.customer}"







