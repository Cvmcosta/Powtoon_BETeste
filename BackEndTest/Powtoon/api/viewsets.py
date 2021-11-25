
from rest_framework import viewsets,mixins,permissions
from Powtoon.api import serializers
from Powtoon import models
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.db.models import Q
from Powtoon.api.permissions import IsOwner
from django.shortcuts import get_object_or_404
from Powtoon.models import Powtoon
# from rest_framework.decorators import action
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
    #try this in another moment
    # @action(detail=True, methods=['post'], name='Share')          
    # def share(self,request,pk=None):    
    #     powtoon = get_object_or_404(models.Powtoon, id = uuid(self.kwargs['pk']))
    #     user = get_object_or_404(User, id = self.validated_data['userid'])

class SharedPowtoonViewSet(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):

    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.PowtoonSerializer

    def get_queryset(self):
        queryset =  models.Powtoon.objects.filter(connection__in = [self.request.user])
        return queryset
    
class SharePowtoonViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)    

    def create(self,view):
        powtoon = get_object_or_404(models.Powtoon, id = view.data['powtoonid'])
        user = get_object_or_404(User, id = view.data['userid'])
        if "share.share_powtoon" in self.request.user.get_user_permissions() or powtoon.owner == self.request.user :
            powtoon.connection.add(user)
            powtoon.save()
            serializedPowtoon = serializers.PowtoonSerializer(powtoon)
            return Response(serializedPowtoon.data)
        else :
            raise PermissionDenied({"message":"You don't have permission to acess this object"})
    
 