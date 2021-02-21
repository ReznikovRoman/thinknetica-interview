from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models as cart_models
from .services import (get_cart_by_customer, get_product_by_pk)


class ShowCart(LoginRequiredMixin, generic.DetailView):
    model = cart_models.Cart

    def get_object(self, queryset=None):
        return get_cart_by_customer(self.request.user)


class AddProduct(LoginRequiredMixin, generic.TemplateView):
    def get(self, request, *args, **kwargs):
        get_cart_by_customer(self.request.user). \
            products.add(get_product_by_pk(kwargs['product_pk']))

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class RemoveProduct(LoginRequiredMixin, generic.TemplateView):
    def get(self, request, *args, **kwargs):
        get_cart_by_customer(self.request.user). \
            products.remove(get_product_by_pk(kwargs['product_pk']))

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class OrderCheckout(LoginRequiredMixin, generic.TemplateView):
    def get(self, request, *args, **kwargs):
        get_cart_by_customer(self.request.user). \
            products.clear()

        return HttpResponseRedirect(reverse('checkout-success'))
