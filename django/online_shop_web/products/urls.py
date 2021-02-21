from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ShowProducts.as_view(), name='product-list'),
    path('<int:pk>/', views.ShowProductPage.as_view(), name='product-detail'),

    path('new/', views.CreateProduct.as_view(), name='product-new'),
    path('edit/<int:pk>/', views.EditProductDetails.as_view(), name='product-edit'),
    path('remove/<int:pk>/', views.DeleteProduct.as_view(), name='product-remove'),

    path('search-results/', views.ProductSearchResults.as_view(), name='products-search-results')
]

