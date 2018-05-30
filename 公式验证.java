//只考虑URScore和ESScore，其中变化的只有URScore，比较商品5和8
ProductId:5|ESScore:4.1247888|URScore:2.0|Score:6.124788761138916
ProductId:8|ESScore:4.1247888|URScore:0.0|Score:4.124788761138916
ProductId:9|ESScore:4.1247888|URScore:1.0|Score:5.124788761138916
ProductId:2|ESScore:4.1247888|URScore:1.0|Score:5.124788761138916
ProductId:4|ESScore:4.1247888|URScore:1.0|Score:5.124788761138916
ProductId:6|ESScore:4.1247888|URScore:2.0|Score:6.124788761138916
ProductId:1|ESScore:4.1247888|URScore:1.0|Score:5.124788761138916
ProductId:7|ESScore:4.1247888|URScore:2.0|Score:6.124788761138916
ProductId:3|ESScore:4.1247888|URScore:1.0|Score:5.124788761138916

//只考虑URScore、ESScore和Discount，其中变化的只有Discount，比较商品2和4
ProductId:5|ESScore:4.1247888|URScore:2.0|Discount:3.0|Score:9.124788761138916
ProductId:8|ESScore:4.1247888|URScore:0.0|Discount:5.0|Score:9.124788761138916
ProductId:9|ESScore:4.1247888|URScore:1.0|Discount:2.5|Score:7.624788761138916
ProductId:2|ESScore:4.1247888|URScore:1.0|Discount:4.5|Score:9.624788761138916
ProductId:4|ESScore:4.1247888|URScore:1.0|Discount:4.0|Score:9.124788761138916
ProductId:6|ESScore:4.1247888|URScore:2.0|Discount:2.0|Score:8.124788761138916
ProductId:1|ESScore:4.1247888|URScore:1.0|Discount:3.5|Score:8.624788761138916
ProductId:7|ESScore:4.1247888|URScore:2.0|Discount:1.5|Score:7.624788761138916
ProductId:3|ESScore:4.1247888|URScore:1.0|Discount:2.5|Score:7.624788761138916

//只考虑URScore、ESScore、Discount、TopProduct，其中，变化的只有TopProduct，比较商品14和8
ProductId:14|ESScore:1.0634974|URScore:0.0|Discount:5.0|TopProduct:1.0|Score:6.063497424125671
ProductId:5|ESScore:1.0634974|URScore:2.0|Discount:3.0|TopProduct:10.0|Score:60.634974241256714
ProductId:8|ESScore:1.0634974|URScore:0.0|Discount:5.0|TopProduct:10.0|Score:60.634974241256714
ProductId:9|ESScore:1.0634974|URScore:1.0|Discount:2.5|TopProduct:10.0|Score:45.634974241256714
ProductId:10|ESScore:1.0634974|URScore:0.0|Discount:1.0|TopProduct:10.0|Score:20.634974241256714
ProductId:2|ESScore:1.0634974|URScore:1.0|Discount:4.5|TopProduct:10.0|Score:65.63497424125671
ProductId:4|ESScore:1.0634974|URScore:1.0|Discount:4.0|TopProduct:10.0|Score:60.634974241256714
ProductId:6|ESScore:1.0634974|URScore:2.0|Discount:2.0|TopProduct:10.0|Score:50.634974241256714
ProductId:1|ESScore:1.0634974|URScore:1.0|Discount:3.5|TopProduct:10.0|Score:55.634974241256714
ProductId:7|ESScore:1.0634974|URScore:2.0|Discount:1.5|TopProduct:10.0|Score:45.634974241256714



//使用double保存计算结果，没有考虑DeltaConfirmedTime
//只考虑URScore、ESScore、Discount、TopProduct、DeltaConfirmedTime，其中变化的只有DeltaConfirmedTime，比较商品9和商品3
ProductId:5|ESScore:4.1247888|URScore:2.0|TopProduct:10.0|Discount:3.0|DeltaConfiremdTime:637795716|Score:91.24788762706815
ProductId:8|ESScore:4.1247888|URScore:0.0|TopProduct:10.0|Discount:5.0|DeltaConfiremdTime:474792716|Score:91.24788763245098
ProductId:9|ESScore:4.1247888|URScore:1.0|TopProduct:10.0|Discount:2.5|DeltaConfiremdTime:738684716|Score:76.24788762492673
ProductId:2|ESScore:4.1247888|URScore:1.0|TopProduct:10.0|Discount:4.5|DeltaConfiremdTime:548858716|Score:96.24788762960878
ProductId:4|ESScore:4.1247888|URScore:1.0|TopProduct:10.0|Discount:4.0|DeltaConfiremdTime:958411716|Score:91.24788762182308
ProductId:6|ESScore:4.1247888|URScore:2.0|TopProduct:10.0|Discount:2.0|DeltaConfiremdTime:1077186716|Score:81.2478876206726
ProductId:1|ESScore:4.1247888|URScore:1.0|TopProduct:10.0|Discount:3.5|DeltaConfiremdTime:717537716|Score:86.24788762532572
ProductId:7|ESScore:4.1247888|URScore:2.0|TopProduct:10.0|Discount:1.5|DeltaConfiremdTime:1149952716|Score:76.24788762008518
ProductId:3|ESScore:4.1247888|URScore:1.0|TopProduct:10.0|Discount:2.5|DeltaConfiremdTime:1063178716|Score:76.24788762079491












