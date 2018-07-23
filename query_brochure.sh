curl -XGET '192.168.1.106:9201/article/post/_search?pretty' -H 'Content-Type: application/json' -d'
{
    "size":13,
    "query": {
      "bool":{
        "should":[
          {
            "constant_score":{
              "filter":{
                  "match":{
                    "productId" : {
                      "query":10554012,
                      "boost" : 1.0
                  }
                }
              }
            }
          },
          {
            "constant_score":{
              "filter":{
                "match":{
                  "productId": {
                    "query":10651986,
                    "boost" : 1.0
                  }
                }
              }
            }
          },
          {
            "constant_score":{
              "filter":{
                "match":{
                  "productId": {
                    "query":10651988,
                    "boost" : 1.0
                  }
                }
              }
            }
            
          },
          {
            "constant_score":{
              "filter":{
                "match":{
                  "productId": {
                    "query":10651980,
                    "boost" : 1.0
                  }
                }
              }
            }
          },
          {
            "constant_score":{
              "filter":{
                "match":{
                  "productId": {
                    "query":10651982,
                    "boost" : 1.0
                  }
                }
              }
            }
          }
        ]
      }
    }
}
'



curl -XGET '192.168.1.106:9201/brochure/items/_search?pretty' -H 'Content-Type: application/json' -d'
{
    "size":13,
    "query": {
      "bool":{
        "should":[
          {
            "constant_score":{
              "filter":{
                  "match":{
                    "products" : {
                      "query":5,
                      "boost" : 1.0
                  }
                }
              }
            }
          },
          {
            "constant_score":{
              "filter":{
                "match":{
                  "products": {
                    "query":4,
                    "boost" : 1.0
                  }
                }
              }
            }
          },
          {
            "constant_score":{
              "filter":{
                "match":{
                  "products": {
                    "query":3,
                    "boost" : 1.0
                  }
                }
              }
            }
            
          },
          {
            "constant_score":{
              "filter":{
                "match":{
                  "products": {
                    "query":2,
                    "boost" : 1.0
                  }
                }
              }
            }
          },
          {
            "constant_score":{
              "filter":{
                "match":{
                  "products": {
                    "query":1,
                    "boost" : 1.0
                  }
                }
              }
            }
          }
        ]
      }
    }
}
'

