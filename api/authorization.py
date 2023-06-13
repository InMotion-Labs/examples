import requests
import json
import ast

data = {
    "username": username,
    "password": password,
    "system": "cloud"
}

URL = "https://auth.vumo.ai/login"
headers = {'content-type': 'application/json'}

authResponse = requests.post(URL, data=json.dumps(data), headers=headers)
responseText = authResponse.text
JSONresponse = json.loads(authResponse.text)
dictResponse = ast.literal_eval(authResponse.text)
print(dictResponse) #printed response as py dictionary

accessToken = dictResponse["access_token"]
print(accessToken) #printed bearer token. Unique for every user.
