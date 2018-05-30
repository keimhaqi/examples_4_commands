                   float disc = countDiscount(productSkuBackend.getDiscount());
                   if(productSkuBackend.getTopProduct() != null && productSkuBackend.getTopProduct()){
                       itemlist.put(productSkuBackend, hit.getScore() * 10);
                       logger.info("\nProductId:" + productSkuBackend.getId() + "|ESScore:" + hit.getScore()
                               + "URScore:" + 0 + "|TopProduct:" + 10 + "|Discount:" + disc);
                   }else{
                       itemlist.put(productSkuBackend, hit.getScore());
                       logger.info("\nProductId:" + productSkuBackend.getId() + "|ESScore:" + hit.getScore()
                               + "URScore:" + 0 + "|TopProduct:" + 1 + "|Discount:" + disc);
                   }




                   float disc = countDiscount(productSkuBackend.getDiscount());
                   if(productSkuBackend.getTopProduct() != null && productSkuBackend.getTopProduct() == Boolean.TRUE){
                       // (urScore + discount * esScore) * topProduct
                       Double dou = urPreference.get(Integer.parseInt(productSkuBackend.getId()));
                       if(dou == null){
                           float score = (hit.getScore() * disc + 0) * 10;
                           logger.info("\nProductId:" + productSkuBackend.getId() + "|ESScore:" + hit.getScore()
                           + "|URScore:" + dou + "|TopProduct:" + 10 + "|Discount:" + disc + "|Score:" + score);
                           itemlist.put(productSkuBackend, score);
                       }else{
                           float score = (hit.getScore() * disc + dou.floatValue()) * 10;
                           itemlist.put(productSkuBackend, score);
                           logger.info("\nProductId:" + productSkuBackend.getId() + "|ESScore:" + hit.getScore()
                                   + "|URScore:" + 0 + "|TopProduct:" + 10 + "|Discount:" + disc + "|Score:" + score);
                       }
                   }else{
                       Double dou = urPreference.get(Integer.parseInt(productSkuBackend.getId()));
                       if(dou == null){
                           float score = (hit.getScore() * disc + 0);
                           itemlist.put(productSkuBackend, score);
                           logger.info("\nProductId:" + productSkuBackend.getId() + "|ESScore:" + hit.getScore()
                                   + "|URScore:" + dou + "|TopProduct:" + 1 + "|Discount:" + disc + "|Score:" + score);
                       }else{
                           float score = (hit.getScore() * disc + dou.floatValue());
                           itemlist.put(productSkuBackend, score);
                           logger.info("\nProductId:" + productSkuBackend.getId() + "|ESScore:" + hit.getScore()
                                   + "|URScore:" + 0 + "|TopProduct:" + 1 + "|Discount:" + disc + "|Score:" + score);
                       }
                   }


// update top_product_promo_info_vendor set product_id=1 where product_id=102265;
update top_product_promo_info_vendor set product_id=2 where product_id=130641;
update top_product_promo_info_vendor set product_id=3 where product_id=142167;
update top_product_promo_info_vendor set product_id=4 where product_id=233068;
update top_product_promo_info_vendor set product_id=5 where product_id=301054;
update top_product_promo_info_vendor set product_id=6 where product_id=312529;
update top_product_promo_info_vendor set product_id=7 where product_id=313187;
update top_product_promo_info_vendor set product_id=8 where product_id=422386;
update top_product_promo_info_vendor set product_id=9 where product_id=2623756;
update top_product_promo_info_vendor set product_id=10 where product_id=4800218;






update product set product_id=2 where product_id=39;
update product set product_id=3 where product_id=40;
update product set product_id=4 where product_id=43;
update product set product_id=5 where product_id=44;
update product set product_id=6 where product_id=46;
update product set product_id=7 where product_id=48;
update product set product_id=8 where product_id=49;
update product set product_id=9 where product_id=50;
update product set product_id=10 where product_id=51;



