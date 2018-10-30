from rest_framework import serializers
from .models import ProductCategory, Products
# from apps.shoppingwebauth.serializers import UserSerializer


class ProductsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('id', 'name')

class ProductsSerializer(serializers.ModelSerializer):
    category = ProductsCategorySerializer()
    class Meta:
        model = Products
        fields = ('id', 'name', 'desc', 'thumbnail', 'category', 'price')


