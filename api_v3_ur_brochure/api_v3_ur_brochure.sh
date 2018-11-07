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
  "num": 1,
  "blacklistItems":[52,40,60,84],
  "blacklist":[4737838,6046746,6244222,6244508,6244058,6244250,1582830,6244322,6244432,6244544,10154666,10188058,10428602,10390276,10339794,9313678,7672980,10318382,10479892,10387808,10543904,10548912,10551138,10480506,10552292,10553338,10508542,10543850,10553644,10553374,10553904,10555936,10558816,10558290,10559332,10554358,10555818,10559222,10556044,10554558,10560720,10562048,10565824,10563762,10564754,10567942,10561882,10565754,10565818,10567078,10576608,10579008,10580306,10584758,10583016,10584570,10583436,10583820,10583310,10583528,10586592,10585954,10585540,10586086,10585804,10586668,10585550,10585662,10587054,10585226,10587234,10587286,10587176,10587288,10587528,10587704,10587178,10587100,10587756,10587590],
  "fields":[
    {"name": "status", "values":[0]}
  ]
}
' http://localhost:9124/api/v3/ur/brochure


curl -i -k -H 'Content-Type: application/json' -d '
{
  "user": "dbcae0ceadd49336",
  "num": 10,
  "blacklistItems":[1088,1086,1064,1084,1090,1082,1080,1078,1076,1072,1074,1068,1070,1066,1058,624,622,1060,1056,1054,1052,1050,1048,1046,1044,1042,1040,1038,1036,1034,1032,1030,1028,1026,1024,1022,1020,1018,1016,1014,1012,1010,1008,1006,1004,1002,1000,998,996,994,992,990,988,986,984,982,980,978,976,974,972,970,968,966,964,962,960,958,956,954,952,950,948,946,944,942,940,938,936,934,932,930,928,926,924,922,920,918,916,914,912,910,908,906,904,902,900,898,896,894,892,890,888,886,884,882,880,878,876,874],
  "blacklist":[],
  "fields":[
    {"name": "status", "values":[0]}
  ]
}
' http://localhost:9124/api/v3/ur/brochure


curl -i -k -H 'Content-Type: application/json' -d '
{
  "user":"230",
  "blacklistItems":[1362,1180,486,1092,1386,1370,1290,814,14,162,1210,324,1212],
  "blacklistArticle":[],
  "from":0,
  "num":10,
  "blacklist":[10866710,10063454,10860460,10867404,10849254,10867406,8398520,8403170,10437782,10444630,10466836,10545072,10552182,10583140,10860346,10860332,10860320,10860326,10860406,10860318,10860324,10860328,10860248,10094774,10867540,10141550,10616600,10616602,10616580,10616584,10616592,10616634,10616636,10466872,10616638,10616642,10616640,10616664,10616660,10616724,10616708,10577164,10616722,10616710,1560232,10616720,4913074,10616714,10616712,10616582,10616716,10543582,10616594,10616718,10616608,9255732,10616590,10616596,10616606,10512258,138127,1510,6815838,10860316,232974,232516,154878,232598,233087,231959,164873,5640116,149774,159188,150412,2588282,150596,144808,157164,163755,5657162,5660634,5660866,5666456,5669962,10488,450666,231773,387973,231805,343356,231775,231816,4739346,387726,4795908,4795902,4748768,4748610,4750378,9667014,10123946,10484792],
  "fields":[{"name":"status","values":[0]}],
  "articleFilter":[],
  "type":"all",
  "language":"en"
}
' http://96.90.248.211:9124/api/v3/ur/brochure/optimize



