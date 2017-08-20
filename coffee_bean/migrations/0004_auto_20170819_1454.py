# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-19 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_bean', '0003_coffee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffee',
            name='powder',
        ),
        migrations.AddField(
            model_name='coffee',
            name='powder',
            field=models.ManyToManyField(to='coffee_bean.Powder'),
        ),
        migrations.RemoveField(
            model_name='coffee',
            name='syrup',
        ),
        migrations.AddField(
            model_name='coffee',
            name='syrup',
            field=models.ManyToManyField(to='coffee_bean.Syrup'),
        ),
    ]
