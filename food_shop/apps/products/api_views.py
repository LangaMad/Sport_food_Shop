# from rest_framework import serializers
# from rest_framework.response import Response
from rest_framework.generics import ListAPIView, UpdateAPIView,  RetrieveAPIView, CreateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import *
from .serializers import ProductSerializer,  CategorySerializer, SubCategorySerializer
from .custom_api import *
from rest_framework.permissions import (IsAuthenticated, AllowAny,
                            IsAdminUser, IsAuthenticatedOrReadOnly)
from .permissions import IsOwnerOrReadOnly, IsAdminOrIsOwner


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

class ProductViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class ProductRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveCreateAPIView(RetrieveCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetriveDestroyUpdateAPIView(RetrieveDestroyUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




























#
# class ProductListAPIView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
# class ProductCreateAPIView(CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class ProductUpdateAPIView(UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
# class ProductRetrieveAPIView(RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class ProductDestroyAPIView(DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class CategoryListAPIView(ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
# class SubCategoryListAPIView(ListAPIView):
#     queryset = SubCategory.objects.all()
#     serializer_class = SubCategorySerializer
#
#
# class SubCategoryCreateAPIView(CreateAPIView):
#     queryset = SubCategory.objects.all()
#     serializer_class = SubCategorySerializer
#
#
# class SubCategoryDestroyAPIView(DestroyAPIView):
#     queryset = SubCategory.objects.all()
#     serializer_class = SubCategorySerializer
#
#
#
#
#
