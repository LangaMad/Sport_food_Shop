from django.urls import path
from .views import *

from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView


app_name = 'accounts'


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('logout/', Logout.as_view(), name='logout'),
]
