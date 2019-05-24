from pathlib import Path
import json
import csv
import re

a = open(Path("Data/OriginalListData.txt"), 'r')
input_list = []
### TEMP
"""
for i in range (200):
    temp = a.readline()
    if temp != '\n':
        temp2 = json.loads(temp)
        input_list.append(temp2)
"""

## First Method;;;; WORKING
for i in range (40018):
    temp = a.readline()
    if temp != '\n':
        temp2 = json.loads(temp)
        input_list.append(temp2)
## Second Method;;;; WORKING

"""
for i in a:
    ##temp = a.readline()
    temp = i
    if temp != '\n':
        temp2 = json.loads(temp)
        b.append(temp2)
"""        
## Third Method;;;; NOT WORKING
"""
for i in a:
    temp = json.loads(a.readline())
    b.append(temp)
"""
"""
for i in a:
    temp = json.loads(i)
    b.append(temp)
"""

orig_tweets = []
retweets_tweets = []
pk_tweets = 0

for i in range (len(input_list)):
    if 'retweeted_status' not in input_list[i]:
        if 'extended_tweet' in input_list[i]:
            dict_data = dict([('name', input_list[i]['user']['name']), ('screen_name',input_list[i]['user']['screen_name']), ('location', input_list[i]['user']['location']), ('tweet', input_list[i]['extended_tweet']['full_text']), ('tweet_status', 'orig')])
        else:
            dict_data = dict([('name', input_list[i]['user']['name']), ('screen_name',input_list[i]['user']['screen_name']), ('location', input_list[i]['user']['location']), ('tweet', input_list[i]['text']), ('tweet_status', 'orig')])
        orig_tweets.append(dict_data)
    else:
        if 'extended_tweet' in input_list[i]['retweeted_status']:
            dict_data = dict([('name', input_list[i]['user']['name']), ('screen_name',input_list[i]['user']['screen_name']), ('location', input_list[i]['user']['location']), ('tweet', input_list[i]['retweeted_status']['extended_tweet']['full_text']), ('tweet_status', 'retweet_retweet')])
            ##retweets_tweets.append(dict_data)
            ##dict_data = dict([('tweet_id', pk_tweets), ('name', input_list[i]['retweeted_status']['user']['name']), ('screen_name',input_list[i]['retweeted_status']['user']['screen_name']), ('location', input_list[i]['retweeted_status']['user']['location']), ('tweet', input_list[i]['retweeted_status']['extended_tweet']['full_text']), ('tweet_status', 'retweet_orig')])
        else:
            dict_data = dict([('name', input_list[i]['user']['name']), ('screen_name',input_list[i]['user']['screen_name']), ('location', input_list[i]['user']['location']), ('tweet', input_list[i]['text']), ('tweet_status', 'retweet_retweet')])
            ##retweets_tweets.append(dict_data)
            ##dict_data = dict([('tweet_id', pk_tweets), ('name', input_list[i]['retweeted_status']['user']['name']), ('screen_name',input_list[i]['retweeted_status']['user']['screen_name']), ('location', input_list[i]['retweeted_status']['user']['location']), ('tweet', input_list[i]['retweeted_status']['text']), ('tweet_status', 'retweet_orig')])
        retweets_tweets.append(dict_data)


with open(Path('Data/Annotators.csv'), 'w', newline = '\n') as f:
    writer = csv.writer(f)
    writer.writerow(['Tweet_id', 'Name', 'Text', 'score'])
    
with open(Path('Data/SemiPreprocessedTranslate.csv'), 'w', newline = '\n') as f:
    writer = csv.writer(f)
    writer.writerow(['Tweet_id', 'Text', 'translated Text','score'])

with open(Path('Data/FullPreprocessedTranslate.csv'), 'w', newline = '\n') as f:
    writer = csv.writer(f)
    writer.writerow(['Tweet_id', 'Text', 'translated Text','score'])


for i in range (len(orig_tweets)):
    if pk_tweets == 3000:
        break
    pk_tweets += 1
    orig_tweets[i]['tweet_id'] = pk_tweets
    temp_tweet = orig_tweets[i]['tweet'].encode('utf8')
    tweet = ' '.join(re.sub(r"(b\'+)|(\\x[a-z0-9][a-z0-9])|(\\n)|(\w+:\/\/\S+)"," ", str(temp_tweet)).split())
    if orig_tweets[i]['location']:temp_locate = orig_tweets[i]['location'].encode('utf8')
    locate = ' '.join(re.sub(r"(b\'+)|(\\x[a-z0-9][a-z0-9])"," ", str(temp_locate)).split())
    FullP_tweet = ' '.join(re.sub(r"(@[A-Za-z0-9_]+)|(#[A-Za-z0-9]+)|(RT @)"," ", tweet).split())
    
    with open(Path('Data/Annotators.csv'), 'a', newline = '\n') as f:
        writer = csv.writer(f)
        writer.writerow([orig_tweets[i]['tweet_id'], orig_tweets[i]['screen_name'], tweet])
        ###writer.writerow(['Tweet_id', 'Name', 'Text', 'location', 'score'])
        ##writer.writerow([orig_tweets[i]['tweet_id'], orig_tweets[i]['screen_name'], orig_tweets[i]['tweet'], orig_tweets[i]['location']])
    with open(Path('Data/SemiPreprocessedTranslate.csv'), 'a', newline = '\n') as f:
        writer = csv.writer(f)
        writer.writerow([orig_tweets[i]['tweet_id'], tweet])
    with open(Path('Data/FullPreprocessedTranslate.csv'), 'a', newline = '\n') as f:
        writer = csv.writer(f)
        writer.writerow([orig_tweets[i]['tweet_id'], FullP_tweet])

for i in range (len(retweets_tweets)):
    if pk_tweets == 3000:
        break
    pk_tweets += 1
    
    retweets_tweets[i]['tweet_id'] = pk_tweets
    temp_tweet = retweets_tweets[i]['tweet'].encode('utf8')
    tweet = ' '.join(re.sub(r"(b\'+)|(\\x[a-z0-9][a-z0-9])|(\\n)|(\w+:\/\/\S+)"," ", str(temp_tweet)).split())
    if retweets_tweets[i]['location']:temp_locate = retweets_tweets[i]['location'].encode('utf8')
    locate = ' '.join(re.sub(r"(b\'+)|(\\x[a-z0-9][a-z0-9])"," ", str(temp_locate)).split())
    FullP_tweet = ' '.join(re.sub(r"(@[A-Za-z0-9_/]+)|(#[A-Za-z0-9]+)|(RT @)"," ", tweet).split())
    
    with open(Path('Data/Annotators.csv'), 'a', newline = '\n') as f:
        writer = csv.writer(f)
        writer.writerow([retweets_tweets[i]['tweet_id'], retweets_tweets[i]['screen_name'], tweet])
    with open(Path('Data/SemiPreprocessedTranslate.csv'), 'a', newline = '\n') as f:
        writer = csv.writer(f)
        writer.writerow([retweets_tweets[i]['tweet_id'], tweet])
    with open(Path('Data/FullPreprocessedTranslate.csv'), 'a', newline = '\n') as f:
        writer = csv.writer(f)
        writer.writerow([retweets_tweets[i]['tweet_id'], FullP_tweet])


with open(Path('Data/orig_tweets.txt'), 'w') as tf:
    json.dump(orig_tweets, tf)
with open(Path('Data/retweets_tweets.txt'), 'w') as kf:
    json.dump(retweets_tweets, kf)
    


