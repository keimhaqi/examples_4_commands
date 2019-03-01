curl -k -H 'Content-Type: application/json' -d '
{
    "productId": 10978984
}
' http://localhost:8094/version/v1/queryMergerTreeByProductId

curl -X GET 'http://96.90.248.210:8094/version/v1/queryMergerTreeByProductId?productId=9985970'

curl -X GET 'http://192.168.1.105:8094/version/v1/queryMergerTreeBySourceProductId?sourceProductId=5098965'


curl -X GET 'http://localhost:8094/version/v1/queryBackendMergerResultByFrontendProductIdBatch?frontendProductId=10978984'

curl -X POST 'http://localhost:8094/version/v1/save?sourceProductId=B001K94CNG&vendorId=3'

curl -k -H 'Content-Type: application/json' -d '
{
    "sourceProductId": "B001K94CNG"
}
' http://localhost:8094/version/v1/save



curl -k -H 'Content-Type: application/json' -d '
{
    "treeInNodeFormat": "B001K94CNG"
}
' http://localhost:8094/version/v1/insertOrUpdateMergerTree