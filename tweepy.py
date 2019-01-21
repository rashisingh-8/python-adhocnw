#!/usr/bin/python2

import tweepy

consumer_key = ''
consumer_sec = ''
# Using above keys we are going to check authentication handler

auth = tweepy.OAuthHandler(consumer_key,consumer_sec)
# Here auth is the token by consumer key and consumer secret

access_key = ''
secret_key = ''

# Connecting data server with access and secret key by using above token
auth.set_access_token(access_key,secret_key)

# Connecting to twitter api with token that is stored in auth
connected = tweepy.API(auth)

# Searching topics
tweet = connected.search('modi',count=10)
# Coverting to text
for j in tweet :
	print j.text
