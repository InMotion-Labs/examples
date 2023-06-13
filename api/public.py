import requests
import ast
URL = "https://api.carscanner.vumo.ai/v2/public/{NameOfCompany}/session/{CarId}"

response = requests.request("GET", URL.format(
    nameOfCompany=nameOfCompany, carId=carId))

dictResponse = ast.literal_eval(response.text)
print(dictResponse) #printed response as py dictionary