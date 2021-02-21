from django.db.models import QuerySet, Q

from .models import Product


def get_search_results(name_query: str) -> QuerySet[Product]:
    return Product.objects.filter(
        Q(name__icontains=name_query))

