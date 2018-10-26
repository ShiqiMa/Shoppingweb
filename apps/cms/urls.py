from django.urls import path
from . import views


app_name = 'cms'

urlpatterns = [
    path('', views.index, name='index'),
    path('write_products/', views.WriteProductsView.as_view(), name='write_products'),
    path('edit_products/', views.EditProductsView.as_view(), name='edit_products'),
    path('products_category/', views.products_category, name='products_category'),
    path('add_products_category/', views.add_products_category, name='add_products_category'),
    path('edit_products_category/', views.edit_products_category, name='edit_products_category'),
    path('delete_products_category/', views.delete_products_category, name='delete_products_category'),
    path('products_list/', views.ProductsListView.as_view(), name='products_list'),
    path('edit_products/', views.EditProductsView.as_view(), name='edit_products'),
    path('delete_products/', views.delete_products, name='delete_products'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('delete_products/', views.delete_products, name='delete_products'),
]
