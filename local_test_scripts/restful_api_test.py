import requests
import json
from datetime import datetime
url = 'http://localhost:9123/api/v3/itemlistPersonal'
count = 900
productIds = []
productIds.append('119')
productIds.append('60')

head = {'Content-type':'application/json',
             'Accept':'application/json'}

for i in range(0, count):
    productIds.append('60')

payload = {}
payload['whitelist'] = productIds
payload['searchword'] = 'Saks Fifth Avenue'

payld = json.dumps(payload)
ret = requests.post(url, headers=head, data=payld)
print(ret.status_code)
print(datetime.now())
print(ret.content)
print(datetime.now())

# 2018-02-06 16:28:59.132