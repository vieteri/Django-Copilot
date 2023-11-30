from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import viewsets

""" Create user view """
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = serializers.ModelSerializer