{
  "user":"230",
  "blacklistItems":[1362,1180,486,1092,1386,1370,1290,814,14,162,1210,324,1212],
  "blacklistArticle":[],
  "from":0,
  "num":10,
  "blacklist":[10866710,10063454,10860460,10867404,10849254,10867406,8398520,8403170,10437782,10444630,10466836,10545072,10552182,10583140,10860346,10860332,10860320,10860326,10860406,10860318,10860324,10860328,10860248,10094774,10867540,10141550,10616600,10616602,10616580,10616584,10616592,10616634,10616636,10466872,10616638,10616642,10616640,10616664,10616660,10616724,10616708,10577164,10616722,10616710,1560232,10616720,4913074,10616714,10616712,10616582,10616716,10543582,10616594,10616718,10616608,9255732,10616590,10616596,10616606,10512258,138127,1510,6815838,10860316,232974,232516,154878,232598,233087,231959,164873,5640116,149774,159188,150412,2588282,150596,144808,157164,163755,5657162,5660634,5660866,5666456,5669962,10488,450666,231773,387973,231805,343356,231775,231816,4739346,387726,4795908,4795902,4748768,4748610,4750378,9667014,10123946,10484792],
  "fields":[{"name":"status","values":[0]}],
  "articleFilter":[],
  "type":"all",
  "language":"en"
}, Result = {"items":[{"item":{"articleId":1362,"commentCount":73,"downCount":0,"good":0,"inTime":1541115890000,"lastCmtTime":1541442170000,"tags":"","description":"","title":"Target Black Friday","top":0,"upCount":0,"upIds":"","userId":217,"viewCount":58,"weight":0.0,"status":0,"shareCount":0,"followCount":0,"resourceUrlUltimate":[{"imageUrl":"https://target.scene7.com/is/image/Target/GUEST_871d09be-ffab-45f7-a815-9dbeb6243ed0?wid=520&hei=520&fmt=pjpeg","width":520,"height":520}],"commentId":39040,"user":{"id":217,"nickName":"sff","active":1,"email":"FANGFEI_SUN@JINBAG.COM","userId":217}},"score":0.9998248938091117,"type":"article"},{"item":{"articleId":1290,"commentCount":2,"downCount":0,"good":0,"inTime":1540862846000,"lastCmtTime":1541439508000,"tags":"","description":"25% Off and more.","title":"Gund Toys","top":0,"upCount":0,"upIds":"","userId":217,"viewCount":4,"weight":0.0,"status":0,"shareCount":0,"followCount":0,"resourceUrlUltimate":[{"imageUrl":"https://images-na.ssl-images-amazon.com/images/I/81yoVFBAxpL._SY355_.jpg","width":355,"height":355}],"commentId":39448,"user":{"id":217,"nickName":"sff","active":1,"email":"FANGFEI_SUN@JINBAG.COM","userId":217}},"score":0.9998214405072352,"type":"article"},{"item":{"lastCmtTime":1541389745000,"followCount":0,"articleId":1106,"upCount":0,"description":"","weight":0.0,"title":"Amazon's Choice","good":0,"userId":99,"commentCount":2939,"tags":"","resourceUrlUltimate":[],"inTime":1525337480000,"downCount":0,"shareCount":0,"top":0,"upIds":"","style":4,"viewCount":648,"window":{"productSale":"$16.69","sourceId":3,"productId":10867622,"lastCheckedTime":1541389721000,"availability":"in_stock","sourceProductId":"B00835PYE6","productTitle":"V8 Original 100% Vegetable Juice, 5.5 oz. Can (6 packs of 8, Total of 48)","vendor":{"vendorId":3,"vendorNameEn":"Amazon","vendorNameCh":"Amazon","vendorDescEn":"Online shopping from the earth's biggest selection of books, magazines, music, DVDs, videos, electronics, computers, software, apparel & accessories, shoes...","vendorDescCh":"全球著名购物平台","vendorLogoUrl":"amazon.png","readable":1,"vendorLogoWidth":109,"vendorLogoHeight":33,"vendorDomain":"amazon.com","currency":"U","language":"en"},"width":450,"productImageLink":"https://images-na.ssl-images-amazon.com/images/I/81Hea2-caqL._SY450_.jpg","productDescription":"[]","productPrice":"$16.69","height":450,"topProductPromoInfoVendor":{"shareTitleEn":"$16.69 V8 Original 100% Vegetable Juice, 5.5 oz. Can (6 packs of 8, Total of 48)","confirmerId":99,"authorId":99,"confirmed":1,"imgUrl":"https://images-na.ssl-images-amazon.com/images/I/81Hea2-caqL._SY450_.jpg","titleEn":"Amazon - $16.69 V8 Original 100% Vegetable Juice, 5.5 oz. Can (6 packs of 8, Total of 48)","price":"$16.69","confirmedTime":1541389741000,"createdTime":1541389741000,"id":{"id":10867622,"vendorId":3},"taskId":6999365,"startDate":1541389744000}},"user":{"id":99,"nickName":"Genie","active":1,"userId":99},"status":0},"score":0.9997568846453864,"type":"article"},{"item":{"lastCmtTime":1541389745000,"followCount":0,"articleId":1106,"upCount":0,"description":"","weight":0.0,"title":"Amazon's Choice","good":0,"userId":99,"commentCount":2939,"tags":"","resourceUrlUltimate":[],"inTime":1525337480000,"downCount":0,"shareCount":0,"top":0,"upIds":"","style":4,"viewCount":648,"window":{"productSale":"$12.28","sourceId":3,"productId":10867612,"lastCheckedTime":1541389570000,"availability":"in_stock","sourceProductId":"B06X6J5F19","productTitle":"Twinings Irish Breakfast Tea Keurig K-Cups, 24 Count","vendor":{"vendorId":3,"vendorNameEn":"Amazon","vendorNameCh":"Amazon","vendorDescEn":"Online shopping from the earth's biggest selection of books, magazines, music, DVDs, videos, electronics, computers, software, apparel & accessories, shoes...","vendorDescCh":"全球著名购物平台","vendorLogoUrl":"amazon.png","readable":1,"vendorLogoWidth":109,"vendorLogoHeight":33,"vendorDomain":"amazon.com","currency":"U","language":"en"},"width":466,"productImageLink":"https://images-na.ssl-images-amazon.com/images/I/51%2BrG2DxAKL._SX466_.jpg","productDescription":"[]","productPrice":"$12.28","height":466,"topProductPromoInfoVendor":{"shareTitleEn":"$12.28 Twinings Irish Breakfast Tea Keurig K-Cups, 24 Count","confirmerId":99,"authorId":99,"confirmed":1,"imgUrl":"https://images-na.ssl-images-amazon.com/images/I/51%2BrG2DxAKL._SX466_.jpg","titleEn":"Amazon - $12.28 Twinings Irish Breakfast Tea Keurig K-Cups, 24 Count","price":"$12.28","confirmedTime":1541389596000,"createdTime":1541389596000,"id":{"id":10867612,"vendorId":3},"taskId":7106982,"startDate":1541389599000}},"user":{"id":99,"nickName":"Genie","active":1,"userId":99},"status":0},"score":0.9997566965155088,"type":"article"},{"item":{"originalLink":"http://forums.huaren.us/archiver/showtopic.aspx?topicid=2231642&page=4","followCount":0,"nickName":"mimibear","articleId":14,"upCount":0,"title":"【参加好物推荐活动】超级爱买买买的推荐清洁，收纳，厨具好物","userId":811,"commentCount":1,"tags":"Storage Organizer,收纳,Cabinet Door Organizer,橱柜门收纳","resourceUrlUltimate":[],"inTime":1526615443000,"downCount":0,"shareCount":0,"style":4,"viewCount":141,"window":{"productSale":"$6.88","sourceId":3,"productId":10579606,"lastCheckedTime":1540579365000,"availability":"in_stock","sourceProductId":"B005N7ETR0","productTitle":"OxiClean Max Force Gel Stick, 6.2 Oz (Pack of 2)","vendor":{"vendorId":3,"vendorNameEn":"Amazon","vendorNameCh":"Amazon","vendorDescEn":"Online shopping from the earth's biggest selection of books, magazines, music, DVDs, videos, electronics, computers, software, apparel & accessories, shoes...","vendorDescCh":"全球著名购物平台","vendorLogoUrl":"amazon.png","readable":1,"vendorLogoWidth":109,"vendorLogoHeight":33,"vendorDomain":"amazon.com","currency":"U","language":"en"},"width":91,"productImageLink":"https://images-na.ssl-images-amazon.com/images/I/71UKo3c4j4L._SY550_.jpg","productDescription":"[]","productPrice":"$11.22","height":355,"topProductPromoInfoVendor":{"shareTitleEn":"$6.88 ($11.22) OxiClean Max Force Gel Stick, 6.2 Oz (Pack of 2)","confirmerId":99,"authorId":99,"confirmed":1,"imgUrl":"https://images-na.ssl-images-amazon.com/images/I/71UKo3c4j4L._SY550_.jpg","titleEn":"Amazon - $6.88 ($11.22) OxiClean Max Force Gel Stick, 6.2 Oz (Pack of 2)","price":"$6.88","confirmedTime":1525643977000,"createdTime":1525643977000,"id":{"id":10579606,"vendorId":3},"taskId":6889062,"startDate":1541388265000}},"user":{"id":811,"nickName":"Cora’s Mom","active":1,"email":"CORAS_MOM@JINBAG.COM","logoUrl":"Q09SQVNfTU9NQEpJTkJBRy5DT00=.jpg","userId":811},"status":0},"score":0.9997549661614261,"type":"article"},{"item":{"originalLink":"http://forums.huaren.us/archiver/showtopic.aspx?topicid=2231642&page=4","followCount":0,"nickName":"mimibear","articleId":14,"upCount":0,"title":"【参加好物推荐活动】超级爱买买买的推荐清洁，收纳，厨具好物","userId":811,"commentCount":1,"tags":"Storage Organizer,收纳,Cabinet Door Organizer,橱柜门收纳","resourceUrlUltimate":[],"inTime":1526615443000,"downCount":0,"shareCount":0,"style":4,"viewCount":141,"window":{"productSale":"$4.98 - $182.99","sourceId":3,"productId":10616662,"lastCheckedTime":1531920386000,"availability":"in_stock","sourceProductId":"B000JKCY8M","productTitle":"Easy Off Easy-Off Professional Oven & Grill Cleaner, 24 oz Can","vendor":{"vendorId":3,"vendorNameEn":"Amazon","vendorNameCh":"Amazon","vendorDescEn":"Online shopping from the earth's biggest selection of books, magazines, music, DVDs, videos, electronics, computers, software, apparel & accessories, shoes...","vendorDescCh":"全球著名购物平台","vendorLogoUrl":"amazon.png","readable":1,"vendorLogoWidth":109,"vendorLogoHeight":33,"vendorDomain":"amazon.com","currency":"U","language":"en"},"width":114,"productImageLink":"https://images-na.ssl-images-amazon.com/images/I/71doK7vzVfL._SY355_.jpg","productDescription":"[]","productPrice":"$4.98 - $182.99","height":355,"topProductPromoInfoVendor":{"shareTitleEn":"$4.98 Easy Off Easy-Off Professional Oven & Grill Cleaner, 24 oz Can","confirmerId":99,"authorId":99,"confirmed":1,"imgUrl":"https://images-na.ssl-images-amazon.com/images/I/71doK7vzVfL._SY355_.jpg","titleEn":"Amazon - $4.98 Easy Off Easy-Off Professional Oven & Grill Cleaner, 24 oz Can","price":"$4.98","confirmedTime":1526511576000,"createdTime":1526511576000,"id":{"id":10616662,"vendorId":3},"taskId":6941412,"startDate":1541388263000}},"user":{"id":811,"nickName":"Cora’s Mom","active":1,"email":"CORAS_MOM@JINBAG.COM","logoUrl":"Q09SQVNfTU9NQEpJTkJBRy5DT00=.jpg","userId":811},"status":0},"score":0.9997549632985084,"type":"article"},{"item":{"lastCmtTime":1540345985000,"followCount":0,"articleId":486,"upCount":0,"description":"","weight":0.0,"title":"Rechargeable Electric Toothbrush","good":0,"userId":811,"commentCount":1,"tags":"","resourceUrlUltimate":[],"inTime":1536534783000,"downCount":0,"shareCount":0,"top":0,"upIds":"","style":4,"viewCount":4,"window":{"productSale":"$39.95","sourceId":3,"productId":6232886,"lastCheckedTime":1541441699000,"availability":"in_stock","sourceProductId":"B00YAR7ZL6","productTitle":"Philips Sonicare for Kids Bluetooth Connected Rechargeable Electric Toothbrush, HX6321/02","vendor":{"vendorId":3,"vendorNameEn":"Amazon","vendorNameCh":"Amazon","vendorDescEn":"Online shopping from the earth's biggest selection of books, magazines, music, DVDs, videos, electronics, computers, software, apparel & accessories, shoes...","vendorDescCh":"全球著名购物平台","vendorLogoUrl":"amazon.png","readable":1,"vendorLogoWidth":109,"vendorLogoHeight":33,"vendorDomain":"amazon.com","currency":"U","language":"en"},"width":355,"productImageLink":"https://images-na.ssl-images-amazon.com/images/I/61UN6Ru9IIL._SX355_.jpg","productDescription":"[\"91% of dental professional parents prefer Sonicare for Kids for their own children\",\"Patented sonic technology with 500 strokes per second. 75% more effective than manual toothbrushes in hard to reach areas for better check-ups guaranteed.\",\"98% of parents say it`s easier to get kids to brush longer and better\",\"Interactive free app educates and gets kids excited abour brushing. Exciting rewards for successful brushing sessions.\",\"KidTimer helps ensure 2minute recommended brushing time, and KidPacer alerts the child to move to the next quadrant of the mouth to ensure a thorough cleaning\"]","productPrice":"$49.99","height":266,"topProductPromoInfoVendor":{"shareTitleEn":"$39.95 ($49.99) Philips Sonicare for Kids Bluetooth Connected Rechargeable Electric Toothbrush, HX6321/02","confirmerId":99,"authorId":99,"confirmed":1,"imgUrl":"https://images-na.ssl-images-amazon.com/images/I/61UN6Ru9IIL._SX355_.jpg","titleEn":"Amazon - $39.95 ($49.99) Philips Sonicare for Kids Bluetooth Connected Rechargeable Electric Toothbrush, HX6321/02","price":"$39.95","confirmedTime":1524880110000,"createdTime":1524880110000,"id":{"id":6232886,"vendorId":3},"taskId":75601,"startDate":1541385041000}},"user":{"id":811,"nickName":"Cora’s Mom","active":1,"email":"CORAS_MOM@JINBAG.COM","logoUrl":"Q09SQVNfTU9NQEpJTkJBRy5DT00=.jpg","userId":811},"status":0},"score":0.9997507837841936,"type":"article"},{"item":{"lastCmtTime":1541389745000,"followCount":0,"articleId":1106,"upCount":0,"description":"","weight":0.0,"title":"Amazon's Choice","good":0,"userId":99,"commentCount":2939,"tags":"","resourceUrlUltimate":[],"inTime":1525337480000,"downCount":0,"shareCount":0,"top":0,"upIds":"","style":4,"viewCount":648,"window":{"productSale":"$7.57","sourceId":3,"productId":10413750,"lastCheckedTime":1541441784000,"availability":"in_stock","sourceProductId":"B0148PKYXU","productTitle":"O'Keeffe's K0290007 Working Hands Hand Cream, 3 oz., Tube, (Pack of 2)","vendor":{"vendorId":3,"vendorNameEn":"Amazon","vendorNameCh":"Amazon","vendorDescEn":"Online shopping from the earth's biggest selection of books, magazines, music, DVDs, videos, electronics, computers, software, apparel & accessories, shoes...","vendorDescCh":"全球著名购物平台","vendorLogoUrl":"amazon.png","readable":1,"vendorLogoWidth":109,"vendorLogoHeight":33,"vendorDomain":"amazon.com","currency":"U","language":"en"},"width":355,"productImageLink":"https://images-na.ssl-images-amazon.com/images/I/81Mx7xgviYL._SX569_.jpg","productDescription":"[]","productPrice":"$10.39","height":355,"topProductPromoInfoVendor":{"shareTitleEn":"$7.57 ($10.39) O'Keeffe's K0290007 Working Hands Hand Cream, 3 oz., Tube, (Pack of 2)","confirmerId":99,"authorId":99,"confirmed":1,"imgUrl":"https://images-na.ssl-images-amazon.com/images/I/81Mx7xgviYL._SY355_.jpg","titleEn":"Amazon - $7.57 ($10.39) O'Keeffe's K0290007 Working Hands Hand Cream, 3 oz., Tube, (Pack of 2)","price":"$7.57","confirmedTime":1541383830000,"createdTime":1541383830000,"id":{"id":10413750,"vendorId":3},"taskId":6802738,"startDate":1541383832000}},"user":{"id":99,"nickName":"Genie","active":1,"userId":99},"status":0},"score":0.9997492156409395,"type":"article"},{"item":{"lastCmtTime":1541389745000,"followCount":0,"articleId":1106,"upCount":0,"description":"","weight":0.0,"title":"Amazon's Choice","good":0,"userId":99,"commentCount":2939,"tags":"","resourceUrlUltimate":[],"inTime":1525337480000,"downCount":0,"shareCount":0,"top":0,"upIds":"","style":4,"viewCount":648,"window":{"productSale":"$9.14","sourceId":3,"productId":10563832,"lastCheckedTime":1541383277000,"availability":"in_stock","sourceProductId":"B0711M6TBL","productTitle":"Silkwood","vendor":{"vendorId":3,"vendorNameEn":"Amazon","vendorNameCh":"Amazon","vendorDescEn":"Online shopping from the earth's biggest selection of books, magazines, music, DVDs, videos, electronics, computers, software, apparel & accessories, shoes...","vendorDescCh":"全球著名购物平台","vendorLogoUrl":"amazon.png","readable":1,"vendorLogoWidth":109,"vendorLogoHeight":33,"vendorDomain":"amazon.com","currency":"U","language":"en"},"width":315,"productImageLink":"https://images-na.ssl-images-amazon.com/images/I/91T1Kgkpp2L._SY445_.jpg","productDescription":"[]","productPrice":"$19.95","height":445,"topProductPromoInfoVendor":{"shareTitleEn":"$9.14 ($19.95) Silkwood","confirmerId":99,"authorId":99,"confirmed":1,"imgUrl":"https://images-na.ssl-images-amazon.com/images/I/91T1Kgkpp2L._SY445_.jpg","titleEn":"Amazon - $9.14 ($19.95) Silkwood","price":"$9.14","confirmedTime":1541383280000,"createdTime":1541383280000,"id":{"id":10563832,"vendorId":3},"taskId":6793237,"startDate":1541383282000}},"user":{"id":99,"nickName":"Genie","active":1,"userId":99},"status":0},"score":0.9997485021340932,"type":"article"},{"item":{"lastCmtTime":1541383243000,"followCount":0,"articleId":1178,"upCount":0,"description":"SanDisk是U盘、SD卡的主流品牌，产品覆盖面广，稳定好用。这个锦囊大家一起来说说他家的产品，系统也会及时发布25% Off 以上的Deal。","weight":0.0,"title":"Sandisk","good":0,"userId":217,"commentCount":64,"tags":"","resourceUrlUltimate":[],"inTime":1540344448000,"downCount":0,"shareCount":0,"top":0,"upIds":"","style":4,"viewCount":79,"window":{"productSale":"$38.99","sourceId":3,"productId":10685426,"lastCheckedTime":1541383240000,"availability":"in_stock","sourceProductId":"B01KJELKQO","productTitle":"SanDisk Extreme 128GB SDXC UHS-I Card (SDSDXVF-128G-GNCIN) [Newest Version]","vendor":{"vendorId":3,"vendorNameEn":"Amazon","vendorNameCh":"Amazon","vendorDescEn":"Online shopping from the earth's biggest selection of books, magazines, music, DVDs, videos, electronics, computers, software, apparel & accessories, shoes...","vendorDescCh":"全球著名购物平台","vendorLogoUrl":"amazon.png","readable":1,"vendorLogoWidth":109,"vendorLogoHeight":33,"vendorDomain":"amazon.com","currency":"U","language":"en"},"width":288,"productImageLink":"https://images-na.ssl-images-amazon.com/images/I/51JR5142wZL.jpg","productDescription":"[]","productPrice":"$59.99","height":355,"topProductPromoInfoVendor":{"shareTitleEn":"$38.99 ($59.99) SanDisk Extreme 128GB SDXC UHS-I Card (SDSDXVF-128G-GNCIN) [Newest Version]","confirmerId":99,"authorId":99,"confirmed":1,"imgUrl":"https://images-na.ssl-images-amazon.com/images/I/51JR5142wZL.jpg","titleEn":"Amazon - $38.99 ($59.99) SanDisk Extreme 128GB SDXC UHS-I Card (SDSDXVF-128G-GNCIN) [Newest Version]","price":"$38.99","confirmedTime":1541298652000,"createdTime":1541298652000,"id":{"id":10685426,"vendorId":3},"taskId":7124826,"startDate":1541383243000}},"user":{"id":217,"nickName":"sff","active":1,"email":"FANGFEI_SUN@JINBAG.COM","userId":217},"status":0},"score":0.9997484514132194,"type":"article"}],"num":10,"lifeCycle":1,"hasMoreData":true,"blacklistProduct":[10866710,10094774],"blacklistComment":[39040,39448]}




