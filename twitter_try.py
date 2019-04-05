from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials

#class that print the tweets; Standard out Listener
class StdOutListener(StreamListener):
    
    #take parameter data, data listening for tweets; from StreamListener
    def on_data(self, data):
        print(data)
        return True
    
    #method return when there is a error; from StreamListener
    def on_error(self, status):
        print(status)
        
if __name__ == "__main__":
    listener = StdOutListener()
    auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_KEY_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
    
    stream = Stream(auth, listener)
    
    #filter the tweet; method from stream clasas
    stream.filter(track=['donald trump', 'hilary clinton', 'barack obama', 'bernie sanders'])
    
    