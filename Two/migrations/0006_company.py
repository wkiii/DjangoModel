# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-27 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Two', '0005_students_bill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=32)),
                ('girls_num', models.IntegerField()),
                ('boys_num', models.IntegerField()),
            ],
        ),
    ]