curl -i -k -H 'Content-Type: application/json' -d '
{
  "user": "299",
  "num": 2,
  "from": 2,
  "blacklist":[10866842],
  "whitelistArticle":[1092]
}
' http://localhost:9124/api/v3/ur/brochure/product


curl -i -k -H 'Content-Type: application/json' -d '
{
  "user": "299",
  "num": 2,
  "from": 2,
  "blacklist":[10866842],
  "whitelistArticle":[1092]
}
' http://96.90.248.211:9124/api/v3/ur/brochure/product


curl -i -k -H 'Content-Type: application/json' -d '
{
  "user": "299",
  "num": 2
}
' http://96.90.248.211:9124/api/v3/ur/brochure/hot

DATA-293 [Search]提供指定锦囊下正在被追踪的商品类表的接口 ---> 

productIds = {LinkedHashMap$LinkedKeySet@13275}  size = 10
10651560,10459046,10776126,10699482,10759370,10676168,10681872,10821472,10665990,10853170

10651560,
{"promo":{"productId":55,"shareTitleEn":"$125.00 Printed Short-Sleeve Polo","titleEn":"Saks Fifth Avenue - $125.00 Printed Short-Sleeve Polo","vendorId":13816,"productImageLink":"https://image.s5a.com/is/image/saks/0400095747459_500x500.jpg"},"product":{"productId":55,"lastCheckedTime":1483250400000,"productSale":"$125.00","productPrice":"$125.00","sourceId":13816,"productTitle":"Printed Short-Sleeve Polo","productImageLink":"https://image.s5a.com/is/image/saks/0400095747459_500x500.jpg"}}


10459046


4737838,6046746,6244222,6244508,6244058,6244250,1582830,6244322,6244432,6244544,10154666,10188058,10428602,10390276,10339794,9313678,7672980,10318382,10479892,10387808,10543904,10548912,10551138,10480506,10552292,10543850,10553338,10553644,10508542,10553374,10553904,10555936,10558816,10558290,10559332,10554358,10559222,10555818,10556044,10554558,10560720,10562048,10565824,10563762,10564754,10567078,10567942,10561882,10565754,10565818,10576608,10579008,10580306,10584758,10583016,10583528,10584570,10583436,10583820,10583310,10586592,10585954,10585540,10586086,10585226,10585804,10586668,10585550,10585662,10587054



SELECT * FROM `article_product` WHERE `product_id` not in (4737838,6046746,6244222,6244508,6244058,6244250,1582830,6244322,6244432,6244544,10154666,10188058,10428602,10390276,10339794,9313678,7672980,10318382,10479892,10387808,10543904,10548912,10551138,10480506,10552292,10543850,10553338,10553644,10508542,10553374,10553904,10555936,10558816,10558290,10559332,10554358,10559222,10555818,10556044,10554558,10560720,10562048,10565824,10563762,10564754,10567078,10567942,10561882,10565754,10565818,10576608,10579008,10580306,10584758,10583016,10583528,10584570,10583436,10583820,10583310,10586592,10585954,10585540,10586086,10585226,10585804,10586668,10585550,10585662,10587054
) and `article_id` in (1090, 1088, 1086, 1084, 1082, 1080, 1078, 1076, 1074, 1072, 1070, 1068, 1066, 1064)

SELECT * FROM `article` WHERE `id` IN (1090, 1088, 1086, 1084, 1082, 1080, 1078, 1076, 1074, 1072, 1070, 1068, 1066, 1064)



{"user":"289","blacklistItems":[],"num":10,"blacklist":[4737838,6046746,6244222,6244508,6244058,6244250,1582830,6244322,6244432,6244544,10154666,10188058,10428602,10390276,10339794,9313678,7672980,10318382,10479892,10387808,10543904,10548912,10551138,10480506,10552292,10553338,10508542,10543850,10553644,10553374,10553904,10555936,10558816,10558290,10559332,10554358,10555818,10559222,10556044,10554558,10560720,10562048,10565824,10563762,10564754,10567942,10561882,10565754,10565818,10567078,10576608,10579008,10580306,10584758,10583016,10584570,10583436,10583820,10583310,10583528,10586592,10585954,10585540,10586086,10585804,10586668,10585550,10585662,10587054,10585226,10587234,10587286,10587176,10587288,10587528,10587704,10587178,10587100,10587756,10587590],"type":"all","language":"en"}, Result = "Result is ignored"


select distinct(product_id) from article_product where product_id is not NULL limit 10;



select distinct(product_id) from article_product where product_id is not NULL  and article_id in (1066, 1088) and product_id not in (1582830, 4737838) limit 10;


select article_id, count(resource_url) as count_res from article_resource where article_id in (300, 302, 304, 306, 308) limit 1;

select article_id, count(resource_url) as count_res from article_resource where article_id in (300, 302, 304, 306, 308) and count_res > 3 group by article_id;

select article_id, resource_url from article_resource where article_id=300 limit 3;

select article_id, resource_url from (select article_id as a_id, resource_url from article_resource where article_id=300 limit 3) where article_id in ;

SELECT DISTINCT b.user_name,b.town_name FROM (SELECT DISTINCT farmer_id FROM t_farmers_images WHERE create_time>='2017-08-18') a
LEFT JOIN t_farmers b ON a.farmer_id=b.id 

CriteriaBuilder builder = em.getCriteriaBuilder();
CriteriaQuery<Tickets> query = builder.createQuery(Tickets.class);
EntityType<Tickets> type = em.getMetamodel().entity(Tickets.class);
EntityType<TicketsUpdates> typeTU = em.getMetamodel().entity(TicketsUpdates.class);
Root<Tickets> root = query.from(Tickets.class);
Root<TicketsUpdates> rootTicketsUpdates = query.from(TicketsUpdates.class);

Join<Tickets,TicketsUpdates> tupdates = rootTicketsUpdates.join("tickets");


public List<ArticleProduct> queryTest(Set<Integer> articleIds, List<Integer> blacklist, Integer num){
    List<ArticleProduct> articleProductsRelationship = null;
    Map<Integer, List<Integer>> articleProducts = new HashMap();
    List<Integer> productIds = new ArrayList();
//        List<Integer> productIdsInArticle = queryDistinctProductIdsInArticles(articleIds, blacklist, num);
//        if(collectionUtils.isAvailable(productIdsInArticle)){
    Session session = hibernateUtil.getSessionFrontendJinbagFactory().openSession();
    CriteriaBuilder criteriaBuilder = session.getCriteriaBuilder();
    CriteriaQuery<ArticleProduct> majorQuer = criteriaBuilder.createQuery(ArticleProduct.class);
    Root root = majorQuer.from(ArticleProduct.class);

    // subquery
    Subquery<Integer> subquery = majorQuer.subquery(Integer.class);
    Root<ArticleProduct> subroot = subquery.from(ArticleProduct.class);
//        subquery.alias("subquery");
//        Join<ArticleProduct, ArticleProduct> join = subroot.join("productId", JoinType.LEFT);
    subquery.select(subroot.get("productId"));
    subquery.distinct(true);
    Path<List<Integer>> path = subroot.get("productId");
    CriteriaBuilder.In<List<Integer>> in = criteriaBuilder.in(path);
    in.value(blacklist);

//        Predicate predicate = criteriaBuilder.equal(subroot.get("productId"), root);
    subquery.where(criteriaBuilder.and(criteriaBuilder.isNotNull(subroot.get("productId")), criteriaBuilder.not(in)));
    majorQuer.where(criteriaBuilder.equal(root.get("productId"), subroot.get("productId")));

    articleProductsRelationship = session.createQuery(majorQuer).setMaxResults(num).getResultList();
    session.close();

//        }

//        if(collectionUtils.isAvailable(articleProductsRelationship)){
//            for(ArticleProduct articleProduct : articleProductsRelationship){
//                if(articleProducts.containsKey(articleProduct.getArticleId())){
//                    articleProducts.get(articleProduct.getArticleId()).add(articleProduct.getProductId());
//                }else{
//                    List<Integer> productIds = new ArrayList();
//                    productIds.add(articleProduct.getProductId());
//                    articleProducts.put(articleProduct.getArticleId(), productIds);
//                }
//            }
//        }

    return articleProductsRelationship;
}



    public Map<Integer, List<Integer>> queryTest(Set<Integer> articleIds, List<Integer> blacklist, Integer num){
        List<ArticleProduct> articleProductsRelationship = null;
        Map<Integer, List<Integer>> articleProducts = new HashMap();
        List<Integer> productIdsInArticle = queryDistinctProductIdsInArticles(articleIds, blacklist, num);
        if(collectionUtils.isAvailable(productIdsInArticle)){
            Session session = hibernateUtil.getSessionFrontendJinbagFactory().openSession();
            CriteriaBuilder criteriaBuilder = session.getCriteriaBuilder();
            CriteriaQuery<ArticleProduct> criteriaQuery = criteriaBuilder.createQuery(ArticleProduct.class);
            Root<ArticleProduct> root = criteriaQuery.from(ArticleProduct.class);
            Join<ArticleProduct, ArticleProduct> joinArticleProduct = root.join("productId");
            criteriaQuery.where(criteriaBuilder.)


            criteriaQuery.select(root);

            try{
                session.getTransaction().begin();
                articleProductsRelationship = (List<ArticleProduct>)session.createQuery(
                        "select ap from  and ap.status=0")
                            .setParameter("productIds", productIdsInArticle)
                            .list();
                session.getTransaction().commit();
            }catch (HibernateException he){
                logger.error(he.getMessage());
            }finally {
                session.close();
            }

        }

        if(collectionUtils.isAvailable(articleProductsRelationship)){
            for(ArticleProduct articleProduct : articleProductsRelationship){
                if(articleProducts.containsKey(articleProduct.getArticleId())){
                    articleProducts.get(articleProduct.getArticleId()).add(articleProduct.getProductId());
                }else{
                    List<Integer> productIds = new ArrayList();
                    productIds.add(articleProduct.getProductId());
                    articleProducts.put(articleProduct.getArticleId(), productIds);
                }
            }
        }

        return articleProducts;
    }


