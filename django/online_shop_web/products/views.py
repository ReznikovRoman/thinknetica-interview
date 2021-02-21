from django.views import generic
from django.urls import reverse_lazy

from braces.views import GroupRequiredMixin

from . import models
from . import forms
from .services import get_search_results


class ShowProducts(generic.ListView):
    model = models.Product
    paginate_by = 6
    ordering = 'id'


class ShowProductPage(generic.DetailView):
    model = models.Product
    context_object_name = 'product'


class CreateProduct(GroupRequiredMixin,
                    generic.CreateView):
    group_required = 'managers'
    model = models.Product
    form_class = forms.ProductForm


class EditProductDetails(GroupRequiredMixin,
                         generic.UpdateView):
    group_required = 'managers'
    model = models.Product
    form_class = forms.ProductForm


class DeleteProduct(GroupRequiredMixin,
                    generic.DeleteView):
    group_required = 'managers'
    model = models.Product
    success_url = reverse_lazy('products:product-list')


class ProductSearchResults(generic.ListView):
    model = models.Product
    template_name = 'products/product_search_results.html'
    context_object_name = 'product_list'
    paginate_by = 6

    def get_queryset(self):
        return get_search_results(self.request.GET.get('q'))



