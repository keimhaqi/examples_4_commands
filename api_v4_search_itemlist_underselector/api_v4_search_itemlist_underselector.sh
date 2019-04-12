curl -k -H 'Content-Type: application/json' -d '
{
    "selectorId": 1,
    "spuBlacklist":["3k46efpgg","lrp4as6go","8q8pdsnn2","p7o4acw","5wq7d194","9qpe6sylv","ryd4rcw5","ww4xo1q5a","8q8pds35","7pw8ktejl","ypq2yte8","2g2dahnaj","ey2x5c6dd","ryd4rc94r","dnvrecdl9","ww4xo1r36","7pw8kteav","47arqcro","7pw8kte3d"]
}
' http://localhost:9124/api/v4/search/itemlist/underselector


curl -k -H 'Content-Type: application/json' -d '
{
    "selectorId": 1,
    "num": 1000,
    "spuBlacklist":["lrp4as6go","8q8pdsnn2","p7o4acw","5wq7d194","9qpe6sylv","ryd4rcw5","ww4xo1q5a","8q8pds35","7pw8ktejl","ypq2yte8","2g2dahnaj","ey2x5c6dd","ryd4rc94r","dnvrecdl9","ww4xo1r36","7pw8kteav","47arqcro","7pw8kte3d"]
}
' http://localhost:9124/api/v4/search/itemlist/underselector