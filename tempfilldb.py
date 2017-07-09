#!/usr/bin/python2.7

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Sentimeter.settings")
import django
django.setup()
from team.models import Team

teams = Team.objects.all()
for team in teams:
    #team.scoreList = team.scoreList[:len(team.scoreList)-1]
    strs = team.scoreList.split(',')
    team.scoreList = team.scoreList+strs[len(strs)-2]+',';
    team.save()