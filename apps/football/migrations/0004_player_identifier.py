# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-13 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0003_player_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='identifier',
            field=models.CharField(default='basic', max_length=10, null=True),
        ),
    ]