ProductId:5|ESScore:4.117138|URScore:0|TopProduct:10.0|Discount:1.0|ConfiremdTime:471733042|Score:51.16926
ProductId:9|ESScore:4.117138|URScore:0|TopProduct:10.0|Discount:1.0|ConfiremdTime:572622042|Score:51.169632
ProductId:1|ESScore:4.117138|URScore:0|TopProduct:10.0|Discount:3.5|ConfiremdTime:551475042|Score:76.16957
ProductId:7|ESScore:4.117138|URScore:0|TopProduct:10.0|Discount:1.0|ConfiremdTime:983890042|Score:51.170364
ProductId:3|ESScore:4.117138|URScore:0|TopProduct:10.0|Discount:2.5|ConfiremdTime:897116042|Score:66.170265
ProductId:8|ESScore:3.1171377|URScore:0|TopProduct:10.0|Discount:1.0|ConfiremdTime:308730042|Score:41.16814
ProductId:2|ESScore:3.1171377|URScore:0|TopProduct:10.0|Discount:1.0|ConfiremdTime:382796042|Score:41.168766
ProductId:4|ESScore:3.1171377|URScore:0|TopProduct:10.0|Discount:1.0|ConfiremdTime:792349042|Score:41.170116
ProductId:6|ESScore:3.1171377|URScore:0|TopProduct:10.0|Discount:1.0|ConfiremdTime:911124042|Score:41.17028


2018-01-08 17:18:47.938  INFO 14425 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:19|ESScore:2.040358|URScore:0|TopProduct:1.0|Discount:2.5|ConfiremdTime:1|Score:3.540358
2018-01-08 17:18:47.940  INFO 14425 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:15|ESScore:2.040358|URScore:0|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:2.040358
2018-01-08 17:18:47.941  INFO 14425 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:13|ESScore:2.040358|URScore:0|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:2.040358
2018-01-08 17:18:47.942  INFO 14425 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:11|ESScore:2.040358|URScore:0|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:2.040358
2018-01-08 17:18:47.943  INFO 14425 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:17|ESScore:2.040358|URScore:0|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:2.040358
2018-01-08 17:18:47.944  INFO 14425 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:14|ESScore:1.0403581|URScore:0|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:1.0403581
2018-01-08 17:18:47.945  INFO 14425 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:12|ESScore:1.0403581|URScore:0|TopProduct:1.0|Discount:5.0|ConfiremdTime:1|Score:5.040358
2018-01-08 17:18:47.946  INFO 14425 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:20|ESScore:1.0403581|URScore:0|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:1.0403581
2018-01-08 17:18:47.947  INFO 14425 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:16|ESScore:1.0403581|URScore:0|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:1.0403581
2018-01-08 17:18:47.948  INFO 14425 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:18|ESScore:1.0403581|URScore:0|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:1.0403581


2018-01-08 17:23:00.015  INFO 15430 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:15|ESScore:2.040358|URScore:0|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:2.040358
2018-01-08 17:23:00.017  INFO 15430 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:13|ESScore:2.040358|URScore:0|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:2.040358
2018-01-08 17:23:00.018  INFO 15430 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:11|ESScore:2.040358|URScore:0|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:2.040358
2018-01-08 17:23:00.020  INFO 15430 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:17|ESScore:2.040358|URScore:0|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:2.040358
2018-01-08 17:23:00.023  INFO 15430 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:14|ESScore:1.0403581|URScore:0|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:1.0403581
2018-01-08 17:23:00.027  INFO 15430 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:19|ESScore:1.0403581|URScore:0|TopProduct:1.0|Discount:2.5|ConfiremdTime:1|Score:2.540358
2018-01-08 17:23:00.030  INFO 15430 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:12|ESScore:1.0403581|URScore:0|TopProduct:1.0|Discount:5.0|ConfiremdTime:1|Score:5.040358
2018-01-08 17:23:00.031  INFO 15430 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:20|ESScore:1.0403581|URScore:0|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:1.0403581
2018-01-08 17:23:00.033  INFO 15430 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:16|ESScore:1.0403581|URScore:0|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:1.0403581
2018-01-08 17:23:00.035  INFO 15430 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:18|ESScore:1.0403581|URScore:0|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:1.0403581


