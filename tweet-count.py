import json
import pandas as pd
from collections import Counter
tweets_data_path = 'twitter_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
print len(tweets_data[0])
for attr in tweets_data[0] :
	print attr
''' 
tweets = pd.DataFrame()
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

#finding relevant tweets using Regular Expression
import re
def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return text
    return False
#infected&death

tweets['infected'] = tweets['text'].apply(lambda tweet: word_in_text('infected',tweet) or word_in_text('infection',tweet) or word_in_text('death',tweet))
print "Number of tweets with infection,infected or death as sub text \n" 		 
print tweets['infected'].value_counts()[True]

print "The zika infected,death tweets are \n"

for infected in tweets['infected']:
	if infected != False:
		print infected


#cure
tweets['cure'] = tweets['text'].apply(lambda tweet: word_in_text('cure',tweet))
print "Number of tweets with cure as sub text \n" 
print tweets['cure'].value_counts()[True]
print "The cure tweets are \n"

for cure in tweets['cure']:
	if cure != False:
		print cure

#fight&prevention

tweets['fight'] = tweets['text'].apply(lambda tweet: word_in_text('fight',tweet) or word_in_text('prevention',tweet) )
print "Number of tweets with fight or prevention as sub text \n" 		 
print tweets['fight'].value_counts()[True]

print "The fight or prevention tweets are \n"

for fight in tweets['fight']:
	if fight != False:
		print fight

#Comparing tweets
import matplotlib.pyplot as plt
tweets_for_zika = [tweets['infected'].value_counts()[True], 
                      tweets['cure'].value_counts()[True], 
                      tweets['fight'].value_counts()[True]]
arr = ['infected','cure','prevention']

x_pos = list(range(len(arr)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_for_zika, width,alpha=1,color='g')
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: infected vs. cure vs. prevention (Relevant data)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(arr)
plt.grid()
plt.savefig('compare_tweets', format='png')
#Extracting links from the relevants tweets
def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''

tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))

#Analyzing Tweets by Language
	print 'Analyzing tweets by language\n'
	tweets_by_lang = tweets['lang'].value_counts()
	fig, ax = plt.subplots()
	ax.tick_params(axis='x', labelsize=15)
	ax.tick_params(axis='y', labelsize=10)
	ax.set_xlabel('Languages', fontsize=15)
	ax.set_ylabel('Number of tweets' , fontsize=15)
	ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
	tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
	plt.savefig('tweet_by_lang', format='png')


	#Analyzing Tweets by Country
	print 'Analyzing tweets by country\n'
	tweets_by_country = tweets['country'].value_counts()
	fig, ax = plt.subplots()
	ax.tick_params(axis='x', labelsize=15)
	ax.tick_params(axis='y', labelsize=10)
	ax.set_xlabel('Countries', fontsize=15)
	ax.set_ylabel('Number of tweets' , fontsize=15)
	ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
	tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
	plt.savefig('tweet_by_country', format='png')



'''
