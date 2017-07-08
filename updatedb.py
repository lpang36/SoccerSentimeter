#!/usr/bin/python2.7

#from urllib2 import Request, urlopen, URLError
import oauth2 as oauth
import json
import urllib
import datetime
from textblob import TextBlob
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Sentimeter.settings")
import django
django.setup()
from team.models import Team
from team.models import Player
from tweet.models import Tweet
import random
import warnings

def getTweets ( str, obj, client, client2, num ):
	urldict = {
		'q': str,
		'since': obj.date.isoformat(),
		'count': num,
	}
	url = "https://api.twitter.com/1.1/search/tweets.json?"+urllib.urlencode(urldict) #find a way to limit search results
	if random.random()>0.5:
		response, data = client.request(url)
	else:
		response, data = client2.request(url)
	return json.loads(data)

def analyzeTweetSentiment ( tweet ):
	blob = TextBlob(tweet['text'])
	return blob.sentiment.polarity*100

def createTweet ( tweet, obj, flag ):
	newTweet = Tweet.objects.create(link=tweet['id_str'],team=obj) #parse this date properly with datetime
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
	output = analyzeTweetSentiment(tweet)
	newTweet.score = output
	loctag = False
	if tweet['coordinates'] is not None:
		print("geotagged")
		newTweet.latitude = tweet['coordinates']['coordinates'][0]
		newTweet.longitude = tweet['coordinates']['coordinates'][1]
		loctag = True
	if loctag or (flag and random.random()>0.1):
		newTweet.save()
	else:
		newTweet.delete()
	return output

def getAggregateScore ( scorelist ):
	return round(sum(scorelist)/len(scorelist))

def update ( flag ):
	file = open("/home/soccersentimeter/Sentimeter/lastteam.txt","w")
	file2 = None
	if flag:
		file2 = open("/home/soccersentimeter/Sentimeter/lastplayer.txt","w")

	random.seed()

	keyfile = open("/home/soccersentimeter/other/keys.txt","r")
	lines = [line.rstrip('\n') for line in keyfile]

	CONSUMER_KEY = lines[0]
	CONSUMER_SECRET = lines[1]
	ACCESS_KEY = lines[2]
	ACCESS_SECRET = lines[3]

	CONSUMER_KEY2 = lines[4]
	CONSUMER_SECRET2 = lines[5]
	ACCESS_KEY2 = lines[6]
	ACCESS_SECRET2 = lines[7]

	keyfile.close()

	consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
	access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
	client = oauth.Client(consumer, access_token)

	consumer2 = oauth.Consumer(key=CONSUMER_KEY2, secret=CONSUMER_SECRET2)
	access_token2 = oauth.Token(key=ACCESS_KEY2, secret=ACCESS_SECRET2)
	client2 = oauth.Client(consumer2, access_token2)

	teams = Team.objects.all()[0:20] #change this to 0

	for thisTeam in teams:
		if thisTeam.name is None or thisTeam.longName is None:
			thisTeam.delete()
			continue
		numTweets = 100
		if not flag:
			numTweets = 500
		data = getTweets(thisTeam.longName, thisTeam, client, client2, numTweets)
		teamlist = []
		for tweet in data['statuses']:
			teamlist.append(createTweet(tweet, thisTeam, True))
		if len(teamlist)==0:
			thisTeam.score = 0
		else:
			thisTeam.score = getAggregateScore(teamlist)
		thisTeam.scoreList = thisTeam.scoreList+str(thisTeam.score)+',' #add volume at some point
		thisTeam.date = datetime.date.today()
		thisTeam.save()
		if flag:
			players = Player.objects.filter(team=thisTeam)
			for thisPlayer in players:
				playerlist = []
				data = getTweets(thisPlayer.firstName+" "+thisPlayer.lastName, thisPlayer, client, client2, 100)
				for tweet in data['statuses']:
					playerlist.append(createTweet(tweet, thisTeam, False))
				if len(playerlist)==0:
					thisPlayer.score = thisPlayer.lastScore
				else:
					thisPlayer.lastScore = thisPlayer.score
					thisPlayer.score = getAggregateScore(playerlist)
				thisPlayer.volume = len(playerlist)
				thisPlayer.date = datetime.date.today()
				thisPlayer.save()
			print(thisTeam.longName)

	file.write(str(datetime.datetime.today()))
	file.close()
	if flag:
		file2.write(str(datetime.datetime.today()))
		file2.close()

warnings.filterwarnings("ignore")
file = open("/home/soccersentimeter/Sentimeter/lastteam.txt","r")
file2 = open("/home/soccersentimeter/Sentimeter/lastplayer.txt","r")
teamtime = datetime.datetime.strptime(file.read(),'%Y-%m-%d %H:%M:%S.%f')
playertime = datetime.datetime.strptime(file2.read(),'%Y-%m-%d %H:%M:%S.%f')
file.close()
file2.close()
thistime = datetime.datetime.today()
t1 = thistime-teamtime
t2 = thistime-playertime
if t2>datetime.timedelta(0,0,3,11,30):
	update(True)
elif t1>datetime.timedelta(0,0,0,11,30):
	update(False)