
from django.contrib import admin
from django.urls import path, include
from .views import PurchaseViewSet, ItemViewSet, PurchaseUserViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'purchases', PurchaseViewSet)
router.register(r'items', ItemViewSet)
router.register(r'mypurchases', PurchaseUserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]