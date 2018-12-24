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
          "values":["舒缓镇静"],
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
  "num": 10,
  "channel":[
      {
          "name": "tags2", 
          "values":["舒缓镇静"],
          "num": 10
      }
  ]
}
' http://localhost:9124/api/v4/ur/brochure



curl -k -H 'Content-Type: application/json' -d '
{
  "num": 10,
  "channel":[
      {
          "name": "tags3", 
          "values":["adidas"],
          "num": 10
      }
  ]
}
' http://localhost:9124/api/v4/ur/brochure