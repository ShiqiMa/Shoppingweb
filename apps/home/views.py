from django.shortcuts import render
from .models import Products, ProductCategory
from django.conf import settings
from utils import restful
from .serializers import ProductsCategorySerializer, ProductsSerializer
from apps.cart.forms import CartAddProductForm
from django.http import Http404


def index(request):
    count = settings.ONE_PAGE_PRODUCTS_COUNT
    productses = Products.objects.select_related('category').all()[0:count]
    categories = ProductCategory.objects.all()
    context = {
        'productses': productses,
        'categories': categories,
    }
    return render(request, 'main/index.html', context=context)


def products(request):
    count = settings.ONE_PAGE_PRODUCTS_COUNT
    productses = Products.objects.select_related('category').all()[0:count]
    categories = ProductCategory.objects.all()
    cart_product_form = CartAddProductForm()
    context = {
        'productses': productses,
        'categories': categories,
        'cart_product_form': cart_product_form
    }
    return render(request, 'main/product_detail.html', context=context)


def products_list(request):
    page = int(request.GET.get('p', 1))
    category_id = int(request.GET.get('category_id', 0))
    start = (page-1)*settings.ONE_PAGE_PRODUCTS_COUNT
    end = start + settings.ONE_PAGE_PRODUCTS_COUNT

    if category_id == 0:
        productses = Products.objects.select_related('category').all()[start:end]
    else:
        productses = Products.objects.filter(category__id=category_id)[start:end]
    serializer = ProductsSerializer(productses, many=True)
    data = serializer.data
    return restful.result(data=data)


def shoppingcart_list(request):
    name = request.GET.get('name')
    price = request.GET.get('price')
    product_item = Products.objects.filter(name=name, price=price)
    serializer = ProductsSerializer(product_item)
    data = serializer.data
    return restful.result(data=data)



def single_product(request, products_id):
    try:
        product = Products.objects.select_related('category').get(pk=products_id)
        categories = ProductCategory.objects.all()
        cart_product_form = CartAddProductForm()
        context = {
            'product': product,
            'categories': categories,
            'cart_product_form': cart_product_form
        }
        return render(request, 'main/single_product.html', context=context)
    except Products.DoesNotExist:
        raise Http404