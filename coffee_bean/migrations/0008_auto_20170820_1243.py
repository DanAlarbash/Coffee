# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-20 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_bean', '0007_auto_20170820_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='powder',
            field=models.ManyToManyField(blank=True, null=True, to='coffee_bean.Powder'),
        ),
        migrations.AlterField(
            model_name='coffee',
            name='syrup',
            field=models.ManyToManyField(blank=True, null=True, to='coffee_bean.Syrup'),
        ),
    ]
