# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-24 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_team_imagepath'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='lastScore',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