10672022,10672148,10672270,10672978,10673410 |
|   10673628 |
|   10674126 |
|   10674574 |
|   10674656 |
|   10674704 |
|   10674818 |
|   10674858 |
|   10674932 |
|   10675002 |


10851766


select distinct(ap.product_id) from article_product ap where ap.product_id not in (10672022,10672148,10672270,10672978,10673410) and article_id in (1090, 1088, 1086, 1084) and status=0 limit 10;

select distinct(ap.product_id) as dic_product_id from article_product ap where product_id not in (10672022,10672148,10672270,10672978,10673410) and article_id in (1090, 1088, 1086, 1084) and status=0 limit 10;

select article_id, product_id from article_product as app inner join (select distinct(ap.product_id) as dic_product_id from article_product ap where product_id not in (10672022,10672148,10672270,10672978,10673410) and article_id in (1090, 1088, 1086, 1084) and status=0 limit 10) as dic on (app.product_id=dic.dic_product_id) where app.article_id in (1090, 1088, 1086, 1084);

select article_id, product_id from article_product as app where app.product_id in (select distinct(ap.product_id) as dic_product_id from article_product ap where product_id not in (10672022,10672148,10672270,10672978,10673410) and article_id in (1090, 1088, 1086, 1084) and status=0) and app.article_id in (1090, 1088, 1086, 1084);


// create the outer query
CriteriaBuilder cb = em.getCriteriaBuilder();
CriteriaQuery cq = cb.createQuery(Author.class);
Root root = cq.from(Author.class);
 
// count books written by an author
Subquery sub = cq.subquery(Long.class);
Root subRoot = sub.from(Book.class);
SetJoin<Book, Author> subAuthors = subRoot.join(Book_.authors);
sub.select(cb.count(subRoot.get(Book_.id)));
sub.where(cb.equal(root.get(Author_.id), subAuthors.get(Author_.id)));
 
// check the result of the subquery
cq.where(cb.greaterThanOrEqualTo(sub, 3L));
 
TypedQuery query = em.createQuery(cq);
List authors = query.getResultList();



select major.article_id as major_article_id, major.product_id as major_product_id from article_product as major left join article_product as sub on sub.product_id=major.product_id;


10851766

4737822,10857940,10853476,239127,237942,4737838,239865,239662


SELECT * FROM `article_product` WHERE `product_id` IN (4737822,10857940,10853476,239127,237942,4737838,239865,239662) and article_id=322 


select distinct(comment_id), max(update_time) as update_time from article_product group by comment_id order by update_time desc 


select product_id, comment_id, max(update_time) as update_time from article_product group by product_id, comment_id order by update_time desc 

select distinct(product_id), max(comment_id), max(update_time) as update_time from article_product group by product_id order by update_time desc 

select distinct(comment_id), distinct(product_id), max(update_time) as update_time from article_product group by comment_id order by update_time desc 

select product_id,max(update_time) as update_time from article_product where comment_id in (select DISTINCT(comment_id) from article_product order by update_time desc) group_by product_id order by update_time desc

select product_id, comment_id, max(update_time) as update_time from article_product group by product_id, comment_id order by update_time desc 

select DISTINCT(product_id) from article_product WHERE (comment_id,update_time) in (select comment_id, max(update_time) as update_time from article_product group by comment_id order by update_time desc)


curl -i -k -H 'Content-Type: application/json' -d '
{
    "user":"299",
    "blacklistItems":[1362,1290,1106,14,486,1178,814,162,1370,1386,1092,1094,1102,1292,1298,1300,1118,1180,1296,1288,1304,1098,1374,568,472,1122,356,1112,420,1272,990,816,1108,1116,1114,1110,1358,1212,418,1158,1154,1150,1100,1104,1168,1144,278,1282,1152,1156,1170,1148,1164,1174,1278,1276,1268,922,824,1176,378,1140,324,1210,1270,690,360,580,1030,1266,1260,1258,1146,1254,1058,1060,1048,1050,1052,1256,1056,1054,1040,1042,1044,1046,1032,1034,1036,1038,1024,1026,1028,1022,1014,1016,1018,1020,1004,1008,1012,1006,996,998,1000,1002,992,1010,988,978,982,984,986,972,970,994,980,976,974,962,964,966,968,952,954,960,956,958,944,946,948,950,936,938,940,942,928,930,932,934,926,918,920,924,910,912,914,916,900,902,904,908,894,906,898,892,882,884,886,888,890,874,896,880,876,866,868,870,872,856,858,878,864,862,848,850,852,854,842,860,840,844,846,832,834,836,838,830,822,826,818,820,804,806,808,810,812,796,798,800,802,788,790,792,794,784,778,780,782,786,772,774,776,768,762,764,766,752,770,754,756,758,760,744,748,734,746,750,736,738,740,742,726,728,730,732,720,722,724,718,708,710,712,714,716,700,704,706,702,692,694,696,698,688,684,686,676,678,682,674,668,670,658,660,680,672,664,666,650,652,654,640,662,656,642,644,646,648,632,634,636,638,624,626,628,630,622,614,616,618,620,606,608,610,612,598,600,602,604,592,588,594,590,582,584,586,576,578,572,574,596,562,564,566,570,560,554,558,546,548,550,552,544,536,538,540,542,528,530,532,534,520,522,524,526,512,514,516,518,510,502,504,506,508,496,498,500,494,484,488,492,490,480,482,478,468,470,474,460,476,464,466,462,450,452,454,456,458,442,448,444,446,434,436,438,440,424,426,428,432,430,422,408,410,412,414,400,398,416,402,406,390,392,396,384,382,404,394,386,388,374,376,368,364,366,380,370,358,362,352,354,348,338,372,350,342,344,346,336,332,334,340,330,322,326,328,1142,1172,1166,1162,1160,120,292,288,286,284,276,268,256,290,222,1280,1,258,2,4,260,6,262,272,16,18,20,264,8,10,266,12,270,54,22,1302,24,282,26,60,28,80,1360,66,52,72,76,58,78,74,96,98,82,84,86,88,90,92,94,62,100,102,114,1384,1388,108,106,110,112,128,130,116,132,118,104,122,124,126,144,146,164,134,166,154,156,142,176,178,182,184,136,138,186,172,174,208,210,194,212,200,168,202,190,192,240,228,216,236,218,206,234,242,244,230,246,214,248,250,252,254,44,486,1092,1362,1094,1106,64,162,1102,1358,1370,1374,1144,14,556,1118,1098,1168,1122,828,814],
    "blacklistArticle":[1096],
    "from":0,
    "num":10,
    "blacklist":[10866710,10094774,10867622,10867612,10579606,10616662,6232886,10413750,10563832,10685426,10860324,10860326,10860320,10583140,10860332,10860328,10867540,10860406,10141550,10552182,10860318,10860248,10860346,10559082,10563486,7936,10858832,10552848,10861516,10564678,10866842,10710436,10864572,10557622,10864488,10865848,10864352,10858988,10867382,10867390,10710388,10706272,10858808,10866836,10586992,6244464,10849254,10063454,8398520,10860460,10867404,10867406,10742834,10853476,10188138,10865306,10171544,8757268,6244202,10563772,10866938,10556150,10866886,10555000,10861150,10861588,10858748,10557822,4737998,10577162,10864386,10284852,10577972,10866608,10866462,10590388,10587294,10508890,10866456,8242024,6244372,10861686,10866426,10556836,6244480,6244552,10866160,10128302,10866256,10866252,10866228,10866226,10864708,10866216,10864576,10866212,10860002,10864216,6244330,10858790,10866038,6244358,10509650,10563868,10564112,10299060,10567694,10863068,213031,214245,214821,10859106,10859116,216815,213358,10859114,216876,214098,10859092,10859094,215285,10859090,216667,216059,213977,213592,623090,615028,217437,10859098,211964,216060,10862526,10562918,10543762,216824,10851476,10860292,10551872,10860826,10578994,10865522,10861340,10554952,10414378,10580044,10567466,10495644,10551662,10544224,10543662,10553374,10507436,10180456,10864706,10863336,10587280,10480396,10239572,10861362,10849134,10577774,10557838,10545844,10578056,10557954,10165670,10085052,10579816,10440328,10561192,9984996,10310138,10399060,10444582,10080390,10171238,10509264,10509256,10861636,10183032,10176704,10563090,10865836,10579898,10865772,10865792,10564792,10556698,10543612,10558966,10171852,10859512,10183072,7670662,10865216,10865220,178182,161800,168456,10859176,177173,168474,168475,7691884,10861758,171548,204327,199204,168491,153128,6825026,168494,168493,185906,10860692,10859156,10860694,10859158,10860700,10860696,10859160,10860698,10859162,142397,9273038,9273550,150596,189514,168526,181326,168012,10120404,182354,147025,10851070,2588282,185440,168562,182389,159354,147065,199294,163456,149638,171655,142468,7679228,144526,180878,189072,201360,7131386,10178566,159392,10860550,181409,7873756,191140,7532762,10860556,10860558,10860552,10222646,4710644,10849298,165072,141014,10583670,170718,170719,6712504,7691946,335590,164582,160485,170731,179432,150257,141046,181496,205560,143612,190210,10859424,10219934,10859436,149774,192270,10859432,178959,145682,178962,190226,10859446,165142,178452,186645,168731,46876,178979,197922,181555,10525586,10859408,10859410,170819,10860522,8409552,181075,10078154,142167,185177,6794556,7853868,154462,168287,185183,168285,168802,185186,168291,185187,8476128,185184,168289,178529,207712,168295,185188,168293,185189,2589518,141680,150390,183681,2589092,10063642,179589,205706,150409,5176256,948124,6333426,179606,195480,185254,167335,185255,10853120,143268,154532,161188,335277,163755,144808,151464,7131586,168371,207286,180148,168373,948150,195000,6711258,149436,141250,168386,183234,168387,167873,168390,168391,168388,195012,168389,168394,168395,168392,183753,168398,194510,168399,202702,168396,168397,168400,195536,10859378,168414,151007,168415,10859386,168413,1906170,10849090,10859340,4815776,10859342,168434,168435,7532928,10859344,201722,10860554,10860200,10863622,10865210,387973,10860322,4748610,164873,231816,387726,10860334,5660634,232974,150412,10860202,10860330,10859444,10860340,10860342,231959,5660866,232598,10860336,10860338,10860348,10860350,5657162,5669962,10860344,10860420,10860422,10860416,10484792,10860418,4748768,10860428,10860430,10860424,10123946,10860308,10860310,10860432,4795902,343356,10860316,10860312,10860314,232516,4795908,5666456,10860404,9667014,10860400,159188,10860402,10860412,4739346,10860414,231775,10860408,231773,10860410,5640116,4750378,450666,157164,10860244,10488,154878,233087,231805,10865204,10862900,10865096,10865100],
    "fields":[{"name":"status","values":[0]}],
    "articleFilter":[],
    "type":"all",
    "language":"en"
}
' http://localhost:9124/api/v3/ur/brochure



