from django.urls import path

from . import views


app_name = 'cart'

urlpatterns = [
    path('', views.ShowCart.as_view(), name='cart-detail'),
    path('<int:product_pk>/add/', views.AddProduct.as_view(), name='new-product'),
    path('<int:product_pk>/remove/', views.RemoveProduct.as_view(), name='product-remove'),
    path('checkout/', views.OrderCheckout.as_view(), name='order-checkout'),
]

