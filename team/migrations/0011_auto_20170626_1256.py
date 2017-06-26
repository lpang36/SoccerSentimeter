# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-26 16:56
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0010_auto_20170626_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='volume',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='volumeList',
            field=models.CharField(default='', max_length=500, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]