from django.shortcuts import render
from .models import Team
from tweet.models import Tweet

# Create your views here.

def team(request,teamName):
    thisTeam = Team.objects.filter(name=teamName).first()
    tweets = Tweet.objects.filter(team=thisTeam)
    return render(request,'team/team.html',{'team': thisTeam,'tweets': tweets})
