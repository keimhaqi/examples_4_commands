curl -k -H 'Content-Type: application/json' -d '
{
  "searchword":"mimibear",  
  "fields":[
    {"name": "status", "values":[0]},
    {"name": "userId", "values":[811]}
  ],
  "blacklist":[22]
}
' http://96.90.248.211:9124/api/v3/search/brochure/personal