curl -k -H 'Content-Type: application/json' -d '
{
  "operation": "query"
}
' http://96.90.248.211:9099/api/v1/discountlink/available


curl -k -H 'Content-Type: application/json' -d '
{
  "operation": "query",
  "num": 1,
  "startPosition": 1
}
' http://192.168.1.105:9099/api/v1/discountlink/available


operation: query表示查询;

===>返回结果
{
    "items": [
        {
            "linkListTaskId": 2,
            "url": "https://shop.samsonite.com/deal-of-the-day/?ranMID=36605&ranEAID=Jv*v1/Wldzg&ranSiteID=Jv.v1_Wldzg-B8ItjPO5asqXUaifYGNoqw&LSNSUBSITE=Omitted_Jv*v1/Wldzg&ranMID=36605&ranEAID=Jv*v1%2FWldzg&ranSiteID=Jv.v1_Wldzg-CsjpgsyqS0Codm6fjel4CA&LSNSUBSITE=Omitted_Jv*v1%2FWldzg",
            "available": 0,
            "checkTime": 1539915984000,
            "sourceWeb": "dealmoon.com",
            "title": "Select Spinners Sale @ Samsonite"
        },
        {
            "linkListTaskId": 3,
            "url": "https://www.uniqlo.com/us/en/home/?ranMID=40462&ranEAID=Jv*v1%2FWldzg&ranSiteID=Jv.v1_Wldzg-uDYu9i.lCX.xh1KgpJd0TQ&utm_source=Rakuten&utm_medium=Affiliate&siteID=Jv.v1_Wldzg-uDYu9i.lCX.xh1KgpJd0TQ",
            "available": 0,
            "checkTime": 1539916008000,
            "sourceWeb": "dealmoon.com",
            "title": "Sitewide @Uniqlo"
        }
    ],
    "message": null,
    "lifeCycle": 1
}

linkListTaskId: 对用后端记录的主键值;
url: 链接值;
available: 0表示可用，1表示不可用;
checkTime: 发现时间;
sourceWeb: 发现源;
title: 标题， 这个字段不一定会有，有可能会空;



当运营人员选择忽略某个link时：
curl -k -H 'Content-Type: application/json' -d '
{
  "operation": "update",
  "discountLink":{
      "linkListTaskId": 204,
      "available": 1
  }
}
' http://localhost:9099/api/v1/discountlink/available

operation: update 表示更新
linkListTaskId: 对应的后端记录的主键值;
available: 1表示更新此链接为不可用;


当运营人员进入某个link之后，调用如下接口返回link包含的商品列表;
curl -k -H 'Content-Type: application/json' -d '
{
      "linkListTaskId": 6688
}
' http://96.90.248.211:9099/api/v1/discountlink/product

linkListTaskId: 对应后端记录的主键值;

===> 返回结果:
{
    "items": [
        {
            "productId": 168790,
            "lastCheckedTime": 1483250400000,
            "productSale": "$19.99",
            "productPrice": "$9.99",
            "sourceProductId": "69105626",
            "sourceId": 2,
            "productTitle": "Stretch Cotton Dog Polo Shirt",
            "productImageLink": "",
            "width": 590,
            "height": 470,
            "availability": 1,
            "brandId": 5193,
            "attributeValue": "red"
        }
    ],
    "message": null,
    "lifeCycle": 1
}



curl -k -H  'Content-Type: application/json' -d '
{
    "promoLinkId":46,
    "productList":["10871398","10871396"],
    "articleList":["1426"],
    "startDate":1542105699000
}' http://192.168.1.105:9099/api/v1/article/promoLink









discover.task.updatetime=1542021272000