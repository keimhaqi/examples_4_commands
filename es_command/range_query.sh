curl -X GET "192.168.1.105:9201/finishline_dynamic/items/_search?pretty" -H 'Content-Type: application/json' -d'
{
    "query": {
        "range" : {
            "updateTime" : {
                "gte" : "now-200d/d",
                "lte" : "now/d",
                "boost" : 2.0
            }
        }
    }
}
'


curl -X GET "192.168.1.105:9201/finishline_dynamic/items/_search?pretty" -H 'Content-Type: application/json' -d'
{
    "query": {
        "range" : {
            "updateTime" : {
                "gte": "2019-01-28 19:04:07"
            }
        }
    }
}
'


curl -X GET "192.168.1.105:9201/finishline_dynamic/items/_search?pretty" -H 'Content-Type: application/json' -d'
{
    "query": {
        "range" : {
            "productSaleValue" : {
                "gte" : 10.0,
                "lte" : 200.0,
                "boost" : 2.0
            }
        }
    }
}
'