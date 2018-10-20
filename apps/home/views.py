from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')


def product(request):
    return render(request, 'main/product_detail.html')
