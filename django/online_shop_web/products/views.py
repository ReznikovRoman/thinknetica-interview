from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from braces.views import GroupRequiredMixin

from . import models
from . import forms


class ShowProducts(generic.ListView):
    model = models.Product
    paginate_by = 6


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







