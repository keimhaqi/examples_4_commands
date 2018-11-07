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

curl -k -H 'Content-Type: application/json' -d '
{
  "params":[
    {
      "searchword":"a",
      "type": "all"
    }
  ],
  "num":5
 
}
' http://localhost:9124/api/v4/autocomplete


curl -k -H 'Content-Type: application/json' -d '
{
  "params":[
    {
      "searchword":"a",
      "type": "all",
      "blacklist":[],
      "num": 5
    },
    {
      "searchword":"a",
      "type": "all",
      "blacklistItems":[12],
      "num": 5
    }
  ]
 
}
' http://localhost:9124/api/v4/autocomplete



curl -k -H 'Content-Type: application/json' -d '
{
  "params":[
    {
      "searchword":"a",
      "type": "article",
      "blacklistItems":[12],
      "num": 5
    }
  ]
 
}
' http://96.90.248.211:9124/api/v4/autocomplete


2018-11-07 10:22:41,999 INFO [pool-9-thread-3] P.d.nosql.manager.AutoCompleteQuery [AutoCompleteQuery.java : 165] 


curl -XGET '172.18.0.2:9200/tag/items/_search?pretty'  -H 'Content-Type: application/json' -d'
{
"size":100,
"query" :
{
  "bool" : {
    "must" : [
      {
        "multi_match" : {
          "query" : "en",
          "fields" : [
            "language^1.0"
          ],
          "type" : "best_fields",
          "operator" : "OR",
          "slop" : 0,
          "prefix_length" : 0,
          "max_expansions" : 50,
          "lenient" : false,
          "zero_terms_query" : "NONE",
          "boost" : 1.0
        }
      }
    ],
    "should" : [
      {
        "multi_match" : {
          "query" : "a",
          "fields" : [
            "words^1.0"
          ],
          "type" : "best_fields",
          "operator" : "OR",
          "slop" : 0,
          "prefix_length" : 0,
          "max_expansions" : 50,
          "lenient" : false,
          "zero_terms_query" : "NONE",
          "boost" : 1.0
        }
      }
    ],
    "disable_coord" : false,
    "adjust_pure_negative" : true,
    "boost" : 1.0
  }
}
}'