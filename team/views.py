from django.shortcuts import render
from .models import Team
from tweet.models import Tweet
from .models import Player

# Create your views here.

def team(request,teamName):
    thisTeam = Team.objects.filter(name=teamName).first()
    tweets = Tweet.objects.filter(team=thisTeam).exclude(latitude=None)
    players = Player.objects.filter(team=thisTeam).order_by('-score')
    return render(request,'team/team.html',{'team': thisTeam,'tweets': tweets,'players': players})
