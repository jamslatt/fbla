# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-02 22:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_delete_generate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='hire_date',
        ),
    ]
