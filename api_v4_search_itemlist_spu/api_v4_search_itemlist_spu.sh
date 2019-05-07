curl -k -H 'Content-Type: application/json' -d '
{
  "spu": "dnvrecne"
}
' http://96.90.248.211:9124/api/v4/search/itemlist/spu


curl http://96.90.248.211:9099/api/v1/productgroup/all



curl -k -H 'Content-Type: application/json' -d '
{
  "productGroupId": 81,
  "num":100,
  "spuBlacklist":[]
}
' http://96.90.248.211:9124/api/v4/search/itemlist/product/underproductgroup