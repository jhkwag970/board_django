# Generated by Django 3.2.8 on 2021-11-04 03:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='follow',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
