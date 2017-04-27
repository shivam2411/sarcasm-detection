import string
import re
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk import word_tokenize
from nltk import pos_tag


affectdict={}
sentidict = {}
stopwords = set(stopwords.words('english'))
tweet = "#sarcasm it was amazing!! i had  fun virat kohli??%*("
tweet = tweet.replace("#sarcasm","")
tweet = tweet.replace("#sarcastic","")
tweet = re.sub(r"(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9]+)", "", tweet)
tweet = re.sub(r'^https?:\/\/.*[\r\n]*', '', tweet, flags=re.MULTILINE)
table = string.maketrans("","")
tweet=tweet.translate(table, "?/:^&*()!@$%:;',<.>-+*\{\}[]\"")
stemmer = SnowballStemmer("english",ignore_stopwords=True)
tokens = tweet.split()
tokens = [ w for w in tokens if w not in stopwords]
tokens = [item for item in tokens if item.isalpha()]
#tokens = [ stemmer.stem(w) for w in tokens ]
#print tokens

bigrams=[]
c=0
while c<=len(tokens)-2:
	bigrams.append(tokens[c]+tokens[c+1])
	c=c+1
print bigrams

trigrams=[]
c=0
while c<len(tokens)-2:
	trigrams.append(tokens[c]+tokens[c+1]+tokens[c+2])
	c=c+1
print trigrams

with open('affectscores.txt','r') as file1:
		for line in file1:
			temp = line.split()
			affectdict[temp[0]]=float(temp[1])
with open('senti.txt','r') as file2:
		for line in file2:
			temp = line.split()
			sentidict[temp[0]]=float(temp[1])

#print sentidict

