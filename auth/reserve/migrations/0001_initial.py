# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-07 18:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.CharField(choices=[('MovieLovers', 'Movie Lovers'), ('FamilyFun', 'Faily Fun')], max_length=100)),
                ('price', models.IntegerField(default=50)),
                ('comments', models.TextField(max_length=1000)),
                ('time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
