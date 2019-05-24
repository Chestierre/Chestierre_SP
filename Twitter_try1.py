
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
import json 
from random import choice

import twitter_credentials


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):
    
    def on_status(self, status):
        ##if not hasattr(status, 'retweeted_status'):
        ##    print (status.text)
        
        ##if (status.geo != None):
        print(status.user.location)
        ##print(status._json['text'])
        print (status)
        ##print ('\n\n')
        ##print (status.retweeted_status)
        ##if (status.retweeted_status):
        ##   print (status.text)
        ## if "RT @" not in status.text:
       ##     print(status.text)
        ##  if (status.retweeted):
       ##     print(status.text)
        ##print(status._json)
       ## print("\n\n")
        ##print(status.coordinates)
        ##print(dir(status.coordinates))
        ##print(status.user.screen_name +' '+status.text)
        return True
     
    """ 
    def on_data(self,data):
        d = json.loads(data)
        ##print(d['text'])
        if not hasattr(d, 'retweeted_status'):
            print (d['text'])
        ##print(data[100])
        print('\n\n')
     """    

    def on_error(self, status):
        ##print(stasus)
        print("ERROR")

 
if __name__ == '__main__':
    

    
    listener = StdOutListener()
    auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_KEY_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
    
    api = API(auth)
    trends1 = api.trends_place(23424934)
    trends12 = choice(trends1[0]['trends'])
    
    print(trends1[0]['trends'][])
    

    ##stream = Stream(auth, listener)
    ##stream.filter(track = trends12['name'])
    ##stream.filter(track = ['#KMKapalit'], languages = ['tl'])
    ##stream.filter(track = ['Duterte'], languages = ['tl'])
    
        