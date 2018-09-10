import tweepy
from textblob import TextBlob
import csv
from array import *
import json
import re
import nltk
from nltk import pos_tag, word_tokenize
from sklearn.feature_extraction.text import CountVectorizer

consumer_key = 'Your Key here'
consumer_secret = 'Your Key here'

access_token = 'Your key here'
access_token_secret ='Your Key here'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
keys = ['tweets','polarity']
tweetings=[]
sentiments=[]
csvdata = []
mentions = []
mentionindex = []

alltweet = api.user_timeline(screen_name='anikethgireesh',count=10)
tokenize = [] 
forbag=[]
for tweet in alltweet:
	forbag.append(tweet.text)
for tweet in alltweet:
    tokenize.append(tweet.text.split(" "))

print()
for i in range(len(tokenize)):
	if "RT" in tokenize[i]:
		tokenize[i].remove("RT")
		tokenize[i].pop(0)
# print(tokenize)
print()
string = '@'
for s in tokenize:
    if string in str(s):
        mentionindex.append(tokenize.index(s))	
for ind in mentionindex:
	for subst in tokenize[ind]:
		if string in subst:
			save = tokenize[ind].index(subst)
			tokenize[ind].pop(save)
			subst = subst[1:]
			tokenize[ind].insert(save,subst)
			mentions.append(subst)
# print(mentions) #First important words for learning
line=[]
#make all lower case and PoS tag
flag=0
for lines in tokenize:
	temp=[]
	for words in lines:
		temp.append((words).lower())
		if(len(temp)==0):
			flag=1
	if(flag==0):
		line.append(nltk.pos_tag(word_tokenize(' '.join(map(str,temp)))))

#extracting all nouns from the PoS tagged features.
nouns=[]
for sentence in line:
	for words in (sentence):
		if(words[1]=='NN' or words[1]=='NNP' or words[1]=='NNS' or words[1]=='NNPS'):
			nouns.append(words[0])
##################################################
# print("UseFul stuff")
# print("Mentions::")
# print(mentions)
# print("Nouns::")
# print(nouns)

#Try using Bag of words for indexing
corpus=forbag
vectorizer=CountVectorizer()
print(vectorizer.fit_transform(corpus).todense())
print(vectorizer.vocabulary_)
