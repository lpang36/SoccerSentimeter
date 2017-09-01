import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Sentimeter.settings")
import django
django.setup()
from team.models import *
# from tweet.models import *
# from game.models import *

file = open("transfers.txt","r")
inflag = True
for line in file:
    words = line.replace("\n","").split(" ")
    if words[0]=="in":
        inflag = True
    elif words[0]=="out":
        inflag = False
    else:
        try:
            team = Team.objects.get(name=words[0])
            lastname = words[len(words)-1]
            firstname = ''
            if len(words)==3:
                firstname = words[1]
            if inflag:
                try:
                    player = Player.objects.get(lastName=lastname,firstName=firstname,team=team)
                except:
                    player = Player.objects.create(lastName=lastname,firstName=firstname,team=team)
                    player.save()
            else:
                try:
                    if firstname=='':
                        player = Player.objects.get(lastName=lastname,team=team)
                    else:
                        player = Player.objects.get(lastName=lastname,firstName=firstname,team=team)
                    player.delete()
                except:
                    pass
        except:
            pass