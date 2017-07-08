import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Sentimeter.settings")
import django
django.setup()
from team.models import *
from tweet.models import *

tweets = Tweet.objects.all()
for tweet in tweets:
	tweet.delete()

teams = Team.objects.all()
for team in teams:
	team.score = 0
	team.scoreList = ''
	team.save()

players = Player.objects.all()
for player in players:
	player.score = 0
	player.lastScore = 0
	player.save()