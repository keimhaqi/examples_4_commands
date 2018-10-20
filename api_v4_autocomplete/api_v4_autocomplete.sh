curl -k -H 'Content-Type: application/json' -d '
{
  "params":[
    {
      "searchword":"a",
      "type": "product",
      "blacklist":[],
      "num": 5
    },
    {
      "searchword":"a",
      "type": "article",
      "blacklistItems":[12],
      "num": 5
    }
  ]
 
}
' http://localhost:9124/api/v4/autocomplete