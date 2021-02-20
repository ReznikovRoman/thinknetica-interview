from django.db import models
from django.core.validators import MinValueValidator
from django.shortcuts import reverse


class Product(models.Model):
    name = models.CharField(verbose_name="Product's name", max_length=255)
    price = models.IntegerField(
        verbose_name="Product's price",
        validators=[
            MinValueValidator(1),
        ]
    )

    def get_absolute_url(self):
        return reverse('products:product-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"Product: {self.name} - {self.price}"










