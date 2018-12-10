from django.shortcuts import render
from apps.home.models import ProductCategory, Products
from utils import restful
from django.views.generic import View
from .forms import WriteProductsForm, EditProductsForm, EditProductsCategoryForm
from django.views.decorators.http import require_POST, require_GET
from django.core.paginator import Paginator
from urllib import parse
import os
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings

@staff_member_required(login_url='index')
def index(request):
    return render(request, 'admin/index.html')


class WriteProductsView(View):
    def get(self, request):
        categories = ProductCategory.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'admin/write_products.html', context=context)

    def post(self, request):
        form = WriteProductsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            desc = form.cleaned_data.get('desc')
            price = form.cleaned_data.get('price')
            category_id = form.cleaned_data.get('category')
            category = ProductCategory.objects.get(pk=category_id)
            Products.objects.create(name=name, desc=desc, price=price, category=category)
            return restful.ok()
        else:
            return restful.params_error(message=form.get_errors())


class EditProductsView(View):
    def get(self, request):
        products_id = request.GET.get('products_id')
        products = Products.objects.get(pk=products_id)
        context = {
            'products': products,
            'categories': ProductCategory.objects.all()
        }
        return render(request, 'admin/write_products.html', context=context)

    def post(self, request):
        form = EditProductsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            desc = form.cleaned_data.get('desc')
            thumbnail = form.cleaned_data.get('thumbnail')
            price = form.cleaned_data.get('price')
            category_id = form.cleaned_data.get('category')
            category = ProductCategory.objects.get(pk=category_id)
            pk = form.cleaned_data.get('pk')
            Products.objects.filter(pk=pk).update(name=name, desc=desc, thumbnail=thumbnail, price=price, category=category)
            return restful.ok()
        else:
            return restful.params_error(message=form.get_errors())


@require_GET
def products_category(request):
    categories = ProductCategory.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'admin/products_category.html', context=context)


@require_POST
def add_products_category(request):
    name = request.POST.get('name')
    exists = ProductCategory.objects.filter(name=name).exists()
    if not exists:
        ProductCategory.objects.create(name=name)
        return restful.ok()
    else:
        return restful.params_error(message='该分类已经存在！')


@require_POST
def edit_products_category(request):
    form = EditProductsCategoryForm(request.POST)
    if form.is_valid():
        pk = form.cleaned_data.get('pk')
        name = form.cleaned_data.get('name')
        try:
            ProductCategory.objects.filter(pk=pk).update(name=name)
            return restful.ok()
        except:
            return restful.params_error(message='该分类不存在！')
    else:
        return restful.params_error(message=form.get_error())


@require_POST
def delete_products_category(request):
    pk = request.POST.get('pk')
    try:
        ProductCategory.objects.filter(pk=pk).delete()
        return restful.ok()
    except:
        return restful.unauth(message='该分类不存在！')


class ProductsListView(View):
    def get(self, request):
        # request.GET获取出来的都是字符串
        page = int(request.GET.get('p', 1))
        start = request.GET.get('start')
        end = request.GET.get('end')
        name = request.GET.get('name')
        category_id = int(request.GET.get('category', 0) or 0)
        productses = Products.objects.select_related('category').all()
        if name:
            productses = productses.filter(name__icontains=name)
        if category_id:
            productses = productses.filter(category=category_id)

        paginator = Paginator(productses, 2)
        page_obj = paginator.page(page)

        context_data = self.get_pagination_data(paginator, page_obj)

        context = {
            'categories': ProductCategory.objects.all(),
            'productses': page_obj.object_list,
            'page_obj': page_obj,
            'paginator': paginator,
            'start': start,
            'end': end,
            'name': name,
            'category_id': category_id,
            'url_query': '&'+parse.urlencode({
                'start': start or '',
                'end': end or '',
                'name': name or '',
                'category': category_id or ''
            })
        }

        context.update(context_data)

        return render(request, 'admin/products_list.html', context=context)

    def get_pagination_data(self, paginator, page_obj, around_count=2):
        current_page = page_obj.number
        num_pages = paginator.num_pages

        left_has_more = False
        right_has_more = False

        if current_page <= around_count + 2:
            left_pages = range(1, current_page)
        else:
            left_has_more = True
            left_pages = range(current_page - around_count, current_page)

        if current_page >= num_pages - around_count - 1:
            right_pages = range(current_page + 1, num_pages + 1)
        else:
            right_has_more = True
            right_pages = range(current_page + 1, current_page + around_count + 1)

        return {
            'left_pages': left_pages,
            'right_pages': right_pages,
            'current_page': current_page,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'num_pages': num_pages
        }

class EditProductsView(View):
    def get(self, request):
        products_id = request.GET.get('products_id')
        products = Products.objects.get(pk=products_id)
        context = {
            'products': products,
            'categories': ProductCategory.objects.all()
        }
        return render(request, 'admin/write_products.html', context=context)

    def post(self, request):
        form = EditProductsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            desc = form.cleaned_data.get('desc')
            thumbnail = form.cleaned_data.get('thumbnail')
            price = form.cleaned_data.get('price')
            category_id = form.cleaned_data.get('category')
            category = ProductCategory.objects.get(pk=category_id)
            pk = form.cleaned_data.get('pk')
            Products.objects.filter(pk=pk).update(name=name, desc=desc, thumbnail=thumbnail, price=price, category=category)
            return restful.ok()
        else:
            return restful.params_error(message=form.get_errors())

@require_POST
def delete_products(request):
    products_id = request.POST.get('products_id')
    Products.objects.filter(pk=products_id).delete()
    return restful.ok()


def upload_file(request):
    file = request.FILES.get('file')
    name = file.name
    with open(os.path.join(settings.MEDIA_ROOT, name), 'wb') as fp:
        for chunk in file.chunks():
            fp.write(chunk)
    url = request.build_absolute_uri(settings.MEDIA_URL + name)
    return restful.result(data={'url': url})