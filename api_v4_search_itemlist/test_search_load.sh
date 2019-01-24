#!/bin/sh
i=0
while (( "$i < 300" ))
do 
    curl -k -H 'Content-Type: application/json' -d '
    {
    "params":[
        {
        "searchword":"nike",
        "type": "product",
        "blacklist":[]
        },
        {
        "searchword":"nike",
        "type": "article",
        "blacklistItems":[],
        "fields":[
            {"name": "status", "values":[0]}
        ]
        }
    ],
    "num": 15
    
    }
    ' http://localhost:9124/api/v4/search/itemlist
    let i++
done