{
    "user":"299",
    "blacklistItems":[1106,14,486,1178,162,1092,1102,1180,1094,1296,1304,1098,1374,568,472,356,420,1362,1272,1290,814,1370,1386,1212,324,1210,1122,816,1298,1300,1112,1288,1114,1116,1292,990,1118,44,486,1092,324,1362,1094,1106,438,1290,64,162,1180,814,1102,1370,1212,1374,1210,1272,14,556,398,1386,740,248],
    "blacklistArticle":[1096],
    "from":0,
    "num":10,
    "blacklist":[10867622,10867612,10579606,10616662,6232886,10413750,10563832,10685426,10559082,10563486,7936,10858832,10552848,10861516,10866842,10710436,10864572,10557622,10864488,10865848,10864352,10858988,10867382,10867390,10710388,10706272,10858808,10866836,10586992,6244464,10742834,10853476,10188138,10865306,10171544,8757268,6244202,10563772,10866938,10556150,10866886,10555000,10861150,10861588,10858748,10557822,4737998,10577162,10864386,10284852,10577972,10866608,10866462,10590388,10587294,10508890,10866456,8242024,6244372,10861686,10866426,10556836,6244480,6244552,10866160,10128302,10866256,10866252,10866228,10866226,10864708,10866216,10864576,10866212,10860002,10864216,6244330,10858790,10866038,6244358,10509650,10563868,10564112,10299060,10567694,10863068,10862526,10562918,10543762,216824],
    "fields":[{"name":"status","values":[0]}],
    "articleFilter":[],
    "type":"all",
    "language":"en"
}


