# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-12 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0009_user_power'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='power',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
