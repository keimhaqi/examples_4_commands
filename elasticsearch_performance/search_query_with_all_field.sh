curl -XGET '172.18.0.2:9200/jinbagsearch/items/_search?pretty'  -H 'Content-Type: application/json' -d'
{
"size":10,
"query" :{
    "bool" : {
      "must" : [
        {
          "bool" : {
            "should" : [
              {
                "match" : {
                  "language" : {
                    "query" : "en",
                    "operator" : "AND",
                    "prefix_length" : 0,
                    "max_expansions" : 50,
                    "fuzzy_transpositions" : true,
                    "lenient" : false,
                    "zero_terms_query" : "NONE",
                    "boost" : 1.0
                  }
                }
              }
            ],
            "disable_coord" : false,
            "adjust_pure_negative" : true,
            "minimum_should_match" : "1",
            "boost" : 1.0
          }
        },
        {
          "match" : {
            "_all" : {
              "query" : "Nike Men Showtime Shield Basketball Jacket",
              "operator" : "AND",
              "prefix_length" : 0,
              "max_expansions" : 50,
              "fuzzy_transpositions" : true,
              "lenient" : false,
              "zero_terms_query" : "NONE",
              "boost" : 1.0
            }
          }
        }
      ],
      "must_not" : [
        {
          "ids" : {
            "type" : [ ],
            "values" : [ ],
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