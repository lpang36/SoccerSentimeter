from django.shortcuts import render

# Create your views here.

def game(request,teamName1,teamName2):
    team1 = Team.objects.filter(name=teamName1).first()
    team2 = Team.objects.filter(name=teamName2).first()
    tweets1 = Tweet.objects.filter(team=team1)
    tweets2 = Tweet.objects.filter(team=team2)
    return render(request,'game/game.html',{'team1': team1,'team2': team2,'tweets1': tweets1,'tweets2': tweets2})
