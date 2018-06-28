curl -H "Content-Type: application/json" -d '{ "user": "200117", "num": 4, "userBias":-1 }' http://192.168.1.110:8001/queries.json
curl -H "Content-Type: application/json" -d '{ "user": "7", "num": 4, "userBias":-1 }' http://localhost:8001/queries.json
curl -H "Content-Type: application/json" -d '{ "user": "200117", "num": 4, "userBias":-1, "eventNames:["buy"] }' http://localhost:8000/queries.json
curl -H "Content-Type: application/json" -d '{ "user": "200117", "num": 4, "userBias":-1, "eventNames":["buy"] }' http://localhost:8000/queries.json
curl -H "Content-Type: application/json" -d '{ "user": "200112", "num": 4, "userBias":-1, "eventNames":["buy"] }' http://localhost:8000/queries.json
curl -H "Content-Type: application/json" -d '{ "user": "200117", "num": 4, "userBias":-1, "eventNames":["buy"] }' http://localhost:8000/queries.json
curl -H "Content-Type: application/json" -d '{ "user": "200117", "num": 4, "userBias":0, "eventNames":["buy"] }' http://localhost:8000/queries.json
curl -H "Content-Type: application/json" -d '{ "user": "200117", "num": 4, "userBias":-1, "eventNames":["buy"] }' http://localhost:8000/queries.json
curl -H "Content-Type: application/json" -d '{ "user": "200117", "num": 100, "userBias":-1, "eventNames":["buy"] }' http://localhost:8000/queries.json
curl -H "Content-Type: application/json" -d '{ "user": "200117", "num": 4, "userBias":-1, "eventNames":["view"] }' http://localhost:8000/queries.json
curl -H "Content-Type: application/json" -d '{ "user": "200117", "num": 100, "userBias":-1, "eventNames":["buy"] }' http://localhost:8000/queries.json
curl -H "Content-Type: application/json" -d '{ "user": "200117", "num": 100, "userBias":-1, "eventNames":["buy"] }' http://localhost:8000/queries.json
curl -H "Content-Type: application/json" -d '{ "user": "200117", "num": 4, "userBias":-1, "eventNames":["buy"] }' http://localhost:8000/queries.json
curl -H "Content-Type: application/json" -d '{ "user": "200117", "num": 4, "userBias":-1, "eventNames":["buy"] }' http://localhost:8000/queries.json
curl -H "Content-Type: application/json" -d '{ "user": "200117", "num": 5, "userBias":-1, "eventNames":["buy"] }' http://localhost:8000/queries.json

curl -k -H 'Content-Type: application/json' -d '{"fields": [{"name":"field", "values": ["category"],"bias": 1}]}' http://96.90.248.213:8000/queries.json

curl -k -H 'Content-Type: application/json' -d '
{
  "user": "7",
  "userBias": -1
}
' http://192.168.1.106:9124/api/v3/ur/brochure