from django.urls import path,include
from .api_views import *


urlpatterns = [
    path('product/', ProductAPIView.as_view()),
    path('product/<int:pk>/', ProductAPIView.as_view()),
    ]
