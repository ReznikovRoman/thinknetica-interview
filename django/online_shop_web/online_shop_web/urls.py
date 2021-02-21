from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='home-page'),
    path('checkout-success/', views.checkout_success, name='checkout-success'),

    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('products/', include('products.urls', namespace='products')),

    path('cart/', include('cart.urls', namespace='cart')),
]

urlpatterns += (
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)

handler404 = 'online_shop_web.views.error_404_view'
handler500 = 'online_shop_web.views.error_500_view'
handler403 = 'online_shop_web.views.error_403_view'
handler400 = 'online_shop_web.views.error_400_view'

