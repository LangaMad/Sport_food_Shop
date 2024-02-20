from django.urls import path,include
from .api_views import *



urlpatterns = [
    path('product/', ProductListCreateAPIView.as_view()),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view()),
    path('product/<int:pk>/', ProductRetrieveDestroyAPIView.as_view()),
    path('product/<int:pk>/', ProductRetrieveCreateAPIView.as_view()),
    path('product/<int:pk>/', ProductRetriveDestroyUpdateAPIView.as_view()),
    path('product/', ProductListAPIView.as_view()),
    path('product/', ProductCreateAPIView.as_view()),
    ]






# urlpatterns = [
#     path('product/', ProductListAPIView.as_view()),
#     path('product/<int:pk>/', ProductRetrieveAPIView.as_view()),
#     path('product/update/', ProductUpdateAPIView.as_view()),
#     path('product/update/<int:pk>/', ProductUpdateAPIView.as_view()),
#     path('category/', CategoryListAPIView.as_view()),
#     path('category/<int:pk>/', CategoryListAPIView.as_view()),
#     path('subcategory/', SubCategoryListAPIView.as_view()),
#     path('subcategory/<int:pk>/', SubCategoryListAPIView.as_view()),
#     path('product/create/',ProductCreateAPIView.as_view()),
#     path('product/delete/<int:pk>/', ProductDestroyAPIView.as_view()),
#     path('subcategory/create/', SubCategoryCreateAPIView.as_view()),
#     path('subcategory/delete/<int:pk>/', SubCategoryDestroyAPIView.as_view()),
#     ]
