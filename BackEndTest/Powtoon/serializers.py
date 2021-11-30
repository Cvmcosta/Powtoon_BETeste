from rest_framework import serializers
from Powtoon import models
from django.contrib.auth.models import User

class PowtoonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Powtoon
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
