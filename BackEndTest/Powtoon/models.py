from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User


# Create your models here.
class Powtoon(models.Model):
    id = models.UUIDField(primary_key = True, default =uuid4 ,editable = False)
    name = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    connection = models.ManyToManyField(User, related_name = 'connection',blank=True)

