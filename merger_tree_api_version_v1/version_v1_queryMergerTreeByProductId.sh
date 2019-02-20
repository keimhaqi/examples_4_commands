curl -k -H 'Content-Type: application/json' -d '
{
    "productId": 10978984
}
' http://localhost:8094/version/v1/queryMergerTreeByProductId

curl -X GET 'http://localhost:8094/version/v1/queryMergerTreeByProductId?productId=10978984'


curl -X GET http://localhost:8094/version/v1/queryMergerTreeByProductId?productId=10978984

curl -X POST 'http://localhost:8094/version/v1/save?sourceProductId=B001K94CNG&vendorId=3'

curl -k -H 'Content-Type: application/json' -d '
{
    "sourceProductId": "B001K94CNG"
}
' http://localhost:8094/version/v1/save