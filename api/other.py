
import requests
import json
import ast
import shutil

data = {
    "username": username,
    "password": password,
    "system": "cloud"
}
URL = "https://auth.vumo.ai/login"
headers = {'content-type': 'application/json'}

authResponse = requests.post(URL, data=json.dumps(data), headers=headers)
dictResponse = ast.literal_eval(authResponse.text)
accessToken = dictResponse["access_token"]

headers = {"Authorization": "Bearer %s" % AccessToken}
ApiURL = "https://api.carscanner.vumo.ai/v2/"+str(NameOfCompany)+"/session/"+str(CarId)

responseAPI = requests.get(ApiURL, headers=headers)
DictResponse = ast.literal_eval(responseAPI.text)

Sections = DictResponse["sections"]
index = 0

for element in Sections:
    if "photos" in element:
        photos = element["photos"]
        for innerElement in photos:
            index += 1
            print(innerElement["url"])
            image_url = innerElement["url"]
            resp = requests.get(image_url, stream=True)
            local_file = open('Content%s.jpg' % (index), 'wb')
            resp.raw.decode_content = True
            shutil.copyfileobj(resp.raw, local_file)
            del resp
