#import modules
import requests
import json
#define url
url="https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"
#fetch data from api
response=requests.get(url)
#store json data into variable
data=response.json()
#store data into json file
with open("cso.json", "w") as file:
    json.dump(data, file)
