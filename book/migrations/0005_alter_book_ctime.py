# Generated by Django 3.2.8 on 2021-11-03 04:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_book_ctime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ctime',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 3, 13, 32, 3, 757934)),
        ),
    ]