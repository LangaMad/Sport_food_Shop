from django.shortcuts import render
from .models import *

from django.views.generic import TemplateView,ListView,DetailView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class ProductDetailView(DetailView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'product_detail.html'
    context_object_name = 'product'

class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'product_list.html'
    context_object_name = 'products'




# class AboutView(TemplateView):
#     template_name = 'about.html'
#
# class ShopView(TemplateView):
#     template_name = 'shop.html'
#
# class ContactView(TemplateView):
#     template_name = 'contact.html'
#

