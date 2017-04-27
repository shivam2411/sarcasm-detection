import sys 
from string import ascii_lowercase 
import codecs
from sklearn import ensemble
import numpy as np
import pickle


reload(sys)  
sys.setdefaultencoding('utf8')
import string
import re
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk import word_tokenize
from nltk import pos_tag
from nltk import FreqDist
from sklearn import svm
import os
import csv

from preproc import *
from feature1 import *
from feature3 import *
#from feature4 import *


stopwords = set(stopwords.words('english'))
affectdict ={}
sentidict={}
bidict={}
tridict={}
train_features = []
train_labels = []

 
#X = [[0,0] , [1,1] ]
#Y = [0,1]


def init_dicts():
	global affectdict
	global sentidict
	global bidict
	global tridict
	with open('affectscores.txt','r') as file1:
		for line in file1:
			temp = line.split()
			affectdict[temp[0]]=float(temp[1])
	with open('senti.txt','r') as file2:
		for line in file2:
			temp = line.split()
			sentidict[temp[0]]=float(temp[1])
#	with open('bigramscore.txt','r') as file2:
#			for line in file2:
#				temp = line.split()
#				bidict[temp[0]]=float(temp[1])
#	with open('trigramscore.txt','r') as file2:
#		for line in file2:
#			temp = line.split()
#			tridict[temp[0]]=float(temp[1])
	#print 'initialised dictionaries!'


def getFeatureHelper(tweet):
	features = []
	try:
		features.extend(contrastingFeatures(tweet,affectdict,sentidict,bidict,tridict))
	except:
		print "error in feature 1"
	try:
		features.extend(affectSentiment(tweet,affectdict,sentidict))
	except:
		print "error in feature3"

	# try:
	# 	features.extend(familiarityLanguage(tweet,past_data ))
	# except:
	# 	print "error in feature4"


	#features.extend(bigrmF(tweet))
	#features.extend(trigrmF(tweet))
	#add other functions
	#print features
	return features
	#call the list of features
	# the list of feature will be written into a file directly 
	


def main():

	init_dicts()  #initialize the dictionaries 
	
	"""
	trainingFile = open("output.csv",'a')
	wr = csv.writer(trainingFile, quoting=csv.QUOTE_ALL)
	features = []

	text_file = open("sar.txt", "r")
	sar = text_file.readlines()
	#print len(lines)
	text_file.close()

	text_file = open("notsar.txt", "r")
	notsar = text_file.readlines()
	#print len(lines)
	text_file.close()
		

	for tweet in sar:
		try:
			words = preprocess(tweet,stopwords) # get words properly
			features = getFeatureHelper(words)
			#features.append(1)
			#print features
			train_features.append(features)
			train_labels.append(1)
			wr.writerow(features)
			#print words
		except:
			print "problem"
			#past = list_tweets[1:]
			features = getFeatureHelper(words)
			#features.append(1)
			wr.writerow(features) 
	
	for tweet in notsar:
		try:
			words = preprocess(tweet,stopwords) # get words properly
			features = getFeatureHelper(words)
			#features.append(1)
			#print features
			train_features.append(features)
			train_labels.append(0)
			#print words
		except:
			print "problem"
			#past = list_tweets[1:]
			features = getFeatureHelper(words)
			#features.append(1)
			wr.writerow(features) 

	print(len(train_features))
	print(len(train_labels))
	print(train_features[:10],train_labels[:10])
	
	with open('features.pickle', 'wb') as handle:
		pickle.dump(train_features, handle)
	with open('labels.pickle', 'wb') as handle:
		pickle.dump(train_labels, handle)
	print ("done")
	"""

	with open('features.pickle', 'rb') as handle:
		train_features= pickle.load(handle)
	with open('labels.pickle', 'rb') as handle:
		train_labels= pickle.load(handle)

	train_labels1 = train_labels[:100]
	for item in train_labels[-100:]:
		train_labels1.append(item)
	#print(train_labels1)

	train_features1 = train_features[:100]
	for item in train_features[-100:]:
		train_features1.append(item)
	#print(train_features1)

	clf = ensemble.RandomForestRegressor()
	clf.fit(train_features1, train_labels1)
	print(clf.get_params())
	

	#sarcastic example

	
	words = preprocess("In my lifetime, we've made huge strides, but there's a lot more to learn.",stopwords) # get words properly
	predict_feature = getFeatureHelper(words)

	print("In my lifetime, we've made huge strides, but there's a lot more to learn.")

	if(clf.predict(predict_feature) > 0.5):
		print("Sarcastic tweet")
	else:
		print("Not a sarcastic tweet")

	words = preprocess("Then argue with yourself. Why bother having others answer for themselves",stopwords) # get words properly
	predict_feature = getFeatureHelper(words)

	print("Then argue with yourself. Why bother having others answer for themselves")

	if(clf.predict(predict_feature) > 0.5):
		print("Sarcastic tweet")
	else:
		print("Not a sarcastic tweet")

	words = preprocess("He is a hell of a lot wiser than thee.",stopwords) # get words properly
	predict_feature = getFeatureHelper(words)

	print("He is a hell of a lot wiser than thee.")

	if(clf.predict(predict_feature) > 0.5):
		print("Sarcastic tweet")
	else:
		print("Not a sarcastic tweet")

	words = preprocess("And the answer is: we don't know. Maybe it came from nowhere. Maybe it was created. We don't know.",stopwords) # get words properly
	predict_feature = getFeatureHelper(words)

	print("And the answer is: we don't know. Maybe it came from nowhere. Maybe it was created. We don't know.")

	if(clf.predict(predict_feature) > 0.5):
		print("Sarcastic tweet")
	else:
		print("Not a sarcastic tweet")
#	path_normal = os.path.abspath(__file__ + "/../../") + "/normal_with_past"
#	fileListNormal  = os.listdir(path_normal)
#	for i in fileListNormal:
#		list_tweets = []
#		features = []
#		with open(path_normal+'/'+i) as tweet_file:
#			file_reader = csv.DictReader(tweet_file)
#			for row in file_reader:
#					try:
#						words = preprocess(row['tweet'])
#						list_tweets.append(words)
#					except:
#						print "problem"
#		words = list_tweets[0]
#		past = list_tweets[1:]
#		features = getFeatureHelper(words , past)
#		features.append(0)
#		wr.writerow(features) 


if __name__=="__main__":
	main()
	# main function for the whole project 
	# command line argument format 
	# positivetweets negativetweets
