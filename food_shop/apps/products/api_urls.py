from django.urls import path, include

from .api_views import *



urlpatterns = [
    path('product/', ProductListAPIView.as_view()),
    path('product/<int:pk>/', ProductListAPIView.as_view()),
    path('product/update/',ProductUpdateAPIView.as_view()),
    path('product/update/<int:pk>/', ProductUpdateAPIView.as_view()),
]

# CRUD - C - Create, R - Read, U - Update, D - Delete