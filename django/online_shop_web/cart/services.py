from . import models as cart_models
from products import models as product_models
from accounts import models as account_models


def get_cart_by_customer(customer: account_models.CustomUser):
    return cart_models.Cart.objects.get(customer=customer)


def get_product_by_pk(product_pk: int):
    return product_models.Product.objects.get(pk=int(product_pk))





