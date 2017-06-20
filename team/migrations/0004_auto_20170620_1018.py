# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-20 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_auto_20170618_1531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='name',
            new_name='lastName',
        ),
        migrations.AddField(
            model_name='player',
            name='firstName',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
