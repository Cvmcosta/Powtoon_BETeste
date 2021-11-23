from rest_framework import viewsets
from Powtoon.api import serializers
from Powtoon import models

class PowtoonViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PowtoonSerializer
    queryset = models.Powtoon.objects.all()