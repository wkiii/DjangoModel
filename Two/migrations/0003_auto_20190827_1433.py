# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-27 14:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Two', '0002_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='time',
            new_name='o_time',
        ),
    ]