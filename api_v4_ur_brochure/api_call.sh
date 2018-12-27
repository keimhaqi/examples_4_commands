curl -k -H 'Content-Type: application/json' -d '
{
  "num": 10,
  "channel":[
      {
          "name": "tags1", 
          "values":["HOME"],
          "num": 10
      },
      {
          "name": "tags2", 
          "values":["Fashion"],
          "num": 10
      },
      {
          "name": "tags3", 
          "values":["adidas"],
          "num": 10
      }
  ]
}
' http://localhost:9124/api/v4/ur/brochure



curl -k -H 'Content-Type: application/json' -d '
{
  "channel":[
      {
          "name": "tags2", 
          "values":["Fashion"],
          "num": 100
      }
  ],
  "blacklistItems":[]
}
' http://96.90.248.211:9124/api/v4/ur/brochure



curl -k -H 'Content-Type: application/json' -d '
{
  "num": 10,
  "channel":[
      {
          "name": "tags3", 
          "values":["adidas"],
          "num": 1
      }
  ],
  "blacklist": [10864498]
}
' http://localhost:9124/api/v4/ur/brochure



/v4/todayPicksStartTime|Thu Dec 27 01:22:14 UTC 2018|/v4/todayPicksEndTime|Thu Dec 27 01:22:14 UTC 2018|/v4/todayPicksTIME|236
/v4/todayPicks Param : 

{
    "user":"0",
    "blacklistItems":[1536,1702,728,1562,492,1502,1678,1710,1720,1738],
    "blacklistComment":[],
    "from":0,
    "num":10,
    "blacklist":[10889712,10551502,10370424,10880806,10903608,10298572,10510592],
    "channel":[
        {
            "name":"home",
            "values":["home"],
            "num":8
        }
    ],
    "articleFilter":[],
    "type":"all",
    "language":"en"
}

curl -k -H 'Content-Type: application/json' -d '
{
    "user":"0",
    "blacklistItems":[1536,1702,728,1562,492,1502,1678,1710,1720,1738],
    "blacklistComment":[],
    "from":0,
    "num":10,
    "blacklist":[10889712,10551502,10370424,10880806,10903608,10298572,10510592],
    "channel":[
        {
            "name":"home",
            "values":["home"],
            "num":8
        }
    ],
    "articleFilter":[],
    "type":"all",
    "language":"en"
}
' http://96.90.248.211:9124/api/v4/ur/brochure

, Result : {"itemlist":{"home":{"itemlist":[],"num":0,"blacklistComment":[],"blacklistProduct":[],"blacklistArticle":[],"hasMoreData":false}},"num":0}