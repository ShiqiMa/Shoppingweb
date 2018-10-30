from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.product, name='product'),
    path('<int:products_id>/', views.single_product, name='single_product')
]