{
    "user":"299",
    "blacklistItems":[1362,1180,486,1092,1386,1370,1290,814,14,162,1210,324,1212,1094,1106,44,486,1092,324,1362,438,1290,1102,64,162,14,1180,814,1370,1212,1178,1210,426,1098,556,322,398,1386,740,1296,804,248,1118,442],"blacklistArticle":[1096],"from":0,"num":10,"blacklist":[],"fields":[{"name":"status","values":[0]}],"articleFilter":[],"type":"all","language":"en"}, Result = {"items":[{"item":{"lastCmtTime":1541389745000,"followCount":0,"articleId":1106,"upCount":0,"description":"","weight":0.0,"title":"Amazon's Choice","good":0,"userId":99,"commentCount":2939,"tags":"","resourceUrlUltimate":[],"inTime":1525337480000,"downCount":0,"shareCount":0,"top":0,"upIds":"","style":4,"viewCount":648,"window":{"productSale":"$16.69","sourceId":3,"productId":10867622,"lastCheckedTime":1541389721000,"availability":"in_stock","sourceProductId":"B00835PYE6","productTitle":"V8 Original 100% Vegetable Juice, 5.5 oz. Can (6 packs of 8, Total of 48)","vendor":{"vendorId":3,"vendorNameEn":"Amazon","vendorNameCh":"Amazon","vendorDescEn":"Online shopping from the earth's biggest selection of books, magazines, music, DVDs, videos, electronics, computers, software, apparel & accessories, shoes...","vendorDescCh":"全球著名购物平台","vendorLogoUrl":"amazon.png","readable":1,"vendorLogoWidth":109,"vendorLogoHeight":33,"vendorDomain":"amazon.com","currency":"U","language":"en"},"width":450,"productImageLink":"https://images-na.ssl-images-amazon.com/images/I/81Hea2-caqL._SY450_.jpg","productDescription":"[]","productPrice":"$16.69","height":450,"topProductPromoInfoVendor":{"shareTitleEn":"$16.69 V8 Original 100% Vegetable Juice, 5.5 oz. Can (6 packs of 8, Total of 48)","confirmerId":99,"authorId":99,"confirmed":1,"imgUrl":"https://images-na.ssl-images-amazon.com/images/I/81Hea2-caqL._SY450_.jpg","titleEn":"Amazon - $16.69 V8 Original 100% Vegetable Juice, 5.5 oz. Can (6 packs of 8, Total of 48)","price":"$16.69","confirmedTime":1541389741000,"createdTime":1541389741000,"id":{"id":10867622,"vendorId":3},"taskId":6999365,"startDate":1541389744000}},"user":{"id":99,"nickName":"Genie","active":1,"userId":99},"status":0},"score":1.9998329242046737,"type":"article"},{"item":{"lastCmtTime":1541389745000,"followCount":0,"articleId":1106,"upCount":0,"description":"","weight":0.0,"title":"Amazon's Choice","good":0,"userId":99,"commentCount":2939,"tags":"","resourceUrlUltimate":[],"inTime":1525337480000,"downCount":0,"shareCount":0,"top":0,"upIds":"","style":4,"viewCount":648,"window":{"productSale":"$12.28","sourceId":3,"productId":10867612,"lastCheckedTime":1541389570000,"availability":"in_stock","sourceProductId":"B06X6J5F19","productTitle":"Twinings Irish Breakfast Tea Keurig K-Cups, 24 Count","vendor":{"vendorId":3,"vendorNameEn":"Amazon","vendorNameCh":"Amazon","vendorDescEn":"Online shopping from the earth's biggest selection of books, magazines, music, DVDs, videos, electronics, computers, software, apparel & accessories, shoes...","vendorDescCh":"全球著名购物平台","vendorLogoUrl":"amazon.png","readable":1,"vendorLogoWidth":109,"vendorLogoHeight":33,"vendorDomain":"amazon.com","currency":"U","language":"en"},"width":466,"productImageLink":"https://images-na.ssl-images-amazon.com/images/I/51%2BrG2DxAKL._SX466_.jpg","productDescription":"[]","productPrice":"$12.28","height":466,"topProductPromoInfoVendor":{"shareTitleEn":"$12.28 Twinings Irish Breakfast Tea Keurig K-Cups, 24 Count","confirmerId":99,"authorId":99,"confirmed":1,"imgUrl":"https://images-na.ssl-images-amazon.com/images/I/51%2BrG2DxAKL._SX466_.jpg","titleEn":"Amazon - $12.28 Twinings Irish Breakfast Tea Keurig K-Cups, 24 Count","price":"$12.28","confirmedTime":1541389596000,"createdTime":1541389596000,"id":{"id":10867612,"vendorId":3},"taskId":7106982,"startDate":1541389599000}},"user":{"id":99,"nickName":"Genie","active":1,"userId":99},"status":0},"score":1.9998327360825385,"type":"article"},{"item":{"originalLink":"http://forums.huaren.us/archiver/showtopic.aspx?topicid=2231642&page=4","followCount":0,"nickName":"mimibear","articleId":14,"upCount":0,"title":"【参加好物推荐活动】超级爱买买买的推荐清洁，收纳，厨具好物","userId":811,"commentCount":1,"tags":"Storage Organizer,收纳,Cabinet Door Organizer,橱柜门收纳","resourceUrlUltimate":[],"inTime":1526615443000,"downCount":0,"shareCount":0,"style":4,"viewCount":141,"window":{"productSale":"$6.88","sourceId":3,"productId":10579606,"lastCheckedTime":1540579365000,"availability":"in_stock","sourceProductId":"B005N7ETR0","productTitle":"OxiClean Max Force Gel Stick, 6.2 Oz (Pack of 2)","vendor":{"vendorId":3,"vendorNameEn":"Amazon","vendorNameCh":"Amazon","vendorDescEn":"Online shopping from the earth's biggest selection of books, magazines, music, DVDs, videos, electronics, computers, software, apparel & accessories, shoes...","vendorDescCh":"全球著名购物平台","vendorLogoUrl":"amazon.png","readable":1,"vendorLogoWidth":109,"vendorLogoHeight":33,"vendorDomain":"amazon.com","currency":"U","language":"en"},"width":91,"productImageLink":"https://images-na.ssl-images-amazon.com/images/I/71UKo3c4j4L._SY550_.jpg","productDescription":"[]","productPrice":"$11.22","height":355,"topProductPromoInfoVendor":{"shareTitleEn":"$6.88 ($11.22) OxiClean Max Force Gel Stick, 6.2 Oz (Pack of 2)","confirmerId":99,"authorId":99,"confirmed":1,"imgUrl":"https://images-na.ssl-images-amazon.com/images/I/71UKo3c4j4L._SY550_.jpg","titleEn":"Amazon - $6.88 ($11.22) OxiClean Max Force Gel Stick, 6.2 Oz (Pack of 2)","price":"$6.88","confirmedTime":1525643977000,"createdTime":1525643977000,"id":{"id":10579606,"vendorId":3},"taskId":6889062,"startDate":1541388265000}},"user":{"id":811,"nickName":"Cora’s Mom","active":1,"email":"CORAS_MOM@JINBAG.COM","logoUrl":"Q09SQVNfTU9NQEpJTkJBRy5DT00=.jpg","userId":811},"status":0},"score":1.9998310055462625,"type":"article"},{"item":{"originalLink":"http://forums.huaren.us/archiver/showtopic.aspx?topicid=2231642&page=4","followCount":0,"nickName":"mimibear","articleId":14,"upCount":0,"title":"【参加好物推荐活动】超级爱买买买的推荐清洁，收纳，厨具好物","userId":811,"commentCount":1,"tags":"Storage Organizer,收纳,Cabinet Door Organizer,橱柜门收纳","resourceUrlUltimate":[],"inTime":1526615443000,"downCount":0,"shareCount":0,"style":4,"viewCount":141,"window":{"productSale":"$4.98 - $182.99","sourceId":3,"productId":10616662,"lastCheckedTime":1531920386000,"availability":"in_stock","sourceProductId":"B000JKCY8M","productTitle":"Easy Off Easy-Off Professional Oven & Grill Cleaner, 24 oz Can","vendor":{"vendorId":3,"vendorNameEn":"Amazon","vendorNameCh":"Amazon","vendorDescEn":"Online shopping from the earth's biggest selection of books, magazines, music, DVDs, videos, electronics, computers, software, apparel & accessories, shoes...","vendorDescCh":"全球著名购物平台","vendorLogoUrl":"amazon.png","readable":1,"vendorLogoWidth":109,"vendorLogoHeight":33,"vendorDomain":"amazon.com","currency":"U","language":"en"},"width":114,"productImageLink":"https://images-na.ssl-images-amazon.com/images/I/71doK7vzVfL._SY355_.jpg","productDescription":"[]","productPrice":"$4.98 - $182.99","height":355,"topProductPromoInfoVendor":{"shareTitleEn":"$4.98 Easy Off Easy-Off Professional Oven & Grill Cleaner, 24 oz Can","confirmerId":99,"authorId":99,"confirmed":1,"imgUrl":"https://images-na.ssl-images-amazon.com/images/I/71doK7vzVfL._SY355_.jpg","titleEn":"Amazon - $4.98 Easy Off Easy-Off Professional Oven & Grill Cleaner, 24 oz Can","price":"$4.98","confirmedTime":1526511576000,"createdTime":1526511576000,"id":{"id":10616662,"vendorId":3},"taskId":6941412,"startDate":1541388263000}},"user":{"id":811,"nickName":"Cora’s Mom","active":1,"email":"CORAS_MOM@JINBAG.COM","logoUrl":"Q09SQVNfTU9NQEpJTkJBRy5DT00=.jpg","userId":811},"status":0},"score":1.9998310027596518,"type":"article"},{"item":{"lastCmtTime":1540345985000,"followCount":0,"articleId":486,"upCount":0,"description":"","weight":0.0,"title":"Rechargeable Electric Toothbrush","good":0,"userId":811,"commentCount":1,"tags":"","resourceUrlUltimate":[],"inTime":1536534783000,"downCount":0,"shareCount":0,"top":0,"upIds":"","style":4,"viewCount":4,"window":{"productSale":"$39.95","sourceId":3,"productId":6232886,"lastCheckedTime":1541441699000,"availability":"in_stock","sourceProductId":"B00YAR7ZL6","productTitle":"Philips Sonicare for Kids Bluetooth Connected Rechargeable Electric Toothbrush, HX6321/02","vendor":{"vendorId":3,"vendorNameEn":"Amazon","vendorNameCh":"Amazon","vendorDescEn":"Online shopping from the earth's biggest selection of books, magazines, music, DVDs, videos, electronics, computers, software, apparel & accessories, shoes...","vendorDescCh":"全球著名购物平台","vendorLogoUrl":"amazon.png","readable":1,"vendorLogoWidth":109,"vendorLogoHeight":33,"vendorDomain":"amazon.com","currency":"U","language":"en"},"width":355,"productImageLink":"https://images-na.ssl-images-amazon.com/images/I/61UN6Ru9IIL._SX355_.jpg","productDescription":"[\"91% of dental professional parents prefer Sonicare for Kids for their own children\",\"Patented sonic technology with 500 strokes per second. 75% more effective than manual toothbrushes in hard to reach areas for better check-ups guaranteed.\",\"98% of parents say it`s easier to get kids to brush longer and better\",\"Interactive free app educates and gets kids excited abour brushing. Exciting rewards for successful brushing sessions.\",\"KidTimer helps ensure 2minute recommended brushing time, and KidPacer alerts the child to move to the next quadrant of the mouth to ensure a thorough cleaning\"]","productPrice":"$49.99","height":266,"topProductPromoInfoVendor":{"shareTitleEn":"$39.95 ($49.99) Philips Sonicare for Kids Bluetooth Connected Rechargeable Electric Toothbrush, HX6321/02","confirmerId":99,"authorId":99,"confirmed":1,"imgUrl":"https://images-na.ssl-images-amazon.com/images/I/61UN6Ru9IIL._SX355_.jpg","titleEn":"Amazon - $39.95 ($49.99) Philips Sonicare for Kids Bluetooth Connected Rechargeable Electric Toothbrush, HX6321/02","price":"$39.95","confirmedTime":1524880110000,"createdTime":1524880110000,"id":{"id":6232886,"vendorId":3},"taskId":75601,"startDate":1541385041000}},"user":{"id":811,"nickName":"Cora’s Mom","active":1,"email":"CORAS_MOM@JINBAG.COM","logoUrl":"Q09SQVNfTU9NQEpJTkJBRy5DT00=.jpg","userId":811},"status":0},"score":1.9998268229196716,"type":"article"},{"item":{"lastCmtTime":1541389745000,"followCount":0,"articleId":1106,"upCount":0,"description":"","weight":0.0,"title":"Amazon's Choice","good":0,"userId":99,"commentCount":2939,"tags":"","resourceUrlUltimate":[],"inTime":1525337480000,"downCount":0,"shareCount":0,"top":0,"upIds":"","style":4,"viewCount":648,"window":{"productSale":"$7.57","sourceId":3,"productId":10413750,"lastCheckedTime":1541441784000,"availability":"in_stock","sourceProductId":"B0148PKYXU","productTitle":"O'Keeffe's K0290007 Working Hands Hand Cream, 3 oz., Tube, (Pack of 2)","vendor":{"vendorId":3,"vendorNameEn":"Amazon","vendorNameCh":"Amazon","vendorDescEn":"Online shopping from the earth's biggest selection of books, magazines, music, DVDs, videos, electronics, computers, software, apparel & accessories, shoes...","vendorDescCh":"全球著名购物平台","vendorLogoUrl":"amazon.png","readable":1,"vendorLogoWidth":109,"vendorLogoHeight":33,"vendorDomain":"amazon.com","currency":"U","language":"en"},"width":355,"productImageLink":"https://images-na.ssl-images-amazon.com/images/I/81Mx7xgviYL._SX569_.jpg","productDescription":"[]","productPrice":"$10.39","height":355,"topProductPromoInfoVendor":{"shareTitleEn":"$7.57 ($10.39) O'Keeffe's K0290007 Working Hands Hand Cream, 3 oz., Tube, (Pack of 2)","confirmerId":99,"authorId":99,"confirmed":1,"imgUrl":"https://images-na.ssl-images-amazon.com/images/I/81Mx7xgviYL._SY355_.jpg","titleEn":"Amazon - $7.57 ($10.39) O'Keeffe's K0290007 Working Hands Hand Cream, 3 oz., Tube, (Pack of 2)","price":"$7.57","confirmedTime":1541383830000,"createdTime":1541383830000,"id":{"id":10413750,"vendorId":3},"taskId":6802738,"startDate":1541383832000}},"user":{"id":99,"nickName":"Genie","active":1,"userId":99},"status":0},"score":1.999825254579323,"type":"article"},{"item":{"lastCmtTime":1541389745000,"followCount":0,"articleId":1106,"upCount":0,"description":"","weight":0.0,"title":"Amazon's Choice","good":0,"userId":99,"commentCount":2939,"tags":"","resourceUrlUltimate":[],"inTime":1525337480000,"downCount":0,"shareCount":0,"top":0,"upIds":"","style":4,"viewCount":648,"window":{"productSale":"$9.14","sourceId":3,"productId":10563832,"lastCheckedTime":1541383277000,"availability":"in_stock","sourceProductId":"B0711M6TBL","productTitle":"Silkwood","vendor":{"vendorId":3,"vendorNameEn":"Amazon","vendorNameCh":"Amazon","vendorDescEn":"Online shopping from the earth's biggest selection of books, magazines, music, DVDs, videos, electronics, computers, software, apparel & accessories, shoes...","vendorDescCh":"全球著名购物平台","vendorLogoUrl":"amazon.png","readable":1,"vendorLogoWidth":109,"vendorLogoHeight":33,"vendorDomain":"amazon.com","currency":"U","language":"en"},"width":315,"productImageLink":"https://images-na.ssl-images-amazon.com/images/I/91T1Kgkpp2L._SY445_.jpg","productDescription":"[]","productPrice":"$19.95","height":445,"topProductPromoInfoVendor":{"shareTitleEn":"$9.14 ($19.95) Silkwood","confirmerId":99,"authorId":99,"confirmed":1,"imgUrl":"https://images-na.ssl-images-amazon.com/images/I/91T1Kgkpp2L._SY445_.jpg","titleEn":"Amazon - $9.14 ($19.95) Silkwood","price":"$9.14","confirmedTime":1541383280000,"createdTime":1541383280000,"id":{"id":10563832,"vendorId":3},"taskId":6793237,"startDate":1541383282000}},"user":{"id":99,"nickName":"Genie","active":1,"userId":99},"status":0},"score":1.9998245410311792,"type":"article"},{"item":{"lastCmtTime":1541383243000,"followCount":0,"articleId":1178,"upCount":0,"description":"SanDisk是U盘、SD卡的主流品牌，产品覆盖面广，稳定好用。这个锦囊大家一起来说说他家的产品，系统也会及时发布25% Off 以上的Deal。","weight":0.0,"title":"Sandisk","good":0,"userId":217,"commentCount":64,"tags":"","resourceUrlUltimate":[],"inTime":1540344448000,"downCount":0,"shareCount":0,"top":0,"upIds":"","style":4,"viewCount":79,"window":{"productSale":"$38.99","sourceId":3,"productId":10685426,"lastCheckedTime":1541383240000,"availability":"in_stock","sourceProductId":"B01KJELKQO","productTitle":"SanDisk Extreme 128GB SDXC UHS-I Card (SDSDXVF-128G-GNCIN) [Newest Version]","vendor":{"vendorId":3,"vendorNameEn":"Amazon","vendorNameCh":"Amazon","vendorDescEn":"Online shopping from the earth's biggest selection of books, magazines, music, DVDs, videos, electronics, computers, software, apparel & accessories, shoes...","vendorDescCh":"全球著名购物平台","vendorLogoUrl":"amazon.png","readable":1,"vendorLogoWidth":109,"vendorLogoHeight":33,"vendorDomain":"amazon.com","currency":"U","language":"en"},"width":288,"productImageLink":"https://images-na.ssl-images-amazon.com/images/I/51JR5142wZL.jpg","productDescription":"[]","productPrice":"$59.99","height":355,"topProductPromoInfoVendor":{"shareTitleEn":"$38.99 ($59.99) SanDisk Extreme 128GB SDXC UHS-I Card (SDSDXVF-128G-GNCIN) [Newest Version]","confirmerId":99,"authorId":99,"confirmed":1,"imgUrl":"https://images-na.ssl-images-amazon.com/images/I/51JR5142wZL.jpg","titleEn":"Amazon - $38.99 ($59.99) SanDisk Extreme 128GB SDXC UHS-I Card (SDSDXVF-128G-GNCIN) [Newest Version]","price":"$38.99","confirmedTime":1541298652000,"createdTime":1541298652000,"id":{"id":10685426,"vendorId":3},"taskId":7124826,"startDate":1541383243000}},"user":{"id":217,"nickName":"sff","active":1,"email":"FANGFEI_SUN@JINBAG.COM","userId":217},"status":0},"score":1.999824490360925,"type":"article"},{"item":{"lastCmtTime":1541383243000,"followCount":0,"articleId":1178,"upCount":0,"description":"SanDisk是U盘、SD卡的主流品牌，产品覆盖面广，稳定好用。这个锦囊大家一起来说说他家的产品，系统也会及时发布25% Off 以上的Deal。","weight":0.0,"title":"Sandisk","good":0,"userId":217,"commentCount":64,"tags":"","resourceUrlUltimate":[],"inTime":1540344448000,"downCount":0,"shareCount":0,"top":0,"upIds":"","style":4,"viewCount":79,"window":{"productSale":"$44.24","sourceId":3,"productId":10559082,"lastCheckedTime":1541383212000,"availability":"in_stock","sourceProductId":"B01J5RH06K","productTitle":"SanDisk Extreme Pro 128GB SDXC UHS-I Card (SDSDXXG-128G-GN4IN)","vendor":{"vendorId":3,"vendorNameEn":"Amazon","vendorNameCh":"Amazon","vendorDescEn":"Online shopping from the earth's biggest selection of books, magazines, music, DVDs, videos, electronics, computers, software, apparel & accessories, shoes...","vendorDescCh":"全球著名购物平台","vendorLogoUrl":"amazon.png","readable":1,"vendorLogoWidth":109,"vendorLogoHeight":33,"vendorDomain":"amazon.com","currency":"U","language":"en"},"width":287,"productImageLink":"https://images-na.ssl-images-amazon.com/images/I/71YO9YWCONL._SY355_.jpg","productDescription":"[]","productPrice":"$57.32","height":355,"topProductPromoInfoVendor":{"shareTitleEn":"$43.99 ($57.32) SanDisk Extreme Pro 128GB SDXC UHS-I Card (SDSDXXG-128G-GN4IN)","confirmerId":99,"authorId":99,"confirmed":1,"imgUrl":"https://images-na.ssl-images-amazon.com/images/I/71YO9YWCONL._SY355_.jpg","titleEn":"Amazon - $43.99 ($57.32) SanDisk Extreme Pro 128GB SDXC UHS-I Card (SDSDXXG-128G-GN4IN)","price":"$43.99","confirmedTime":1540923754000,"createdTime":1540923754000,"id":{"id":10559082,"vendorId":3},"taskId":6714861,"startDate":1541383217000}},"user":{"id":217,"nickName":"sff","active":1,"email":"FANGFEI_SUN@JINBAG.COM","userId":217},"status":0},"score":1.999824456668533,"type":"article"},{"item":{"lastCmtTime":1541389745000,"followCount":0,"articleId":1106,"upCount":0,"description":"","weight":0.0,"title":"Amazon's Choice","good":0,"userId":99,"commentCount":2939,"tags":"","resourceUrlUltimate":[],"inTime":1525337480000,"downCount":0,"shareCount":0,"top":0,"upIds":"","style":4,"viewCount":648,"window":{"productSale":"$2.06","sourceId":3,"productId":10563486,"lastCheckedTime":1541382736000,"availability":"in_stock","sourceProductId":"B000F5TTE8","productTitle":"Gardner Bender 25-AWC WireGard Screw-On Wire Connector Assortment, 22-10Wire Gauge (AWG), 600-1000V Max, 25 Resealable Pk., Blue, Grey, Orange, Red, & Yellow","vendor":{"vendorId":3,"vendorNameEn":"Amazon","vendorNameCh":"Amazon","vendorDescEn":"Online shopping from the earth's biggest selection of books, magazines, music, DVDs, videos, electronics, computers, software, apparel & accessories, shoes...","vendorDescCh":"全球著名购物平台","vendorLogoUrl":"amazon.png","readable":1,"vendorLogoWidth":109,"vendorLogoHeight":33,"vendorDomain":"amazon.com","currency":"U","language":"en"},"width":355,"productImageLink":"https://images-na.ssl-images-amazon.com/images/I/71Iu7HGM69L._SX355_.jpg","productDescription":"[]","productPrice":"$4.19","height":236,"topProductPromoInfoVendor":{"shareTitleEn":"$2.06 ($4.19) Gardner Bender 25-AWC WireGard Screw-On Wire Connector Assortment, 22-10Wire Gauge (AWG), 600-1000V Max, 25 Resealable Pk., Blue, Grey, Orange, Red, & Yellow","confirmerId":99,"authorId":99,"confirmed":1,"imgUrl":"https://images-na.ssl-images-amazon.com/images/I/71Iu7HGM69L._SX355_.jpg","titleEn":"Amazon - $2.06 ($4.19) Gardner Bender 25-AWC WireGard Screw-On Wire Connector Assortment, 22-10Wire Gauge (AWG), 600-1000V Max, 25 Resealable Pk., Blue, Grey, Orange, Red, & Yellow","price":"$2.06","confirmedTime":1541382749000,"createdTime":1541382749000,"id":{"id":10563486,"vendorId":3},"taskId":6791304,"startDate":1541382752000}},"user":{"id":99,"nickName":"Genie","active":1,"userId":99},"status":0},"score":1.999823853393122,"type":"article"}],"num":10,"lifeCycle":1}



