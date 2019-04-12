curl -XPUT 192.168.1.192:9200/search_unpopular_*/_settings -d '{
    "index" : {
    "refresh_interval" : "60s"
    }
}'