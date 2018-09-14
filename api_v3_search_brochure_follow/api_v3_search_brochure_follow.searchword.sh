curl -k -H 'Content-Type: application/json' -d '
{
  "searchword":"锦囊征求",
  "whitelist":[14, 132]
}
' http://192.168.1.104:9124/api/v3/search/brochure/follow