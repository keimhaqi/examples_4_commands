curl -k -H 'Content-Type: application/json' -d '
{
    "productGroupId": 79,
    "attributeValueIds": "10240663,1334898,1334385",
    "vendorId":1237
}
' http://96.90.248.211:9099/api/v1/productgroup/makeupspulist

{"unpopular":["v72l6c264"],"popular":["7pw8ktdvx"]}


+----+------------------------+-----------+
| id | attribute_value_ids    | vendor_id |
+----+------------------------+-----------+
| 52 | 1334383,907698,1334586 |     13867 |     ==> categoryStr: women, brand: sandro, vendor: bloomingdales
| 53 | 1334383,1334385,907698 |      1237 |     ==> categoryStr: women, brand: sandro, vendor: nordstrom
| 54 | 1334663,1334586,907698 |     13867 |     ==> categoryStr: women, brand: maje, vendor: bloomingdales
| 55 | 1334385,1334663,907698 |      1237 |     ==> categoryStr: women, brand: maje, vendor: nordstrom

#Location Record
#Tue Apr 16 03:41:24 UTC 2019
added.to.brochure.id=1555385176000



#Location Record
#Tue Apr 16 03:41:42 UTC 2019
next.seed.id=1540882191000



3,4,5,6,7,8,9,10,12,13,14,15,16,17,18


|  4 | 1633153,1334601,2386246 |      3184 |    ==> macys:vendor dl:brand categoryStr:juniors' clothing - jeans
|  8 | 1916437,1334601         |      3184 |    ==> macys:vendor ag jeans:brand
| 15 | 1813168,1334601,2386246 |      3184 |    ==> macys:vendor citizens of humanity:brand categoryStr:juniors' clothing - jeans


curl http://96.90.248.211:9099/api/v1/productgroup/makeupspulist/all



