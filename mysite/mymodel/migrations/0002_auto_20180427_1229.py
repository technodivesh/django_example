# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-27 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymodel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='add_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
