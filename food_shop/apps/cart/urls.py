from django.urls import path

from .views import *

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/<int:id>/', add_to_cart, name='add'),
    path('remove/<int:id>/', remove_from_cart, name='remove'),
    path('clear/', clear_cart, name='clear'),
]

