# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-08 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0004_auto_20170107_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserve',
            name='userid',
        ),
        migrations.AddField(
            model_name='reserve',
            name='user',
            field=models.CharField(default='Bob', max_length=100),
        ),
    ]
