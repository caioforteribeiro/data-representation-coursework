import requests

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"
response = requests.get(url)
data = response.json()
print(data)

with open("cso.json", "w") as fp:
    json.dump(data, fp)