2018-01-08 17:46:35.685  INFO 21828 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:14|ESScore:2.040358|URScore:2.1|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:4.140358
2018-01-08 17:46:35.687  INFO 21828 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:19|ESScore:2.040358|URScore:2.11|TopProduct:1.0|Discount:2.5|ConfiremdTime:1|Score:5.6503577
2018-01-08 17:46:35.688  INFO 21828 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:12|ESScore:2.040358|URScore:2.11|TopProduct:1.0|Discount:5.0|ConfiremdTime:1|Score:8.150358
2018-01-08 17:46:35.689  INFO 21828 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:15|ESScore:2.040358|URScore:2.11|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:4.150358
2018-01-08 17:46:35.690  INFO 21828 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:13|ESScore:2.040358|URScore:2.11|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:4.150358
2018-01-08 17:46:35.691  INFO 21828 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:11|ESScore:2.040358|URScore:2.11|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:4.150358
2018-01-08 17:46:35.692  INFO 21828 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:17|ESScore:2.040358|URScore:2.11|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:4.150358
2018-01-08 17:46:35.693  INFO 21828 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:20|ESScore:1.0403581|URScore:0.0|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:1.0403581
2018-01-08 17:46:35.694  INFO 21828 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:16|ESScore:1.0403581|URScore:0.0|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:1.0403581
2018-01-08 17:46:35.694  INFO 21828 --- [nio-9123-exec-1] PIOInterface.backendQuery.SearchQuery    : 
ProductId:18|ESScore:1.0403581|URScore:0.0|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:1.0403581


2018-01-08 17:50:59.191  INFO 21828 --- [nio-9123-exec-2] PIOInterface.backendQuery.SearchQuery    : 
ProductId:14|ESScore:2.040358|URScore:2.1|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:4.140358
2018-01-08 17:50:59.197  INFO 21828 --- [nio-9123-exec-2] PIOInterface.backendQuery.SearchQuery    : 
ProductId:19|ESScore:2.040358|URScore:2.11|TopProduct:1.0|Discount:2.5|ConfiremdTime:1|Score:5.6503577
2018-01-08 17:50:59.215  INFO 21828 --- [nio-9123-exec-2] PIOInterface.backendQuery.SearchQuery    : 

ProductId:5|ESScore:2.040358|URScore:2.11|TopProduct:10.0|Discount:1.0|ConfiremdTime:474288177|Score:51.501472

2018-01-08 17:50:59.216  INFO 21828 --- [nio-9123-exec-2] PIOInterface.backendQuery.SearchQuery    : 

ProductId:9|ESScore:2.040358|URScore:2.11|TopProduct:10.0|Discount:1.0|ConfiremdTime:575177177|Score:51.501842

2018-01-08 17:50:59.217  INFO 21828 --- [nio-9123-exec-2] PIOInterface.backendQuery.SearchQuery    : 
ProductId:12|ESScore:2.040358|URScore:2.11|TopProduct:1.0|Discount:5.0|ConfiremdTime:1|Score:8.150358
2018-01-08 17:50:59.221  INFO 21828 --- [nio-9123-exec-2] PIOInterface.backendQuery.SearchQuery    : 
ProductId:15|ESScore:2.040358|URScore:2.11|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:4.150358
2018-01-08 17:50:59.222  INFO 21828 --- [nio-9123-exec-2] PIOInterface.backendQuery.SearchQuery    : 
ProductId:1|ESScore:2.040358|URScore:2.11|TopProduct:10.0|Discount:3.5|ConfiremdTime:554030177|Score:76.50177
2018-01-08 17:50:59.223  INFO 21828 --- [nio-9123-exec-2] PIOInterface.backendQuery.SearchQuery    : 
ProductId:7|ESScore:2.040358|URScore:2.11|TopProduct:10.0|Discount:1.0|ConfiremdTime:986445177|Score:51.502567
2018-01-08 17:50:59.223  INFO 21828 --- [nio-9123-exec-2] PIOInterface.backendQuery.SearchQuery    : 
ProductId:13|ESScore:2.040358|URScore:2.11|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:4.150358
2018-01-08 17:50:59.224  INFO 21828 --- [nio-9123-exec-2] PIOInterface.backendQuery.SearchQuery    : 
ProductId:3|ESScore:2.040358|URScore:2.11|TopProduct:10.0|Discount:2.5|ConfiremdTime:899671177|Score:66.502464










