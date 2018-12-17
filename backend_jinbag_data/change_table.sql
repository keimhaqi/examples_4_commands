ALTER TABLE `jinbag_data`.`product_sku_saks` 
ADD COLUMN `coupon_price` varchar(100) NULL AFTER `product_sale`,
ADD COLUMN `linkshare_checked_time` datetime(0) NULL;

ALTER TABLE `jinbag_data`.`product_sku_amazon` 
ADD COLUMN `coupon_price` varchar(100) NULL AFTER `product_sale`,
ADD COLUMN `linkshare_checked_time` datetime NULL;

ALTER TABLE `jinbag_data`.`product_sku_amazon_cn` 
ADD COLUMN `coupon_price` varchar(100) NULL AFTER `product_sale`,
ADD COLUMN `linkshare_checked_time` datetime NULL;

ALTER TABLE `jinbag_data`.`product_sku_bloomingdales` 
ADD COLUMN `coupon_price` varchar(100) NULL AFTER `product_sale`,
ADD COLUMN `linkshare_checked_time` datetime NULL;


ALTER TABLE `jinbag_data`.`product_sku_kohls` 
ADD COLUMN `coupon_price` varchar(100) NULL AFTER `product_sale`,
ADD COLUMN `linkshare_checked_time` datetime NULL;


ALTER TABLE `jinbag_data`.`product_sku_lastcall` 
ADD COLUMN `coupon_price` varchar(100) NULL AFTER `product_sale`,
ADD COLUMN `linkshare_checked_time` datetime NULL;


ALTER TABLE `jinbag_data`.`product_sku_macys` 
ADD COLUMN `coupon_price` varchar(100) NULL AFTER `product_sale`,
ADD COLUMN `linkshare_checked_time` datetime NULL;


ALTER TABLE `jinbag_data`.`product_sku_neimanmarcus` 
ADD COLUMN `coupon_price` varchar(100) NULL AFTER `product_sale`,
ADD COLUMN `linkshare_checked_time` datetime NULL;


ALTER TABLE `jinbag_data`.`product_sku_nordstrom` 
ADD COLUMN `coupon_price` varchar(100) NULL AFTER `product_sale`,
ADD COLUMN `linkshare_checked_time` datetime NULL;

ALTER TABLE `jinbag_data`.`product_sku_saksoff` 
ADD COLUMN `coupon_price` varchar(100) NULL AFTER `product_sale`,
ADD COLUMN `linkshare_checked_time` datetime NULL;

ALTER TABLE `jinbag_data`.`product_sku_striderite` 
ADD COLUMN `coupon_price` varchar(100) NULL AFTER `product_sale`,
ADD COLUMN `linkshare_checked_time` datetime NULL;

ALTER TABLE `jinbag_data`.`product_sku_walmart` 
ADD COLUMN `coupon_price` varchar(100) NULL AFTER `product_sale`,
ADD COLUMN `linkshare_checked_time` datetime NULL;