from django.urls import path
from . import views

app_name = 'shoppingweb_auth'

urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('register/',views.register,name='register'),
    path('cache/',views.cache_test,name='cache'),
]