ProductId:5|ESScore:4.117138|URScore:2.11|TopProduct:10.0|Discount:1.0|ConfiremdTime:475302804|Score:72.26927
ProductId:9|ESScore:4.117138|URScore:2.11|TopProduct:10.0|Discount:1.0|ConfiremdTime:576191804|Score:72.26964
ProductId:1|ESScore:4.117138|URScore:2.11|TopProduct:10.0|Discount:3.5|ConfiremdTime:555044804|Score:97.26958
ProductId:7|ESScore:4.117138|URScore:2.11|TopProduct:10.0|Discount:1.0|ConfiremdTime:987459804|Score:72.27036
ProductId:3|ESScore:4.117138|URScore:2.11|TopProduct:10.0|Discount:2.5|ConfiremdTime:900685804|Score:87.27027
ProductId:8|ESScore:3.1171377|URScore:0.0|TopProduct:10.0|Discount:1.0|ConfiremdTime:312299804|Score:41.168175
ProductId:2|ESScore:3.1171377|URScore:0.0|TopProduct:10.0|Discount:1.0|ConfiremdTime:386365804|Score:41.16879
ProductId:4|ESScore:3.1171377|URScore:0.0|TopProduct:10.0|Discount:1.0|ConfiremdTime:795918804|Score:41.170124
ProductId:6|ESScore:3.1171377|URScore:0.0|TopProduct:10.0|Discount:1.0|ConfiremdTime:914693804|Score:41.170288





ProductId:5|ESScore:4.117138|URScore:2.11|TopProduct:10.0|Discount:1.0|ConfiremdTime:476117478|Score:72.273476
ProductId:9|ESScore:4.117138|URScore:2.11|TopProduct:10.0|Discount:1.0|ConfiremdTime:577006478|Score:72.27311
ProductId:1|ESScore:4.117138|URScore:2.11|TopProduct:10.0|Discount:3.5|ConfiremdTime:555859478|Score:97.27318
ProductId:7|ESScore:4.117138|URScore:2.11|TopProduct:10.0|Discount:1.0|ConfiremdTime:988274478|Score:72.272385
ProductId:3|ESScore:4.117138|URScore:2.11|TopProduct:10.0|Discount:2.5|ConfiremdTime:901500478|Score:87.272484
ProductId:8|ESScore:3.1171377|URScore:0.0|TopProduct:10.0|Discount:1.0|ConfiremdTime:313114478|Score:41.174576
ProductId:2|ESScore:3.1171377|URScore:0.0|TopProduct:10.0|Discount:1.0|ConfiremdTime:387180478|Score:41.173965
ProductId:4|ESScore:3.1171377|URScore:0.0|TopProduct:10.0|Discount:1.0|ConfiremdTime:796733478|Score:41.172634
ProductId:6|ESScore:3.1171377|URScore:0.0|TopProduct:10.0|Discount:1.0|ConfiremdTime:915508478|Score:41.17247


ProductId:14|ESScore:2.040358|URScore:2.1|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:4.140358
ProductId:19|ESScore:2.040358|URScore:2.11|TopProduct:1.0|Discount:2.5|ConfiremdTime:1|Score:5.6503577
ProductId:12|ESScore:2.040358|URScore:2.11|TopProduct:1.0|Discount:5.0|ConfiremdTime:1|Score:8.150358
ProductId:15|ESScore:2.040358|URScore:2.11|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:4.150358
ProductId:13|ESScore:2.040358|URScore:2.11|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:4.150358
ProductId:11|ESScore:2.040358|URScore:2.11|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:4.150358
ProductId:17|ESScore:2.040358|URScore:2.11|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:4.150358
ProductId:20|ESScore:1.0403581|URScore:0.0|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:1.0403581
ProductId:16|ESScore:1.0403581|URScore:0.0|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:1.0403581
ProductId:18|ESScore:1.0403581|URScore:0.0|TopProduct:1.0|Discount:1.0|ConfiremdTime:1|Score:1.0403581





















