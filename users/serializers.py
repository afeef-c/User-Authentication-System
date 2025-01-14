
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Log,CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','first_name', 'last_name', 'username', 'is_staff']

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'

