# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-20 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_bean', '0008_auto_20170820_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
    ]
