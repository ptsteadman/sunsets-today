import json
import urllib2
from pprint import pprint
from datetime import datetime
from dateutil import tz
import pytz
import random
from time import sleep
import tweepy

def creds():
	with open('creds.json') as data_file:
		data = json.load(data_file)
		consumer_key = data['creds'][0]['consumer_key']
		consumer_secret = data['creds'][0]['consumer_secret']
		access_token = data['creds'][0]['access_token']
		access_token_secret = data['creds'][0]['access_token_secret']
		#return consumer_key, consumer_secret
		return consumer_key, consumer_secret, access_token, access_token_secret


def twitter_api(consumer_key, consumer_secret, access_token, access_token_secret):
    consumer_key = consumer_key
    consumer_secret = consumer_secret
    access_token = access_token
    access_token_secret = access_token_secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

def bullshit():
	url = 'http://api.sunrise-sunset.org/json?lat=40.6970074&lng=-73.9284384&date=today&formatted=0'

	response = urllib2.urlopen(url)
	data = json.load(response)
	sunset = data["results"]["sunset"]
	eastern = datetime.strptime(sunset[:-6], '%Y-%m-%dT%H:%M:%S').replace(tzinfo = pytz.UTC).astimezone(pytz.timezone('America/New_York'))
	current_time = datetime.utcnow().replace(tzinfo = pytz.UTC)
	utc_sunset = datetime.strptime(sunset[:-6], '%Y-%m-%dT%H:%M:%S').replace(tzinfo = pytz.UTC)
	delta = utc_sunset - current_time
	delta = str(delta)
	hours = delta[0:2]
	minutes = delta[2:4]
	if hours[1] == ':':
		hours = hours[0]
	if minutes[0] == '0':
		minutes = minutes[1]
	eastern = str(eastern)
	eastern_time = eastern[11:-6]
	eastern_time = datetime.strptime(eastern_time, "%H:%M:%S")
	actual_time = eastern_time.strftime("%-I:%M")

	if hours == '1':
		hours = hours+' hour'
	else:
		hours = hours+' hours'

	if minutes == '1':
		minutes = minutes+' minute'
	else:
		minutes = minutes+' minutes'

	return actual_time, hours, minutes



consumer_key, consumer_secret, access_token, access_token_secret = creds()

while True:
	consumer_key, consumer_secret, access_token, access_token_secret = creds()

	actual_time, hours, minutes = bullshit()

	'the sun sets '+hours+' and '+minutes+', at '+actual_time,
	"at "+actual_time+", the sun sets ... that's like in "+hours,
	"in "+hours+" and "+minutes+", the sun is gonna set",
	"it is gonna be dark in about "+hours,
	"at "+actual_time+", which is like in "+hours+", the sun is gonna set",
	"the sun goes down at "+actual_time+" today, which is like in "+hours,
	"it is going to start to get dark in "+hours,
	"at "+actual_time+" it is going to get dark",
	"in "+hours+" it is going to start to get dark outside",
	"sun goes down at "+actual_time+" today",
	"sun is going to go down at "+actual_time+", like in "+hours]
	api = twitter_api()
	t = (random.choice(p))
	print t
	api.update_status(status=t)
	sleep(random.randint(7200,7600))

