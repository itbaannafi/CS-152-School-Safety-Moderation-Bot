from queue import PriorityQueue
from googleapiclient import discovery
import os
import json
import unidecode as decode

token_path = 'tokens.json'
if not os.path.isfile(token_path):
    raise Exception(f"{token_path} not found!")
with open(token_path) as f:
    # If you get an error here, it means your token is formatted incorrectly. Did you put it in quotes?
    tokens = json.load(f)
    perspective_token = tokens['perspective']
    print("perspective successfully activated")

    
def analyzer(text_to_analyze):
    client = discovery.build("commentanalyzer","v1alpha1", developerKey=perspective_token,
    discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
    static_discovery=False,)

    analyze_request = {
    'comment': { 'text': text_to_analyze },
    'requestedAttributes': {'THREAT': {}}
    }
    response = client.comments().analyze(body=analyze_request).execute()
    #print(json.dumps(response, indent=2))
    #print(response)
    return response['attributeScores']['THREAT']['spanScores'][0]['score']['value']