private double jinbagSort(ProductSkuBackend productSkuBackend, Map<Integer, Double> urItems, SearchHit hit){
    float disc = countDiscount(productSkuBackend.getDiscount());
    Date t1 = new Date();
    double topProduct = 1;
    double score = 0;
    long confiremdTime = 1;
    double urScore = 0;
    Double ur = urItems.get(Integer.parseInt(productSkuBackend.getId()));
    if(ur != null){
        urScore = ur.floatValue();
    }
    if (productSkuBackend.getTopProduct() != null && productSkuBackend.getTopProduct() == TRUE) {
        // 处理临时信息的公式逻辑
        if (productSkuBackend.getTopProductPromoInfoVendor() != null) {
            TopProductPromoInfoVendor topProductPromoInfoVendor = productSkuBackend.getTopProductPromoInfoVendor();
            if (topProductPromoInfoVendor.getConfirmedTime() != null) {
                confiremdTime = t1.getTime() - topProductPromoInfoVendor.getConfirmedTime();
            }
        }
        topProduct = 10;
        if(confiremdTime == 0.0) confiremdTime = 1;
        double confirmedFactor = 1.0 / confiremdTime;
        score = topProduct * (urScore + disc + hit.getScore() + confirmedFactor);
        logger.info("\nProductId:" + productSkuBackend.getId() + "|ESScore:" + hit.getScore()
                + "|URScore:" + urScore + "|TopProduct:" + topProduct + "|Discount:" + disc + "|DeltaConfiremdTime:" + confiremdTime + "|Score:" + score);
    } else {
        // 处理永久信息和普通promo的公式逻辑
        if(confiremdTime == 0.0) confiremdTime = 1;
        double confirmedFactor = 1.0 / confiremdTime;
        score = topProduct * (urScore + disc + hit.getScore() + confirmedFactor);
        logger.info("\nProductId:" + productSkuBackend.getId() + "|ESScore:" + hit.getScore()
                + "|URScore:" + urScore + "|TopProduct:" + topProduct + "|Discount:" + disc + "|DeltaConfiremdTime:" + confiremdTime + "|Score:" + score);
    }

    return score;

}



ProductId:10093506|ESScore:12.714941|URScore:0.0|TopProduct:10.0|Discount:4.5|DeltaConfiremdTime:149397083|Score:172.14941031473845
ProductId:10094772|ESScore:12.714941|URScore:0.0|TopProduct:10.0|Discount:4.5|DeltaConfiremdTime:65999074|Score:172.14941039932
ProductId:95888|ESScore:12.80321|URScore:0.0|TopProduct:10.0|Discount:4.5|DeltaConfiremdTime:584618640|Score:173.03210260194405

{
    "startTime":2018-01-17 01:53:07,
    "endTime":2018/1/17 9:53:8
}



10097810:饮水机 第82个
ProductId:10097810|ESScore:12.706205|URScore:0.0|TopProduct:10.0|Discount:1.5|DeltaConfiremdTime:194117|Score:142.06210519574316

{
    "startTime":
    "endTime":2018/1/17 10:14:16
}


10097808:化妆品 第11个
ProductId:10097808|ESScore:12.706205|URScore:0.0|TopProduct:10.0|Discount:4.0|DeltaConfiremdTime:480586|Score:167.06207448835022
{
    "startTime":2018-01-17 02:09:41
    "endTime":2018/1/17 10:9:41
}



10094772:中性笔 第1个
ProductId:10094772|ESScore:12.706205|URScore:0.0|TopProduct:10.0|Discount:4.5|DeltaConfiremdTime:67581582|Score:172.06205382838925
{
    "startTime":2018-01-16 07:31:20
    "endTime":2018/1/17 10:21:3
}


10097806: 搅拌机 第34个
ProductId:10097806|ESScore:12.706205|URScore:0.0|TopProduct:10.0|Discount:3.0|DeltaConfiremdTime:1474625|Score:157.062060461805
{
    "startTime":2018-01-17 01:53:07
    "endTime":2018/1/17 10:21:3
}