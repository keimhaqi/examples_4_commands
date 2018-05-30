import requests
import json
import datetime

url = "http://96.90.248.211:9124/api/v3/todayPicks/productUnderTag"
body = {"params":[{"fields":[{"name": "sources", "values":["amazon's choice"]}], "superTag": "amazon's choice"}]}
headers = {'content-type': "application/json"}

index = 0
start = datetime.datetime.now()
response = requests.post(url, data=json.dumps(body), headers=headers)
end = datetime.datetime.now()
rs = (end - start).seconds
print(start)
print(end)
print(response.content)
print("time = " + str(rs))
