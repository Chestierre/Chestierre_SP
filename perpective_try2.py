from googleapiclient import discovery

API_KEY='AIzaSyAxzUUX1o6PBhJNGZTlV9FB5Fw_EecVanU'
input_keyword = 'i love you'

# Generates API client object dynamically based on service name and version.
service = discovery.build('commentanalyzer', 'v1alpha1', developerKey=API_KEY)

analyze_request = {
  'comment': { 'text': input_keyword },
  'requestedAttributes': {'TOXICITY': {}}
}

response = service.comments().analyze(body=analyze_request).execute()

import json
##print (input_keyword)
x = json.loads(json.dumps(response, indent=2))

print(x['attributeScores']['TOXICITY']['summaryScore']['value'])
