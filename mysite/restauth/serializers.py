""" Create serializers for django rest-auth """
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_auth.models import Token

""" create user serializer """
class UserSerializer(serializers.ModelSerializer):
    """ a serializer for the User model """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff')

