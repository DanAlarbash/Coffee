# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-23 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20170823_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='delivery_total',
            field=models.DecimalField(decimal_places=3, default=2.0, max_digits=6),
        ),
    ]