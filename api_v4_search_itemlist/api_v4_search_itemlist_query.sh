curl -k -H 'Content-Type: application/json' -d '
{
  "params":[
    {
      "searchword":"storage",
      "type": "product",
      "blacklist":[]
    },
    {
      "searchword":"storage",
      "type": "brochure",
      "blacklistItems":[12]
    }
  ]
 
}
' http://96.90.248.211:9124/api/v4/search/itemlist