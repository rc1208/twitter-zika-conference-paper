import json
import pandas as pd
from collections import Counter
tweets_data_path = 'tweet-cure.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue



tweets = pd.DataFrame()
#mapping text
tweets['text'] = list(map(lambda tweet: tweet['text'],tweets_data))
'''
for t in tweets['text']:
	print(t)
'''
#mapping created_at 
tweets['created_at'] = list(map(lambda tweet: tweet['created_at'],tweets_data))
'''
for t in tweets['created_at']:
	print(t)
'''
#id_string
tweets['id_str'] = list(map(lambda tweet: tweet['id_str'],tweets_data))

#users
tweets['user_id'] = list(map(lambda tweet: tweet['user']['id_str'],tweets_data))
tweets['user_location'] = list(map(lambda tweet: tweet['user']['location'],tweets_data))
tweets['user_followers_count'] = list(map(lambda tweet: tweet['user']['followers_count'],tweets_data))
tweets['user_friends_count'] = list(map(lambda tweet: tweet['user']['friends_count'],tweets_data))
tweets['user_followers_count'] = list(map(lambda tweet: tweet['user']['followers_count'],tweets_data))
tweets['user_favourites_count'] = list(map(lambda tweet: tweet['user']['favourites_count'],tweets_data))

#retweets
tweets['retweet_count'] = list(map(lambda tweet: tweet['retweet_count'],tweets_data))
#fav_count
tweets['favorite_count'] = list(map(lambda tweet: tweet['favorite_count'],tweets_data))
#retweet_count
tweets['retweet_count'] = list(map(lambda tweet: tweet['retweet_count'],tweets_data))

#converting to csv file
tweets.to_csv('tweets.csv')


