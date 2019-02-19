curl -XPUT <nameofhost>:9200/<name_of_index>/_settings -d '{
     "index" : {
     "refresh_interval" : "-1"
     } 
}'