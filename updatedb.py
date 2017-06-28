#from urllib2 import Request, urlopen, URLError
import oauth2 as oauth
import json
import urllib.parse
import datetime
from textblob import TextBlob
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Sentimeter.settings")
import django
django.setup()
from team.models import *
from tweet.models import *
import random

random.seed()

CONSUMER_KEY = "gqsJ6CliVLM46nOFsAn71EFjT"
CONSUMER_SECRET = "EmwVMq4ef73YSx3aP357j36EgtwH5MwnKh2FAV53bGFCAA0r7j"
ACCESS_KEY = "3329651637-fd7leHwH9jHc5XOzmaDQFz27i0WqMpAtkxWNlva"
ACCESS_SECRET = "3MIv0kokV8xfRjRpGzXpERdF4kIfLs57Jo12xUvY0KLy3"

CONSUMER_KEY2 = "NgaOJeiipvnuyJ0WDV0IobZl3"
CONSUMER_SECRET2 = "U7vd2EzJKT8aEhITwUQrWclZwKFTvQHkAIQRQwqokiJ99L9umb"
ACCESS_KEY2 = "879392004760883200-Qceh7HtHO4rHs8mpEFcQ18HsIXuMrOW"
ACCESS_SECRET2 = "1B589fz5x7XpxkqbBIxgrAKi7PUX2TB9TnNFWAjUwNRbA"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

consumer2 = oauth.Consumer(key=CONSUMER_KEY2, secret=CONSUMER_SECRET2)
access_token2 = oauth.Token(key=ACCESS_KEY2, secret=ACCESS_SECRET2)
client2 = oauth.Client(consumer2, access_token2)

currentTeam = Team.objects.first()

def getTweets ( str ):
	urldict = {
		'q': str,
		'since': currentTeam.date.isoformat(),
		'count': 25,
	}
	url = "https://api.twitter.com/1.1/search/tweets.json?"+urllib.parse.urlencode(urldict) #find a way to limit search results
	if random.random()>0.5:
		response, data = client.request(url)
	else:
		response, data = client2.request(url)
	return json.loads(data)

def analyzeTweetSentiment ( tweet ):
	blob = TextBlob(tweet['text'])
	return blob.sentiment.polarity*100

def createTweet ( tweet ):
	newTweet = Tweet.objects.create(link=tweet['id_str'],team=currentTeam) #parse this date properly with datetime
	datestr1 = tweet['created_at'].split(" ")
	datestr2 = datestr1[3].split(":")
	monthdict = {
		'Jan': 1,
		'Feb': 2,
		'Mar': 3,
		'Apr': 4,
		'May': 5,
		'Jun': 6,
		'Jul': 7,
		'Aug': 8,
		'Sep': 9,
		'Oct': 10,
		'Nov': 11,
		'Dec': 12
	}
	newTweet.date = datetime.datetime(int(datestr1[5]),monthdict[datestr1[1]],int(datestr1[2]),int(datestr2[0]),int(datestr2[1]))
	newTweet.score = analyzeTweetSentiment(tweet)
	if tweet['coordinates'] is not None:
		print("geotagged")
		newTweet.latitude = tweet['coordinates']['coordinates'][0]
		newTweet.longitude = tweet['coordinates']['coordinates'][1]
	newTweet.save()
	return newTweet.score
	
def getAggregateScore ( scorelist ):
	return round(sum(scorelist)/len(scorelist))
	
teams = Team.objects.all()[0:20] #change this to 0
for thisTeam in teams:
	currentTeam = thisTeam
	if currentTeam.name is None or currentTeam.longName is None:
		currentTeam.delete()
		continue
	data = getTweets(thisTeam.longName)
	teamlist = []
	for tweet in data['statuses']:
		teamlist.append(createTweet(tweet))
	if len(teamlist)==0:
		thisTeam.score = 0
	else:
		thisTeam.score = getAggregateScore(teamlist)
	thisTeam.scoreList = thisTeam.scoreList+str(thisTeam.score)+',' #add volume at some point
	thisTeam.date = datetime.date.today()
	thisTeam.save() 
	players = Player.objects.filter(team=thisTeam)
	for thisPlayer in players:
		playerlist = []
		data = getTweets(thisPlayer.firstName+" "+thisPlayer.lastName)
		for tweet in data['statuses']:
			playerlist.append(createTweet(tweet))
		if len(playerlist)==0:
			thisPlayer.score = thisPlayer.lastScore
		else:
			thisPlayer.lastScore = thisPlayer.score
			thisPlayer.score = getAggregateScore(playerlist)
		thisPlayer.volume = len(playerlist)
		thisPlayer.save()
	print(thisTeam.longName)