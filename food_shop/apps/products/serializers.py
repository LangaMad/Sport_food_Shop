from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name','slug']
        read_only_fields = ['id']


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = SubCategory
        fields = ['name','slug','category']
        read_only_fields = ['id']



class ProductSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer()
    class Meta:
        model = Product
        fields = ['name','description','price','subcategory','image']
        read_only_fields = ['id','created']