{
    "user":"299",
    "blacklistItems":[],
    "blacklistArticle":[1096],
    "from":0,
    "num":10,
    "blacklist":[],
    "fields":[{"name":"status","values":[0]}],
    "articleFilter":[],
    "type":"all",
    "language":"en"
}



{
    "user":"299",
    "blacklistItems":[1362,1180,486,1092,1386,1370,1290,814,14,162,1210,324,1212,1094,1106,44,486,1092,324,1362,438,1290,1102,64,162,14,1180,814,1370,1212,1178,1210,426,1098,556,322,398,1386,740,1296,804,248,1118,442],
    "blacklistArticle":[1096],
    "from":0,
    "num":10,
    "blacklist":[],
    "fields":[{"name":"status","values":[0]}],
    "articleFilter":[],
    "type":"all",
    "language":"en"
}





{
    "user":"776",
    "blacklistItems":[1362,1180,486,1092,1386,1370,1290,814,14,162,1210,324,1212,1094,1106,44,486,1092,324,1362,438,1290,1102,64,162,14,1180,814,1370,1212,1178,1210,426,1098,556,322,398,1386,740,1296,804,248,1118,442],
    "blacklistArticle":[1096],
    "from":0,
    "num":10,
    "blacklist":[],
    "fields":[{"name":"status","values":[0]}],
    "articleFilter":[],
    "type":"all",
    "language":"en"
}


2018-11-07 11:50:29.960  INFO 22657 --- [nio-9124-exec-1] PIOInterface.api.v2.ItemListController   : /v3/ur/brochure, Param = 
{
    "user":"3d9464a48f0dffa2",
    "blacklistItems":[1362,1290,1106,14,486,1178,814,162,1370,1386,1092,1094,1102,1292,1298,1300,1118,1180,1296,1288,1304,1098,1374,568,472,1122,356,1112,420,1272,990,816,1108,1116,1114,1110,1358,1212,418,1158,1154,1150,1100,1104,1168,1144,278,1282,1152,1170,1148,1164,1174,1278,1156,1276,1270,1268,922,824,1176,378,1140,360,690,580,1030,324,1266,1260,1258,1256,1146,1254,1210,1058,1060,1056,1050,1052,1048,1054,1040,1042,1044,1046,1032,1034,1036,1038,1024,1026,1028,1022,1014,1016,1018,1020,1004,1006,1008,1010,1012,996,998,1000,1002,992,994,988,978,980,982,984,986,976,970,972,974,962,964,966,960,952,954,944,946,968,958,936,940,942,926,956,948,950,938,928,930,934,920,932,918,924,912,914,916,910,900,902,904,906,896,898,892,894,882,884,886,888,908,890,880,874,876,878,868,872,866,870,864,856,858,860,862,848,850,852,854,844,840,842,846,832,834,838,830,836,822,826,818,820,804,806,808,810,812,800,802,796,798,788,790,794,778,780,792,784,786,782,772,770,776,762,774,768,764,766,752,754,758,744,756,760,746,748,750,736,738,740,742,734,726,728,730,732,720,724,718,708,710,722,712,714,716,704,706,700,702,692,694,696,698,688,684,686,676,680,682,668,678,674,670,658,662,664,666,650,672,660,656,654,652,640,644,648,642,646,632,634,636,638,624,626,628,630,622,614,620,616,618,608,612,606,610,598,600,602,604,592,596,588,590,594,582,584,586,576,578,572,574,562,564,566,570,560,558,546,548,550,552,536,554,544,540,538,542,528,532,520,530,534,522,524,526,512,514,516,518,510,502,504,506,508,496,498,500,494,488,484,490,492,480,482,476,478,468,470,474,464,466,460,462,450,452,454,456,458,442,448,444,446,434,436,438,440,424,426,428,432,430,416,422,408,410,412,414,400,398,402,404,406,390,392,394,384,386,382,396,388,374,376,380,368,370,372,364,366,358,362,352,354,348,350,340,342,344,44,486,1092,1362,1094,1106,64,162,1102,1370,1358,1374,1144,1212,14,556,1118,1098,1168,1122,418,828,814],
    "blacklistArticle":[1096],
    "from":0,
    "num":10,
    "blacklist":[10866710,10094774,10867622,10867612,10579606,10616662,6232886,10413750,10563832,10685426,10860324,10860326,10860320,10583140,10860332,10860328,10867540,10860406,10141550,10552182,10860318,10860248,10860346,10559082,10563486,7936,10858832,10552848,10861516,10564678,10866842,10710436,10864572,10557622,10864488,10865848,10864352,10858988,10867382,10867390,10710388,10706272,10858808,10866836,10586992,6244464,10849254,10063454,8398520,10860460,10867404,10867406,10742834,10853476,10188138,10865306,10171544,8757268,6244202,10563772,10866938,10556150,10866886,10555000,10861150,10861588,10858748,10557822,4737998,10577162,10864386,10284852,10577972,10866608,10866462,10590388,10587294,10508890,10866456,8242024,6244372,10861686,10866426,10556836,6244480,6244552,10866160,10128302,10866256,10866252,10866228,10866226,10864708,10866216,10864576,10866212,10860002,10864216,6244330,10858790,10866038,6244358,10509650,10563868,10564112,10299060,10567694,10863068,213031,214245,214821,10859106,10859116,216815,213358,10859114,216876,214098,10859092,10859094,215285,10859090,216667,216059,213977,213592,623090,615028,217437,10859098,211964,216060,10862526,10562918,10543762,216824,10851476,10860292,10551872,10860826,10578994,10865522,10861340,10554952,10414378,10580044,10567466,10495644,10551662,10544224,10543662,10553374,10507436,10180456,10864706,10863336,10587280,10480396,10239572,10861362,10849134,10577774,10557838,10545844,10578056,10557954,10165670,10085052,10579816,10440328,10561192,9984996,10310138,10399060,10444582,10080390,10171238,10509264,10509256,10861636,10183032,10176704,10563090,10865836,10579898,10865772,10865792,10564792,10556698,10543612,10558966,10171852,10859512,10183072,7670662,10865216,10865220,150596,161188,10849090,10860556,163755,144808,10860558,149774,10860552,202702,10859446,10861758,2588282,10860554,10860200,10863622,10865210,387973,232516,4748610,164873,231816,387726,5660634,232974,4795908,150412,5666456,231959,5660866,232598,9667014,159188,4739346,5657162,5669962,231775,231773,5640116,4750378,10484792,4748768,450666,157164,10123946,4795902,10488,343356,154878,233087,231805,10860316,10860408,10865204,10862900,10865096,10865100],
    "fields":[{"name":"status","values":[0]}],
    "articleFilter":[],
    "type":"all",
    "language":"en"
}

