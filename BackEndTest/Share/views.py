from rest_framework import viewsets,mixins
from Powtoon import serializers
from Share import models
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

        
class SharePowtoonViewSet(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.PowtoonSerializer

    def get_queryset(self):
        queryset =  models.Powtoon.objects.filter(connection__in = [self.request.user])
        return queryset

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
