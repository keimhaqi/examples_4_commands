curl -k -H 'Content-Type: application/json' -d '
{
    "selectorId": 24
}
' http://96.90.248.211:9099/api/v1/selector/makeupspulist


curl http://96.90.248.211:9099/api/v1/selector/makeupspulist/all


curl -k -H 'Content-Type: application/json' -d '
{
    "selectorId": 13
}
' http://localhost:9099/api/v1/selector/makeupspulist


DATA-612, https://www.jinbags.com/s-moment/988这个selector moment里面的数据比原网站多出2倍都不止