2018-11-07 12:09:35.207  INFO 26567 --- [nio-9124-exec-5] PIOInterface.api.v2.ItemListController   : /v3/ur/brochure, Param = 
{
    "user":"3d9464a48f0dffa2",
    "blacklistItems":[1362,1290,1106,14,486,1178,814,162,1370,1386,1092,1094,1102,1292,1298,1300,1118,1180,1296,1288,1304,1098,1374,568,472,1122,356,1112,420,1272,990,816,1108,1116,1114,1110,1358,1212,418,1158,1154,1150,1100,1104,1168,1144,278,1282,1152,1156,1170,1148,1164,1174,1278,1276,1270,1268,922,1176,824,378,1140,360,690,580,1030,324,1266,1260,1258,1256,1146,1254,1210,1058,1060,1056,1048,1050,1052,1054,1044,1046,1042,1038,1034,1040,1032,1036,1024,1026,1028,1022,1014,1016,1018,1020,1008,1010,1012,1004,1006,998,1000,1002,996,994,988,978,982,984,986,970,992,980,976,972,974,962,966,968,952,964,960,954,958,944,946,948,950,936,956,938,940,942,928,930,932,934,926,918,920,924,912,914,916,910,900,902,906,904,908,896,898,892,894,882,884,886,888,890,880,874,876,878,866,868,870,872,856,864,860,858,848,850,854,840,842,862,852,844,846,832,834,836,838,830,822,826,818,820,804,806,808,810,812,796,798,800,802,790,792,794,784,778,780,788,770,772,774,776,768,762,764,786,782,756,752,754,760,744,746,766,758,748,750,736,740,734,726,738,742,728,732,730,722,724,718,708,720,710,714,716,704,706,700,702,692,712,694,698,684,686,676,678,680,696,688,672,668,670,660,662,682,674,664,666,652,654,650,640,658,656,644,646,648,636,638,634,642,632,624,626,628,614,616,618,630,622,608,612,610,606,598,600,602,620,592,594,588,590,582,586,604,596,576,572,574,562,564,566,584,578,560,558,554,548,550,552,570,546,536,538,540,542,528,532,544,520,522,524,526,512,514,516,530,534,510,502,504,508,496,494,518,506,500,484,488,490,492,478,498,482,476,468,470,474,464,460,480,462,450,452,454,456,458,444,442,466,448,434,436,438,440,424,426,428,446,432,430,416,422,408,410,412,398,414,400,402,404,406,390,392,394,382,396,384,386,388,374,376,380,368,364,366,370,372,358,362,352,354,348,350,338,340,342,344,330,332,334,322,326,328,346,336,1142,1172,1166,1162,1160,120,290,292,284,222,276,1280,256,1,288,286,268,258,2,260,4,262,6,8,272,16,18,22,264,10,12,270,52,54,24,58,266,26,282,28,80,66,20,1302,72,74,60,76,78,62,1360,98,82,84,86,88,90,92,94,96,112,102,1384,104,106,1388,108,110,128,114,132,116,100,118,122,124,126,144,146,130,164,134,136,138,154,156,142,176,178,166,168,184,186,172,174,190,208,192,194,210,212,214,182,200,202,206,240,242,228,244,230,246,216,218,234,236,248,250,254,252,44,486,1092,1362,1094,1106,64,162,1102,1370,1358,1374,1144,1212,14,556,1118,1098,1168,1122,418,828,814],
    "blacklistArticle":[1096],
    "from":0,
    "num":10,
    "blacklist":[10866710,10094774,10867622,10867612,10579606,10616662,6232886,10413750,10563832,10685426,10860324,10860326,10860320,10583140,10860332,10860328,10867540,10860406,10141550,10552182,10860318,10860248,10860346,10559082,10563486,7936,10858832,10552848,10861516,10564678,10866842,10710436,10864572,10557622,10864488,10865848,10864352,10858988,10867382,10867390,10710388,10706272,10858808,10866836,10586992,6244464,10849254,10063454,8398520,10860460,10867404,10867406,10742834,10853476,10188138,10865306,10171544,8757268,6244202,10563772,10866938,10556150,10866886,10555000,10861150,10861588,10858748,10557822,4737998,10577162,10864386,10284852,10577972,10866608,10866462,10590388,10587294,10508890,10866456,8242024,6244372,10861686,10866426,10556836,6244480,6244552,10866160,10128302,10866256,10866252,10866228,10866226,10864708,10866216,10864576,10866212,10860002,10864216,6244330,10858790,10866038,6244358,10509650,10563868,10564112,10299060,10567694,10863068,213031,214245,214821,10859106,10859116,216815,213358,10859114,216876,214098,10859092,10859094,215285,10859090,216667,216059,213977,213592,623090,615028,217437,10859098,211964,216060,10862526,10562918,10543762,216824,10851476,10860292,10551872,10860826,10578994,10865522,10861340,10554952,10414378,10580044,10567466,10495644,10551662,10544224,10543662,10553374,10507436,10180456,10864706,10863336,10587280,10480396,10239572,10861362,10849134,10577774,10557838,10545844,10578056,10557954,10165670,10085052,10579816,10440328,10561192,9984996,10310138,10399060,10444582,10080390,10171238,10509264,10509256,10861636,10183032,10176704,10563090,10865836,10579898,10865772,10865792,10564792,10556698,10543612,10558966,10171852,10859512,10183072,7670662,10865216,10865220,150596,161188,10849090,10860556,163755,144808,10860558,149774,10860552,202702,10859446,10861758,2588282,10860554,10860200,10863622,10865210,387973,232516,4748610,164873,231816,387726,5660634,232974,4795908,150412,5666456,231959,5660866,232598,9667014,159188,4739346,5657162,5669962,231775,231773,5640116,4750378,10484792,4748768,450666,157164,10123946,4795902,10488,343356,154878,233087,231805,10860316,10860408,10865204,10862900,10865096,10865100],
    "fields":[{"name":"status","values":[0]}],
    "articleFilter":[],
    "type":"all",
    "language":"en"
}, 

Result = {"items":[],"num":0,"lifeCycle":1,"hasMoreData":false,"blacklistProduct":[]}



2018-11-07 14:05:49.399  INFO 30376 --- [nio-9124-exec-6] PIOInterface.api.v2.ItemListController   : /v3/ur/brochure, Param = 

{
    "user":"299",
    "blacklistItems":[1362,1290,1106,14,486,1178,814,162,1370,1386,1092,1094,1102,1292,1298,1300,1118,1180,1296,1288,1304,1098,1374,568,472,1122,356,1112,420,1272,990,816,1108,1116,1114,1110,1358,1212,418,1158,1154,1150,1100,1104,1168,1144,278,1282,1152,1156,1170,1148,1164,1174,1278,1276,1268,922,824,1176,378,1140,324,1210,1270,690,360,580,1030,1266,1260,1258,1146,1254,1058,1060,1048,1050,1052,1256,1056,1054,1040,1042,1044,1046,1032,1034,1036,1038,1024,1026,1028,1022,1014,1016,1018,1020,1004,1008,1012,1006,996,998,1000,1002,992,1010,988,978,982,984,986,972,970,994,980,976,974,962,964,966,968,952,954,960,956,958,944,946,948,950,936,938,940,942,928,930,932,934,926,918,920,924,910,912,914,916,900,902,904,908,894,906,898,892,882,884,886,888,890,874,896,880,876,866,868,870,872,856,858,878,864,862,848,850,852,854,842,860,840,844,846,832,834,836,838,830,822,826,818,820,804,806,808,810,812,796,798,800,802,788,790,792,794,784,778,780,782,786,772,774,776,768,762,764,766,752,770,754,756,758,760,744,748,734,746,750,736,738,740,742,726,728,730,732,720,722,724,718,708,710,712,714,716,700,704,706,702,692,694,696,698,688,684,686,676,678,682,674,668,670,658,660,680,672,664,666,650,652,654,640,662,656,642,644,646,648,632,634,636,638,624,626,628,630,622,614,616,618,620,606,608,610,612,598,600,602,604,592,588,594,590,582,584,586,576,578,572,574,596,562,564,566,570,560,554,558,546,548,550,552,544,536,538,540,542,528,530,532,534,520,522,524,526,512,514,516,518,510,502,504,506,508,496,498,500,494,484,488,492,490,480,482,478,468,470,474,460,476,464,466,462,450,452,454,456,458,442,448,444,446,434,436,438,440,424,426,428,432,430,422,408,410,412,414,400,398,416,402,406,390,392,396,384,382,404,394,386,388,374,376,368,364,366,380,370,358,362,352,354,348,338,372,350,342,344,346,336,332,334,340,330,322,326,328,1142,1172,1166,1162,1160,120,292,288,286,284,276,268,256,290,222,1280,1,258,2,4,260,6,262,272,16,18,20,264,8,10,266,12,270,54,22,1302,24,282,26,60,28,80,1360,66,52,72,76,58,78,74,96,98,82,84,86,88,90,92,94,62,100,102,114,1384,1388,108,106,110,112,128,130,116,132,118,104,122,124,126,144,146,164,134,166,154,156,142,176,178,182,184,136,138,186,172,174,208,210,194,212,200,168,202,190,192,240,228,216,236,218,206,234,242,244,230,246,214,248,250,252,254,44,486,1092,1362,1094,1106,64,162,1102,1358,1370,1374,1144,14,556,1118,1098,1168,1122,828,814],
    "blacklistArticle":[1096],
    "from":0,
    "num":10,
    "blacklist":[10866710,10094774,10867622,10867612,10579606,10616662,6232886,10413750,10563832,10685426,10860324,10860326,10860320,10583140,10860332,10860328,10867540,10860406,10141550,10552182,10860318,10860248,10860346,10559082,10563486,7936,10858832,10552848,10861516,10564678,10866842,10710436,10864572,10557622,10864488,10865848,10864352,10858988,10867382,10867390,10710388,10706272,10858808,10866836,10586992,6244464,10849254,10063454,8398520,10860460,10867404,10867406,10742834,10853476,10188138,10865306,10171544,8757268,6244202,10563772,10866938,10556150,10866886,10555000,10861150,10861588,10858748,10557822,4737998,10577162,10864386,10284852,10577972,10866608,10866462,10590388,10587294,10508890,10866456,8242024,6244372,10861686,10866426,10556836,6244480,6244552,10866160,10128302,10866256,10866252,10866228,10866226,10864708,10866216,10864576,10866212,10860002,10864216,6244330,10858790,10866038,6244358,10509650,10563868,10564112,10299060,10567694,10863068,213031,214245,214821,10859106,10859116,216815,213358,10859114,216876,214098,10859092,10859094,215285,10859090,216667,216059,213977,213592,623090,615028,217437,10859098,211964,216060,10862526,10562918,10543762,216824,10851476,10860292,10551872,10860826,10578994,10865522,10861340,10554952,10414378,10580044,10567466,10495644,10551662,10544224,10543662,10553374,10507436,10180456,10864706,10863336,10587280,10480396,10239572,10861362,10849134,10577774,10557838,10545844,10578056,10557954,10165670,10085052,10579816,10440328,10561192,9984996,10310138,10399060,10444582,10080390,10171238,10509264,10509256,10861636,10183032,10176704,10563090,10865836,10579898,10865772,10865792,10564792,10556698,10543612,10558966,10171852,10859512,10183072,7670662,10865216,10865220,178182,161800,168456,10859176,177173,168474,168475,7691884,10861758,171548,204327,199204,168491,153128,6825026,168494,168493,185906,10860692,10859156,10860694,10859158,10860700,10860696,10859160,10860698,10859162,142397,9273038,9273550,150596,189514,168526,181326,168012,10120404,182354,147025,10851070,2588282,185440,168562,182389,159354,147065,199294,163456,149638,171655,142468,7679228,144526,180878,189072,201360,7131386,10178566,159392,10860550,181409,7873756,191140,7532762,10860556,10860558,10860552,10222646,4710644,10849298,165072,141014,10583670,170718,170719,6712504,7691946,335590,164582,160485,170731,179432,150257,141046,181496,205560,143612,190210,10859424,10219934,10859436,149774,192270,10859432,178959,145682,178962,190226,10859446,165142,178452,186645,168731,46876,178979,197922,181555,10525586,10859408,10859410,170819,10860522,8409552,181075,10078154,142167,185177,6794556,7853868,154462,168287,185183,168285,168802,185186,168291,185187,8476128,185184,168289,178529,207712,168295,185188,168293,185189,2589518,141680,150390,183681,2589092,10063642,179589,205706,150409,5176256,948124,6333426,179606,195480,185254,167335,185255,10853120,143268,154532,161188,335277,163755,144808,151464,7131586,168371,207286,180148,168373,948150,195000,6711258,149436,141250,168386,183234,168387,167873,168390,168391,168388,195012,168389,168394,168395,168392,183753,168398,194510,168399,202702,168396,168397,168400,195536,10859378,168414,151007,168415,10859386,168413,1906170,10849090,10859340,4815776,10859342,168434,168435,7532928,10859344,201722,10860554,10860200,10863622,10865210,387973,10860322,4748610,164873,231816,387726,10860334,5660634,232974,150412,10860202,10860330,10859444,10860340,10860342,231959,5660866,232598,10860336,10860338,10860348,10860350,5657162,5669962,10860344,10860420,10860422,10860416,10484792,10860418,4748768,10860428,10860430,10860424,10123946,10860308,10860310,10860432,4795902,343356,10860316,10860312,10860314,232516,4795908,5666456,10860404,9667014,10860400,159188,10860402,10860412,4739346,10860414,231775,10860408,231773,10860410,5640116,4750378,450666,157164,10860244,10488,154878,233087,231805,10865204,10862900,10865096,10865100],
    "fields":[{"name":"status","values":[0]}],
    "articleFilter":[],
    "type":"all",
    "language":"en"
}

