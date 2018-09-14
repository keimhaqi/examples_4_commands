curl -i -k -H 'Content-Type: application/json' -d '
{
  "param":[
    {"productId": 55}
  ]
}
' http://localhost:9099/api/v1/prepare/promo/temporary


curl -i -k -H 'Content-Type: application/json' -d '
{
  "param":[
    {"productId": 56}
  ],
  "user": 2
}
' http://localhost:9099/api/v1/prepare/promo/persist