# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-24 13:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0007_auto_20170624_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='team.Team'),
        ),
    ]
