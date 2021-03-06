from django.shortcuts import render
from team.models import Team
from tweet.models import Tweet
from team.models import Player

# Create your views here.

def game(request,teamName1,teamName2):
    team1 = Team.objects.filter(name=teamName1).first()
    team2 = Team.objects.filter(name=teamName2).first()
    tweets1 = Tweet.objects.filter(team=team1).exclude(latitude=None)
    tweets2 = Tweet.objects.filter(team=team2).exclude(latitude=None)
    players1 = Player.objects.filter(team=team1).order_by('-score')
    players2 = Player.objects.filter(team=team2).order_by('-score')
    return render(request,'game/game.html',{'team1': team1,'team2': team2,'tweets1': tweets1,'tweets2': tweets2,'players1': players1,'players2': players2})
