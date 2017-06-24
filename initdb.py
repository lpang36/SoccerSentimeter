import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Sentimeter.settings")
import django
django.setup()
from team.models import *
# from tweet.models import *
# from game.models import *

file = open("initdb.txt","r")
currentTeam = Team.objects.first()
currentPlayer = Player.objects.first()
flag = False
def findColour( str ):
	if str=="red":
		return "ff0000"
	elif str=="blue":
		return "0000ff"
	elif str=="green":
		return "008000"
	elif str=="yellow":
		return "ffff00"
	elif str=="purple":
		return "800080"
	elif str=="black":
		return "000000"
	elif str=="white":
		return "ffffff"
	elif str=="gray" or str=="grey":
		return "808080"
	else:
		return str
for line in file:
	words = line.replace("\n","").split(": ")
	if words[0]=="name":
		if Team.objects.filter(name=words[1]).exists():
			currentTeam = Team.objects.get(name=words[1])
			# flag = True
		else:
			currentTeam = Team.objects.create(name=words[1])
			# flag = False
	if flag:
		continue
	else:
		if words[0]=="longName":
			currentTeam.longName = words[1]
		elif words[0]=="homeColour":
			currentTeam.homeColour = findColour(words[1])
		elif words[0]=="awayColour":
			currentTeam.awayColour = findColour(words[1])
		elif words[0]=="league":
			currentTeam.league = words[1]
		elif words[0]=="nextGame":
			currentTeam.nextGame = Team.objects.get(name=words[1])
		elif words[0]=="imagePath":
			currentTeam.imagePath = words[1]
		elif words[0]=="Player":
			if words[1]=="lastName":
				if Player.objects.filter(lastName=words[2],team=currentTeam).exists():
					currentPlayer = Player.objects.get(lastName=words[2],team=currentTeam)
				else: 
					currentPlayer = Player.objects.create(lastName = words[2],team = currentTeam)
			elif words[1]=="firstName":
				currentPlayer.firstName = words[2]
		currentTeam.save()
		currentPlayer.save()
	
