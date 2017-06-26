import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Sentimeter.settings")
import django
django.setup()
from team.models import *
from tweet.models import *

myteam = Team.objects.filter(name='LIV').first()
players = Player.objects.filter(team=myteam)
tweets = Tweet.objects.filter(team=myteam)

for tweet in tweets:
	tweet.delete()

myteam.score = 0
myteam.scoreList = ''
myteam.save()

for player in players:
	player.score = 0
	player.lastScore = 0
	player.save()