curl -k -H 'Content-Type: application/json' -d '
{
  "params":[
    {
      "searchword":"storage",
      "type": "product",
      "blacklist":[],
      "num": 1
    },
    {
      "searchword":"storage",
      "type": "article",
      "blacklistItems":[12],
      "num": 1
    }
  ]
 
}
' http://localhost:9124/api/v4/search/itemlist