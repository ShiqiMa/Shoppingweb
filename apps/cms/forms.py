from apps.forms import FormMixin
from django import forms
from apps.home.models import ProductCategory, Products


class WriteProductsForm(forms.ModelForm, FormMixin):
    category = forms.IntegerField()
    class Meta:
        model = Products
        exclude = ['category']


class EditProductsForm(forms.ModelForm, FormMixin):
    category = forms.IntegerField()
    pk = forms.IntegerField()
    class Meta:
        model = Products
        exclude = ['category']


class EditProductsCategoryForm(forms.Form):
    pk = forms.IntegerField(error_messages={"required": "必须传入分类的id"})
    name = forms.CharField(max_length=100)