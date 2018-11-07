curl -k -H 'Content-Type: application/json' -d '
{
  "params":[
    {
      "searchword":"canada 24",
      "type": "product",
      "blacklist":[],
      "num": 1
    },
    {
      "searchword":"canada 24",
      "type": "article",
      "blacklistItems":[],
      "num": 1
    }
  ],
  "num": 15
 
}
' http://localhost:9124/api/v4/search/itemlist




curl -k -H 'Content-Type: application/json' -d '
{
  "params":[
    {
      "searchword":"nike",
      "type": "product",
      "blacklist": []
    }
  ],
  "num": 10
 
}
' http://96.90.248.211:9124/api/v4/search/itemlist







curl -k -H 'Content-Type: application/json' -d '
{
    "params":
    [
        {
            "user":"0",
            "from":0,
            "num":10,
            "searchword":"Canada",
            "blacklist":[10859412,6712504,192270,204327,182354,201722,7679228,204295,205560,199204,178962,179606,179589,6711258,179432,178959,204975,8148076,6825026,2570298,10859170,132314,437061,436906,9312100,10859168,373265,10859338,10859378,129160,129159,129157,10859342,10859340,436920],

            "articleFilter":[],
            "type":"product",
            "language":"en"
        },
        {
            "user":"0",
            "blacklistItems":[1030],
            "from":0,
            "num":10,
            "searchword":"Canada",
            "articleFilter":[],
            "type":"article",
            "language":"en"
        }
    ],
"num":18
}
' http://localhost:9124/api/v4/search/itemlist