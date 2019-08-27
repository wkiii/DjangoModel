# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-27 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Two', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=16, unique=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]