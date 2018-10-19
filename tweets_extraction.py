from textblob import TextBlob
import sys , tweepy
import matplotlib.pyplot as plt 

def percentage(part,whole):
	return 100*(float(part)/float(whole))

consumerKey = "*****************"
consumerSecret = "******************************"


accessToken = "*-*"#create these keys on twitter developer site
accessTokenSecret = "***********************************"

auth = tweepy.OAuthHandler(consumerKey,consumerSecret)
auth.set_access_token(accessToken,accessTokenSecret)
api = tweepy.API(auth)

searchTerm = input("enter keyword to search about:")
noOfSearchTerms = int(input("enter how many tweets to analyze:"))

tweets = tweepy.Cursor(api.search,q=searchTerm,lang="en").items(noOfSearchTerms)

positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
