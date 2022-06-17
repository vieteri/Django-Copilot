from django.contrib import admin
from django.urls import path
from .views import index, detail

urlpatterns = [
    path('', index),
    path('<int:item_id>/', detail),
]