import requests
import json
import datetime
import random
import string

searchword = ["ascis", "anta", "apple"]
atype = ["shoes", "shirt", "jeans"]
color = ["black", "red", "yellow","green","white"]


url = "http://96.90.248.211:9124/api/v3/itemlist"
# body = {"params":[{"fields":[{"name": "sources", "values":["amazon's choice"]}], "superTag": "amazon's choice"}]}
body = {"num":10, "searchword":"nike", "blacklist":[111, 222, 333, 444, 555]}
headers = {'content-type': "application/json"}

count = 0
index = 0
while index < 100:
    start = datetime.datetime.now()
    body["searchword"] = searchword[random.randint(0, 2)] + " " + atype[random.randint(0, 2)] +" "+ color[random.randint(0, 4)]
    response = requests.post(url, data=json.dumps(body), headers=headers)
    # print response.status_code
    end = datetime.datetime.now()
    rs = (end - start).seconds
    print(start)
    print(end)
    print(response.content)
    print("time = " + str(rs))
    if rs >= 1:
        count = count + 1

    print("index = " + str(index))
    index = index + 1

print("count = " + str(count))

