from django.urls import path
from .views import *



urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('about/', views.about, name='about'),
    # path('shop/',  views.shop, name='shop'),
    # path('contact/', views.contact, name='contact'),
    # path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
