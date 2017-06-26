from urllib2 import Request, urlopen, URLError
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

CONSUMER_KEY = "gqsJ6CliVLM46nOFsAn71EFjT"
CONSUMER_SECRET = "EmwVMq4ef73YSx3aP357j36EgtwH5MwnKh2FAV53bGFCAA0r7j"
ACCESS_KEY = "3329651637-fd7leHwH9jHc5XOzmaDQFz27i0WqMpAtkxWNlva"
ACCESS_SECRET = "3MIv0kokV8xfRjRpGzXpERdF4kIfLs57Jo12xUvY0KLy3"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

currentTeam = Team.objects.first()

def getTweets ( str ):
	url = "https://api.twitter.com/1.1/search/tweets.json?q="+urllib.parse.urlencode(str) #find a way to limit search results
	response, data = client.request(url)
	return json.loads(data)

def analyzeTweetSentiment ( tweet ):
	blob = TextBlob(tweet['text'])
	return blob.sentiment.polarity

def createTweet ( tweet )
	newTweet = Tweet.objects.create(link=tweet['id_str'],team=currentTeam,date=tweet['created_at']) #parse this date properly with datetime
	newTweet.score = analyzeTweetSentiment(tweet)
	newTweet.latitude = tweet['coordinates']['coordinates'][0]
	newTweet.longitude = tweet['coordinates']['coordinates'][1]
	newTweet.save()
	return newTweet.score
	
teams = Team.objects.all()
for thisTeam in teams:
	currentTeam = thisTeam
	data = getTweets(thisTeam.longName)
	teamlist = []
	for tweet in data:
		teamlist.append(createTweet(tweet))
	thisTeam.score = round(sum(teamlist)/len(teamlist))
	thisTeam.scoreList = thisTeam.scoreList+str(thisTeam.score)+','
	thisTeam.save()
	players = Player.objects.filter(team=thisTeam)
	for thisPlayer in players:
		playerlist = []
		data = getTweets(thisPlayer.firstName+" "+thisPlayer.lastName)
		for tweet in data:
			playerlist.append(createTweet(tweet))
		thisPlayer.lastScore = thisPlayer.score
		thisPlayer.score = round(sum(playerlist)/len(playerlist))
		thisPlayer.save()