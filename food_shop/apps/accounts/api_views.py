from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from .models import *
from .serializers import UserSerializer


class UserAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer