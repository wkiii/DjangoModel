# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-26 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20190826_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='p_age',
            field=models.IntegerField(db_column='age'),
        ),
        migrations.AlterField(
            model_name='person',
            name='p_sex',
            field=models.BooleanField(db_column='sex'),
        ),
    ]
