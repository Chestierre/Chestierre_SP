from googleapiclient import discovery
from pathlib import Path
import json
import csv

API_KEY='AIzaSyAxzUUX1o6PBhJNGZTlV9FB5Fw_EecVanU'

# Generates API client object dynamically based on service name and version.
service = discovery.build('commentanalyzer', 'v1alpha1', developerKey=API_KEY)

readfile = open(Path('Translation/Translated-SemiProcessed.txt'),'r')
score = []
    
input_keyword = readfile.read().splitlines()
##samplelise = ["i love you","i hate you"]
with open(Path('Translation/SemiPreprocessedTranslateScore.csv'), 'w', newline = '\n') as f:
    writer = csv.writer(f)
    writer.writerow(['Tweet_id','score'])
    
for i in range (3000):
    try:
        analyze_request = {
          'comment': { 'text': input_keyword[i] },
          'requestedAttributes': {'TOXICITY': {}}
        }
        
        response = service.comments().analyze(body=analyze_request).execute()
        
        
        ##print (input_keyword)
        x = json.loads(json.dumps(response, indent=2))

        dict_data = {'tweet_id':i+1,'score':x['attributeScores']['TOXICITY']['summaryScore']['value']}
        score.append(dict_data)
        print(i)
        ##score.append(x['attributeScores']['TOXICITY']['summaryScore']['value'])
    except BaseException:
        print(i)
        print("error")
        dict_data = {'tweet_id':i+1, 'score':"HttpError"}
        score.append(dict_data)        
print(score)
for i in range (len(score)):
    with open(Path('Translation/SemiPreprocessedTranslateScore.csv'), 'a', newline = '\n') as f:
            writer = csv.writer(f)
            writer.writerow([score[i]['tweet_id'], score[i]['score']])