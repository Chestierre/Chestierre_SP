from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials

#Twitter Authentication
class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_KEY_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth


class TwitterStreamer():
    
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()
        
    
    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        #this handles Twitter Authentication and connect to Twitter API
        listener = TwitterListener(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)
    
        #filter the tweet; method from stream clasas
        stream.filter(track=hash_tag_list)
   
#class that print the tweets; Standard out Listener
class TwitterListener(StreamListener):
    
    
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename
    
    #take parameter data, data listening for tweets; from StreamListener
    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
    
    #method return when there is a error; from StreamListener
    def on_error(self, status):
        if status == 420:
            #tweet lime error checker
            return False
        print(status)
        
if __name__ == "__main__":
    
    hash_tag_list = ["donald trump", "hillary clinton", "barack obama", "bernie sanders"]
    fetched_tweets_filename = "tweets.txt"
    
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
    
        