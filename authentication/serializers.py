from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=65, min_length=8, write_only=True)
    email=serializers.EmailField(max_length=255, min_length=2)
    first_name=serializers.CharField(max_length=255, min_length=2)
    last_name=serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']