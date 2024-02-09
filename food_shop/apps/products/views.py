from django.shortcuts import render
from .models import *

from django.views.generic import TemplateView,ListView,DetailView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    queryset = Product.objects.all()
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'product_detail.html'
    context_object_name = 'product'

class CategoryListView(ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = 'category_list.html'
    context_object_name = 'categories'



# class AboutView(TemplateView):
#     template_name = 'about.html'
#
# class ShopView(TemplateView):
#     template_name = 'shop.html'
#
# class ContactView(TemplateView):
#     template_name = 'contact.html'
#

