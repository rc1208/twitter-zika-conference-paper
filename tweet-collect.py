#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = '2842149534-Za3BBQVgOjWczYgXcjpnTthGh0YmYAIUZuILxlv'
access_token_secret = 'xgbRYus3uwrr16QKItmI38PBzOTRV6mbwNUqiVkLVXqxf'
consumer_key = 'N3Gq9TG2CpLjF1rdWGjbHQXxU'
consumer_secret = 'cHhh9XYiKK4CtCmAqG1djrzvYcHZzQ6FYFL7GPtLiwbfSbJytA'


class StdOutListener(StreamListener,filename):

    def on_data(self, data,filename):
        print(data)
        with open(filename,'a') as f:
            f.write(data)
        return True

    def on_error(self, status):
        print(status)



if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener(###Passs File Name Here eg "tweet.py")
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'zika', 'zikavirus', 'Aedes'
    stream.filter(track=['zika', 'zikavirus', 'Aedes'])


