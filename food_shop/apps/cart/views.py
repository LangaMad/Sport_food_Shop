from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from ..products.models import Product
from .cart import Cart
# Create your views here.


class CartView(TemplateView):
    template_name = 'cart.html'

def add_to_cart(request, id):
    cart = Cart(request)
    product = Product.objects.get(pk=id)
    cart.add(product)
    return redirect('cart')
def remove_from_cart(request, id):
    cart = Cart(request)
    product = Product.objects.get(pk=id)
    cart.remove(product)
    return redirect('cart')
def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart')





