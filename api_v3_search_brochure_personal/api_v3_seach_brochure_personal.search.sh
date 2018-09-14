curl -k -H 'Content-Type: application/json' -d '
{
  "searchword":"锦囊征求",  
  "fields":[
    {"name": "status", "values":[0]},
    {"name": "userId", "values":[23]}
  ],
  "blacklist":[22]
}
' http://192.168.1.104:9124/api/v3/search/brochure/personal