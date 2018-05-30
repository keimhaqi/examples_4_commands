from elasticsearch import Elasticsearch
import datetime
import random
from elasticsearch import helpers
import string
es = Elasticsearch(hosts="96.90.248.211:9201", cluster="es-cluster")

searchword = ["nike", "adidas", "puma", "ralph lauren"]

count = 0
index = 0
while index < 20:
    sw = searchword[random.randint(0, 3)] + " " + string.ascii_lowercase[random.randint(0, 25)] + string.ascii_lowercase[random.randint(0, 25)]
    # sw = "nike shoes yellow"
    start = datetime.datetime.now()
    es_result = es.search(doc_type="items", params={"search_type":"dfs_query_then_fetch"}, body={"query":{
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
                    "fuzzy_transpositions" : True,
                    "lenient" : False,
                    "zero_terms_query" : "NONE",
                    "boost" : 1.0
                    }
                }
                }
            ],
            "disable_coord" : False,
            "adjust_pure_negative" : True,
            "minimum_should_match" : "1",
            "boost" : 1.0
            }
        },
        {
            "bool" : {
            "should" : [
                {
                "match" : {
                    "_all" : {
                    "query" : sw,
                    "operator" : "AND",
                    "prefix_length" : 0,
                    "max_expansions" : 50,
                    "fuzzy_transpositions" : True,
                    "lenient" : False,
                    "zero_terms_query" : "NONE",
                    "boost" : 1.0
                    }
                }
                }
            ],
            "disable_coord" : False,
            "adjust_pure_negative" : True,
            "minimum_should_match" : "1",
            "boost" : 1.0
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
        "should" : [
        {
            "match" : {
            "topProduct" : {
                "query" : True,
                "operator" : "OR",
                "prefix_length" : 0,
                "max_expansions" : 50,
                "fuzzy_transpositions" : True,
                "lenient" : False,
                "zero_terms_query" : "NONE",
                "boost" : 1.0
            }
            }
        }
        ],
        "disable_coord" : False,
        "adjust_pure_negative" : True,
        "boost" : 1.0
    }
    }},
    index="jinbagsearch")

    end = datetime.datetime.now()
    rs = (end - start).seconds
    if rs >= 1:
        count = count + 1

    print(start)
    print(end)
    print("time = " + str(rs) + ", searchword = " + sw)
    index = index + 1
    print es_result

print("count = " + str(count))






