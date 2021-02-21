from django.db import models
from django.core.validators import MinValueValidator
from django.shortcuts import reverse

from cart import models as cart_models


class Product(models.Model):
    cart = models.ManyToManyField(cart_models.Cart, related_name='products', blank=True)
    name = models.CharField(verbose_name="Product's name", max_length=255)
    price = models.IntegerField(
        verbose_name="Product's price",
        validators=[
            MinValueValidator(1),
        ]
    )
    created_at = models.DateTimeField(verbose_name="date of product's creation", auto_now_add=True)

    def get_absolute_url(self):
        return reverse('products:product-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"Product: {self.name} - {self.price}"










