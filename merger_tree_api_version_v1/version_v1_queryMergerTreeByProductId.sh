curl -k -H 'Content-Type: application/json' -d '
{
    "productId": 10978984
}
' http://localhost:8094/version/v1/queryMergerTreeByProductId

curl -X GET 'http://96.90.248.210:8094/version/v1/queryMergerTreeByProductId?productId=10909468'

curl -X GET 'http://192.168.1.105:8094/version/v1/queryMergerTreeBySourceProductId?sourceProductId=5098965'


curl -X GET 'http://localhost:8094/version/v1/queryBackendMergerResultByFrontendProductIdBatch?frontendProductId=10978984'

curl -X POST 'http://96.90.248.210:8094/version/v1/save2MergerTree?sourceProductId=2770520&vendorId=13867'

curl -k -H 'Content-Type: application/json' -d '
{
    "sourceProductId": "B001K94CNG"
}
' http://localhost:8094/version/v1/save

"1562911" -> "4"

curl -k -H 'Content-Type: application/json' -d '
{
    "treeInNodeFormat": "B001K94CNG"
}
' http://localhost:8094/version/v1/insertOrUpdateMergerTree

808618968374

808618962822

808618955954

808618963652

808618956135

    "190041878000", "190041878130", "190041878161", "190041878208", "190041878109", "190041878147", "190041878215", "190041878192", "190041878154", "190041878222", "190041878185", "190041878178", "190041878116"

+--------------+-----------+
| upc          | vendor_id |
+--------------+-----------+
| 190041878000 |      1237 |
| 190041878000 |     25003 |
| 190041878109 |     13867 |
| 190041878116 |     13867 |
| 190041878130 |      1237 |
| 190041878130 |     13867 |
| 190041878130 |     25003 |
| 190041878147 |     13867 |
| 190041878147 |     25003 |
| 190041878154 |     13867 |
| 190041878154 |     25003 |
| 190041878161 |     13867 |
| 190041878161 |     25003 |
| 190041878178 |     13867 |
| 190041878178 |     25003 |
| 190041878185 |     13867 |
| 190041878192 |     13867 |
| 190041878208 |     13867 |
| 190041878208 |     25003 |
| 190041878215 |     13867 |
| 190041878222 |     13867 |
+--------------+-----------+


+--------------+-----------+----------+
| upc          | vendor_id | depot_id |
+--------------+-----------+----------+
| 190041878000 |      1237 |  1353401 |
| 190041878000 |     25003 |   266227 |
| 190041878109 |     13867 |   234949 |
| 190041878116 |     13867 |   484462 |
| 190041878130 |      1237 |  1499697 |
| 190041878130 |     13867 |   235692 |
| 190041878130 |     25003 |   284497 |
| 190041878147 |     13867 |   235469 |
| 190041878147 |     25003 |   361943 |
| 190041878154 |     13867 |   237191 |
| 190041878154 |     25003 |   230259 |
| 190041878161 |     13867 |   333474 |
| 190041878161 |     25003 |   349030 |
| 190041878178 |     13867 |   234951 |
| 190041878178 |     25003 |   342891 |
| 190041878185 |     13867 |   234953 |
| 190041878192 |     13867 |   234947 |
| 190041878208 |     13867 |   234948 |
| 190041878208 |     25003 |    48622 |
| 190041878215 |     13867 |   234950 |
| 190041878222 |     13867 |   234952 |
+--------------+-----------+----------+




curl -X POST 'http://96.90.248.210:8094/version/v1/save?sourceProductId=3236693&vendorId=1237'