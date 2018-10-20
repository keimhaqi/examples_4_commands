curl -i -k -H 'Content-Type: application/json' -d '
{
  "param":[
    {"productId": 178962}
  ]
}
' http://96.90.248.211:9099/api/v1/prepare/promo/temporary


curl -i -k -H 'Content-Type: application/json' -d '
{
  "param":[
    {"productId": 10495708}
  ],
  "user": 2
}
' http://localhost:9099/api/v1/prepare/promo/persist

curl -i -k -H 'Content-Type: application/json' -d '
{
  "param":{
    "product_id":115577777,
    "price": "$33.33",
    "author_id": 55577777
  },
  "user": 2
}
' http://localhost:9099/api/v1/prepare/promo/hot/persist



curl -i -k -H 'Content-Type: application/json' -d '
{
    "param":{
        "task_id":7334939,
        "title_en":"Amazon - $8.64 ($18.99) Last Week Tonight with John Oliver Presents a Day in the Life of Marlon Bundo",
        "title_ch":"title_ch_example",
        "desc_en":"desc_en_example",
        "desc_ch":"desc_ch_example",
        "share_title_en":"$8.81 ($18.99) Last Week Tonight with John Oliver Presents a Day in the Life of Marlon Bundo",
        "share_title_ch":"share_title_ch_example",
        "share_desc_en":"share_desc_en_example",
        "share_desc_ch":"share_desc_ch_example",
        "img_url":"https://images-na.ssl-images-amazon.com/images/I/51g1nHlue-L._SX478_BO1,204,203,200_.jpg",
        "card_width":480,
        "card_height":500,
        "price":"$99.99",
        "start_date":1538455702111,
        "author_id":99,
        "keywords":"keywords_example",
        "confirmed":1,
        "created_time":1538618663000,
        "confirmed_time":1538618663000,
        "confirmer_id":99,
        "product_id":10495708,
        "vendor_id":3
    },
    "user":23
}
' http://localhost:9099/api/v1/prepare/promo/hot/persist


2018-10-09 05:48:30


[{"productId":239865,"brandId":6969,"categoryTypeId":0,"categoryTypePriority":0,"height":355,"availability":"in_stock","productDescription":[],"productDetail":["We designed Dr. Scholl’s Pain Relief Orthotics for Arch Pain specifically for people who suffer from arch pain due to stress and strain on their arch. They have Shock Guard Technology to treat pain at the source for immediate, all-day relief. The package contains one pair of insoles to fit men's shoe sizes 8-12. Dr. Scholl's has been a trusted brand in foot care since 1904 when Dr. William Mathias Scholl, grandson of a cobbler, launched the company under the name Dr. Scholl Inc."],"productImageLink":"https://images-na.ssl-images-amazon.com/images/I/81S9z9ZXkcL._SY355_.jpg","productPrice":"$20.00","productSale":"$10.10","productTitle":"Dr. Scholl's Dr. Scholl’s Pain Relief Orthotics for Arch Pain for Men, 1 Pair, Size 8-12","sourceId":[3],"sourceProductId":"B014EX3672","width":355,"morePictures":0,"hasSmartPrice":0,"brandName":"Dr. Scholl's","lastCheckedTime":1529970797000,"numOfReviews":76,"score":4.1,"deleted":0,"categories":["Health & Household"],"sources":["subscribe and save"],"vendors":["Amazon"],"topProductPromoInfoVendor":{"id":{"id":239865,"vendorId":3},"taskId":6800960,"titleEn":"Amazon - $10.10 ($20.00) Dr. Scholl's Dr. Scholl’s Pain Relief Orthotics for Arch Pain for Men, 1 Pair, Size 8-12","shareTitleEn":"$10.10 ($20.00) Dr. Scholl's Dr. Scholl’s Pain Relief Orthotics for Arch Pain for Men, 1 Pair, Size 8-12","price":"$10.10","startDate":1530161601000,"authorId":99,"confirmed":1,"createdTime":1539053279000,"confirmedTime":1539053279000,"confirmerId":99,"postedTime":1530161601000,"vendorLogoUrl":"amazon.png","vendorLogoWidth":109,"vendorLogoHeight":33,"product_id":239865,"articleProductId":7783},"price":{"min":20.0,"max":20.0},"currency":"$","sale":{"min":10.1,"max":10.1},"discount":{"min":49.5,"max":49.5,"discountStr":"49.5%"},"language":["en"],"brands":["Dr. Scholl's"],"channel":1,"updateESTime":1539054721384}]


# id, parent_id, category_id, product_id, product_title, product_url, product_image_link, product_short_description, product_long_description, product_keywords, width, height, category_str, availability, brand, attribute_str, upc, spu, class_id, update_time, linkshare_product_id, linkshare_sku, product_price, product_sale, source_product_id, attrs, last_checked, num_of_reviews, score
'217321', '1684', '5', '10495708', 'Last Week Tonight with John Oliver Presents a Day in the Life of Marlon Bundo', 'https://www.amazon.com/dp/145217380X', 'https://images-na.ssl-images-amazon.com/images/I/51g1nHlue-L._SX478_BO1,204,203,200_.jpg', '[]', '[\"About the Author      MARLON BUNDO is a very fun bunny who recently relocated to Washington, D.C. from his home in Indiana. He enjoys hopping through the garden, eating all his vegetables, and hula-hooping.       Read more\"]', NULL, '480', '500', 'Books>Children\'s Books>Growing Up & Facts of Life', 'onsale', '', '907277,1373246,1388007,1387578,1243429,1446236,1387541,907390,1330256,907185,1387527', NULL, NULL, NULL, '2018-03-21 18:15:08', '', '', '$18.99', '$8.64', '145217380X', NULL, '2018-10-08 16:48:24', '7842', '4.9'


# id, product_vendor_id, currency, product_price, product_sale, date, final_price, discount_ids
'775746', '217321', 'USD', '18.99', '8.6400', '2018-10-08 16:48:30', '8.6400', NULL
