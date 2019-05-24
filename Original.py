from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import datetime
import time

import twitter_credentials
total_limit_tweets = 10

## TWITTER AUTHENTICATOR ##
## returns twitter credetials


class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_KEY_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth

class TwitterStreamer():
    
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()
        
    
    def stream_tweets(self, Output_filename, hash_tag_list):
        #this handles Twitter Authentication and connect to Twitter API
        listener = TwitterListener(Output_filename)
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)
    
        #filter the tweet; method from stream clasas
        stream.filter(track=hash_tag_list)
   
#class that print the tweets; Standard out ; printing out live tweets
class TwitterListener(StreamListener):
    
    
    def __init__(self, Output_filename):
        self.Output_filename = Output_filename
    
    #take parameter data, data listening for tweets; from StreamListener
    def on_data(self, data):
        try:
            print(data)
            with open(self.Output_filename, 'a') as tf:
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
##"""
        
def test_rate_limit(api, wait=True, buffer=.1):
###    """
    
    """
    Tests whether the rate limit of the last request has been reached.
    :param api: The `tweepy` api instance.
    :param wait: A flag indicating whether to wait for the rate limit reset
                 if the rate limit has been reached.
    :param buffer: A buffer time in seconds that is added on to the waiting
                   time as an extra safety margin.
    :return: True if it is ok to proceed with the next request. False otherwise.
    """
##    """
    #Get the number of remaining requests
    remaining = int(api.last_response.getheader('x-rate-limit-remaining'))
    #Check if we have reached the limit
    if remaining == 0:
        limit = int(api.last_response.getheader('x-rate-limit-limit'))
        reset = int(api.last_response.getheader('x-rate-limit-reset'))
        #Parse the UTC time
        reset = datetime.fromtimestamp(reset)
        #Let the user know we have reached the rate limit
        print ("0 of {} requests remaining until {}.".format(limit, reset))

        if wait:
            #Determine the delay and sleep
            delay = (reset - datetime.now()).total_seconds() + buffer
            print ("Sleeping for {}s...".format(delay))
            time.sleep(delay)
            #We have waited for the rate limit reset. OK to proceed.
            return True
        else:
            #We have reached the rate limit. The user needs to handle the rate limit manually.
            return False 

    #We have not reached the rate limit
    return True

class submain():    
    global total_limit_tweets
    while total_limit_tweets > 0:
        pass
        

###"""
### MAIN CLASS ###

if __name__ == "__main__":
    submain()
    
    
    
    
    
    
    """
    hash_tag_list = ["donald trump", "hillary clinton", "barack obama", "bernie sanders"]
    Output_filename = "tweets.txt"
    
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(Output_filename, hash_tag_list)
    """