# Generated by Django 3.2.8 on 2021-11-01 04:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_book_ctime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ctime',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 13, 55, 18, 439605)),
        ),
    ]