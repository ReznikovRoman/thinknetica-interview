from django.db.models import QuerySet

from datetime import datetime, timedelta

from products import models as product_models


def get_latest_products(n_latest: int = 3) -> QuerySet[product_models.Product]:
    return product_models.Product.objects. \
               filter(created_at__gte=datetime.today() - timedelta(days=14)).  \
               order_by('-created_at')[:n_latest]
