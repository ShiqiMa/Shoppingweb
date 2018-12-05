from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from apps.home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('manage/', admin.site.urls),
    path('product/', include('apps.home.urls')),
    path('admin/', include('apps.cms.urls')),
    path('account/', include("apps.shoppingweb_auth.urls")),
    path('cart/', include('apps.cart.urls', namespace='cart')),
    path('orders/', include('apps.orders.urls', namespace='orders')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment/', include('apps.payment.urls', namespace='payment')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
