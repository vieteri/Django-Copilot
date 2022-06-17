"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import UserViewSet
from .models import FacebookLogin
from rest_framework import routers




urlpatterns = [
    #path('users/', include(router.urls)),
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    # facebook rest-auth
    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
]
