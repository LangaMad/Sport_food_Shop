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


