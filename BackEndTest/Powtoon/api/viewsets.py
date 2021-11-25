import uuid
from rest_framework import viewsets,mixins,permissions
from Powtoon.api import serializers
from Powtoon import models
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.db.models import Q
from Powtoon.api.permissions import IsOwner
from django.shortcuts import render, get_object_or_404
from Powtoon.models import Powtoon


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
        if True:
            queryset = models.Powtoon.objects.filter(Q(owner = self.request.user)|Q(connection__in = [self.request.user]))            
            
        else:
            queryset =  models.Powtoon.objects.all()
        return queryset          

class SharedPowtoonViewSet(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):

    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.PowtoonSerializer

    def get_queryset(self):
        queryset =  models.Powtoon.objects.filter(connection__in = [self.request.user])
        return queryset
    
class SharePowtoonViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    serializer_class = serializers.sharePowtoon
    
 