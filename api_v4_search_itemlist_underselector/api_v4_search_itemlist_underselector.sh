curl POST -k -H 'Content-Type: application/json' -d '
{
    "id": 2,
    "executorParam": ""
}
' http://192.168.1.188:8080/xxl-job-admin/jobinfo/trigger


curl -k -H 'Content-Type: application/json' -d '
{
    "selectorId":17,
    "num": 10,
    "uniqueIdBlacklist":[1554]
}
' http://localhost:9124/api/v4/search/itemlist/underselector
curl -k -H 'Content-Type: application/json' -d '
{
    "selectorId": 3,
    "num": 8,
    "spuBlacklist": [
        "nnwnk0joax",
        "y646k0d4dy",
        "wrprkcerav",
        "wrprkcyy94",
        "nnwnk06nwp",
        "x8e8k1j6rv",
        "y646k0vvey",
        "2k6kwcg56l"
    ]
}
' http://localhost:9124/api/v4/search/itemlist/underselector


curl -XGET 'http://192.168.1.105:9201/*_static/items/_search?pretty' -H 'Content-Type: application/json' -d'
{
    "size": 100,
    "query":
{"bool":{"must":[{"bool":{"must":[{"constant_score":{"filter":{"match":{"spu":{"query":["47arqcxvv","7pw8ktdvx","apd5wtnkw","jdw4vfrkp","ypq2yt7lg","v72l6cxew","nqy4vsdev","ryd4rcw5","8q8pds35","ypq2ytg7j","xra2xsorq","p7o4acjpk","nqy4vso","lrp4as2d","47arqce5k","qw52e1878","2g2dahdvv","ww4xo1g7","ey2x5c6q5","p7o4acpa","5wq7d1p6v","ryd4rc9n","2g2dahnaj","3k46ef8j","qw52e1kx","ryd4rc7ap","v72l6col","ryd4rc9o9","3k46efpgg","ey2x5c42d","ryd4rcav7","gya4jc7d7","lrp4as665","2g2dah99g","gya4jc38x","ypq2ytgd5","ey2x5crq","ryd4rc94r","2g2dahnka","ong4ecn58","v72l6cya","7pw8ktkj","jdw4vfr2p","ww4xo1r36","6k7w6fw8l","8q8pdsnn2","7pw8ktend","2g2dah2eq","6k7w6fgg6","jdw4vf8ej","3k46ef9r9","ryd4rcnq3","7pw8kte3d","ww4xo15vg","9qpe6sylv","p7o4acw","9qpe6syd6","8q8pdsn4p","7pw8kt2on","dnvrecdl9","v72l6cjq6","9qpe6s5o4","nqy4vsxy","xra2xs8rl","qw52e1wnv","ww4xo1n3l","apd5wtnxv","jdw4vf36","p7o4acn4","ong4ecrxx","7pw8ktejl","ryd4rcnyx","ey2x5cww","ong4ecgd5","ww4xo1l","apd5wtqgn","ww4xo1q5a","nqy4vsg7l","5wq7d1vgj","xra2xsax","gya4jcn9l","dnvrecno5","7pw8kt85","v72l6cjv6","lrp4as4","ypq2ytrvo","5wq7d194","ey2x5c6a","5wq7d1va7","v72l6c264","k984jtg","lrp4ase53","ypq2ytv5","ey2x5c6dd","7pw8kteav","ypq2yte8","nqy4vsynl","47arqcro","3k46ef3d","ypq2ytggj","5wq7d1ydp","jdw4vfr6q","ryd4rc9jr","3k46efdl9"],"operator":"OR","prefix_length":0,"max_expansions":50,"fuzzy_transpositions":true,"lenient":false,"zero_terms_query":"NONE","boost":1.0}}},"boost":1.0}}],"disable_coord":false,"adjust_pure_negative":true,"boost":1.0}}],"should":[{"match":{"isHot":{"query":1,"operator":"OR","prefix_length":0,"max_expansions":50,"fuzzy_transpositions":true,"lenient":false,"zero_terms_query":"NONE","boost":10.0}}}],"disable_coord":false,"adjust_pure_negative":true,"boost":1.0}}
}'

curl http://96.90.248.211:9099/api/v1/selector/makeupspulist/all