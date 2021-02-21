from django.contrib import admin
from django.db import models

from . import models as cart_models


class CartAdmin(admin.ModelAdmin):
    list_display = ('customer', 'get_products', 'total_price')
    readonly_fields = ('get_products', 'total_price')

    def get_queryset(self, request):
        qs = super(CartAdmin, self).get_queryset(request)
        qs = qs.annotate(
            _total_price=models.Sum('products__price'),
        )
        return qs

    def total_price(self, obj):
        return obj.total_price
    total_price.admin_order_field = '_total_price'

    def get_products(self, obj: cart_models.Cart):
        return "; ".join([f"{product.name}-{product.price}" for product in obj.products.all()])
    get_products.short_description = 'products in the cart'


admin.site.register(cart_models.Cart, CartAdmin)

