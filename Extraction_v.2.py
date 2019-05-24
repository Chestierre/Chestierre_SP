from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from random import choice
from pathlib import Path
from random import randint
import datetime
import time 

import twitter_credentials

## Total Number of tweets to be extracted
total_limit_tweets = 10000

## Twitter Authenticator - call the credential to access the API
class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_KEY_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth

## class for getting the API wrapper, access to .API methods
class TwitterAPIWrapper():
    def __init__(self):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.TwitterAPIWrapper = API(self.auth)

    def get_twitter_api(self):
        return self.TwitterAPIWrapper

## claas TwitterStreamer - calls the API to stream to tweets
class TwitterStreamer():
    
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()
        
    
    def stream_tweets(self, search_trend):
 
        listener = TwitterListener()
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)
        
        stream.filter(track= search_trend, languages = ['tl'])
         
## class that handle the data passed by the stream     
class TwitterListener(StreamListener):
    def __init__(self):
        super().__init__()
        global total_limit_tweets
        self.counter = 0
        ##random number generator, limits how many tweets to be extracted
        ##from a specific keyword query
        if total_limit_tweets < 50:
            self.limit = randint(1,total_limit_tweets)
        else:
            self.limit = randint(1,100)

    ##Method handles what to do in incomming data       
    def on_data(self, data):
        global total_limit_tweets
        ##save data to .txt file
        try:
            with open(Path("Data/OriginalListData.txt"), 'a') as tf:  
                tf.write(data)
            print(total_limit_tweets)
            print('limit')
            print(self.limit)
            self.counter += 1
            total_limit_tweets -= 1
            ##limit tweets from keyword search
            if self.counter < self.limit:
                return True
            else:
                return False
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
    ## handle if error encountered while streaming tweet
    def on_error(self, status):
        ##pass rate-limit error, in respect to the twitter's term and condition
        ##policy
        if status == 420:
            return False
        print(status)
##suppose to test rate limit of the API                
def test_rate_limit(api, wait=True, buffer=.1):
    
    """
    Tests whether the rate limit of the last request has been reached.
    :param api: The `tweepy` api instance.
    :param wait: A flag indicating whether to wait for the rate limit reset
                 if the rate limit has been reached.
    :param buffer: A buffer time in seconds that is added on to the waiting
                   time as an extra safety margin.
    :return: True if it is ok to proceed with the next request. False otherwise.
    """
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
##subMain    
class submain():    
    global total_limit_tweets
    API_Wrapper = TwitterAPIWrapper()
    twitter_streamer = TwitterStreamer()
    api = API_Wrapper.get_twitter_api()
    
    ##23424934 - yahoo's WOIED for the Philippines    
    trendings = api.trends_place(23424934)
    while total_limit_tweets > 0:

    ## Pass a specific keyword for the list of trending keyword to the stream
    ## once the limit is reached return a pass another keyword       
        temp_trends = choice(trendings[0]['trends'])
        print(temp_trends['name'])
        twitter_streamer.stream_tweets(temp_trends['name'])

##Main class
if __name__ == "__main__":
    submain()
