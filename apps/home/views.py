from django.shortcuts import render
from .models import Products, ProductCategory

def index(request):
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