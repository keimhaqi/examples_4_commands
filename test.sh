while (true)
do
  curl -k -H 'Content-Type: application/json' -d '
  {
    "num": 100,
    "searchword":"amazon",
    "blacklist":[111, 222, 333, 444, 555],
    "fields":
    [
        
    ]
    
  }
  ' http://localhost:9124/api/v3/itemlist
  sleep 0.1
done