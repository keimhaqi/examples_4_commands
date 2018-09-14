curl -i -k -H 'Content-Type: application/json' -d '
{
  "user": "289",
  "num": 10,
  "blacklistItems":[52,40,60,84],
  "blacklist":[9652038,10183072,6467258,10651960,10651982,423595,10651980,10651992],
  "fields":[
    {"name": "status", "values":[0]}
  ]
}
' http://localhost:9125/api/v3/ur/brochure

if(mapUtils.isAvailable(articleProduct)){
            for(Map.Entry<Integer, List<Integer>> entry : articleProduct.entrySet()){
                productIds.addAll(entry.getValue());
                if(collectionUtils.isAvailable(entry.getValue())){
                    for(Integer productId : entry.getValue()){
                        if(collectionUtils.isAvailable(blacklist)){
                            if(!blacklist.contains(productId)){
                                productWithScore.put(productId, 0.);
                            }
                        }
                    }
                }
            }
        }


curl -i -k -H 'Content-Type: application/json' -d '
{
  "user": "289",
  "num": 10,
  "blacklistItems":[52,40,60,84],
  "blacklist":[9652038],
  "fields":[
    {"name": "status", "values":[0]}
  ]
}
' http://localhost:9124/api/v3/ur/brochure

{"promo":{"productId":55,"shareTitleEn":"$125.00 Printed Short-Sleeve Polo","titleEn":"Saks Fifth Avenue - $125.00 Printed Short-Sleeve Polo","vendorId":13816,"productImageLink":"https://image.s5a.com/is/image/saks/0400095747459_500x500.jpg"},"product":{"productId":55,"lastCheckedTime":1483250400000,"productSale":"$125.00","productPrice":"$125.00","sourceId":13816,"productTitle":"Printed Short-Sleeve Polo","productImageLink":"https://image.s5a.com/is/image/saks/0400095747459_500x500.jpg"}}
