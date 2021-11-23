from rest_framework import serializers
from Powtoon import models

class PowtoonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Powtoon
        fields = '__all__'