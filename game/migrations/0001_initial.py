# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-18 01:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='1+', to='team.Team')),
                ('team2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='2+', to='team.Team')),
            ],
        ),
    ]
