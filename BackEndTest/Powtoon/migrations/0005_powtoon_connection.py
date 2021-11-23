# Generated by Django 3.2.9 on 2021-11-23 15:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Powtoon', '0004_alter_powtoon_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='powtoon',
            name='connection',
            field=models.ManyToManyField(related_name='connection', to=settings.AUTH_USER_MODEL),
        ),
    ]