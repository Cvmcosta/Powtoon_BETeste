from rest_framework import viewsets,mixins,permissions
from Powtoon import serializers
from Powtoon import models
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.db.models import Q
from Powtoon.permissions import IsOwner
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

class PowtoonViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,IsOwner)
    serializer_class = serializers.PowtoonSerializer
    def get_serializer_context(self):
        if not (self.request.method in permissions.SAFE_METHODS):
            self.request.data.update({
                'owner':self.request.user.id
            })        
        return super().get_serializer_context()
    def get_queryset(self):
        if "powtoon.get_all" in self.request.user.get_user_permissions() :
            queryset =  models.Powtoon.objects.all()            
        else:
            queryset = models.Powtoon.objects.filter(Q(owner = self.request.user)|Q(connection__in = [self.request.user]))             
        return queryset
   
 