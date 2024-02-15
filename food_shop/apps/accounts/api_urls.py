from django.urls import path,include
from .api_views import *


urlpatterns = [
    path('account/', UserAPIView.as_view()),
    path('account/<int:pk>/', UserAPIView.as_view()),
    ]