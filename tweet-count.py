import json
import pandas as pd
from collections import Counter
tweets_data_path = 'tweet.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
#print (len(tweets_data[0])) to print no. of attr
'''
for attr in tweets_data[0] :
	print (attr)
	print(tweets_data[0][attr])
'''

tweets = pd.DataFrame()
#mapping for all except user and entities
for attr in tweets_data[0]:
	if attr != 'user' and attr != 'entities':
		tweets[attr] = map(lambda tweet: tweet[attr], tweets_data) 
#mapping for entities
tweets['expanded_url'] = map(lambda tweet: tweet['entities']['urls']['expanded_url'],tweets_data)
tweets['hashtags'] = map(lambda tweet: tweet['entities']['hashtags']['text'],tweets_data)
#mapping for user





