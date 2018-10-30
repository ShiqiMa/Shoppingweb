from django.shortcuts import render
from .models import Products, ProductCategory
from django.conf import settings
from utils import restful
from .serializers import ProductsCategorySerializer, ProductsSerializer
from django.http import Http404


def index(request):
    count = settings.ONE_PAGE_NEWS_COUNT
    newses = Products.objects.select_related('category').all()[0:count]
    categories = ProductCategory.objects.all()
    context = {
        'productses': productses,
        'categories': categories,
    }
    return render(request, 'main/index.html')


def product(request):
    return render(request, 'main/product_detail.html')


def single_product(request, products_id):
    try:
        product = Products.objects.select_related('category').get(pk=products_id)
        context = {
            'product': product
        }
        return render(request, 'main/single_product.html', context=context)
    except News.DoesNotExist:
        raise Http404