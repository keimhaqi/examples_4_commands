-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Host: 96.90.248.212:3306
-- Generation Time: Jul 06, 2018 at 06:25 AM
-- Server version: 5.7.12-log
-- PHP Version: 7.0.30-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `jinbag`
--

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `product_id` bigint(11) NOT NULL,
  `category_type_id` int(11) NOT NULL DEFAULT '0',
  `product_title` varchar(500) NOT NULL,
  `product_image_link` varchar(250) NOT NULL,
  `product_detail` varchar(1000) NOT NULL,
  `product_description` varchar(1000) NOT NULL,
  `product_price` varchar(100) NOT NULL,
  `product_sale` varchar(100) NOT NULL,
  `last_checked_time` datetime NOT NULL DEFAULT '2017-01-01 00:00:00',
  `brand_id` int(11) DEFAULT NULL,
  `source_id` int(11) NOT NULL,
  `width` int(11) NOT NULL,
  `height` int(11) NOT NULL,
  `more_pictures` tinyint(1) NOT NULL DEFAULT '0',
  `has_smart_price` tinyint(1) NOT NULL DEFAULT '0',
  `availability` int(2) NOT NULL DEFAULT '0',
  `onSale` int(1) NOT NULL DEFAULT '0',
  `source_product_id` varchar(50) NOT NULL,
  `product_link` varchar(250) NOT NULL DEFAULT '',
  `coupon_price` varchar(100) DEFAULT NULL,
  `more_resolutions` tinyint(1) DEFAULT NULL,
  `ch_table_available` tinyint(1) DEFAULT NULL,
  `page_title` varchar(1000) NOT NULL DEFAULT '',
  `category_type_priority` int(11) DEFAULT NULL,
  `product_keywords` varchar(1000) DEFAULT NULL,
  `history_low_price` varchar(100) DEFAULT NULL,
  `confirmed_msrp` varchar(100) DEFAULT NULL,
  `deleted` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`product_id`, `category_type_id`, `product_title`, `product_image_link`, `product_detail`, `product_description`, `product_price`, `product_sale`, `last_checked_time`, `brand_id`, `source_id`, `width`, `height`, `more_pictures`, `has_smart_price`, `availability`, `onSale`, `source_product_id`, `product_link`, `coupon_price`, `more_resolutions`, `ch_table_available`, `page_title`, `category_type_priority`, `product_keywords`, `history_low_price`, `confirmed_msrp`, `deleted`) VALUES
(1, 11, 'Stretch Cotton Dog Polo Shirt', 'http://www.ralphlauren.com', '["Ribbed polo collar. Two-button placket.","Short sleeves with ribbed armbands. Uneven vented hem.","\\"3\\" patch at the right sleeve. Our signature embroidered Big Pony accents the back.","Discreet leash hole at the back.","98% cotton, 2% elastane.","Machine washable.","Imported."]', '["This cotton mesh polo shirt is made with a hint of stretch to keep your canine comfortable and is finished with our signature embroidered Big Pony at the back."]', '$40.00', '$19.99', '2017-01-01 00:00:00', 5193, 2, 590, 470, 0, 0, 1, 1, '69105626', 'http://www.ralphlauren.com/product/index.jsp?productId=69105626', '', 0, NULL, 'Stretch Cotton Dog Polo Shirt - For the Pet   Home - RalphLauren.com', 8, '', NULL, NULL, 0),
(2, 631, 'ARTWORK Seaton Delaval Stables', 'http://www.ralphlauren.com/graphics/product_images/pPOLO2-10609010_standard_v360x480.jpg', '["William Curtis Rolf has photographed the architectural and cultural details of Britain and France and has published books on British and French stables. His prints are in fine collections worldwide, and he has had exhibitions in the US, France and Japan.","This image was specially selected by Ralph Lauren\'s art acquisition team and made available through an exclusive partnership with Getty Images and Conde Nast.","Image: 12\\" L x 12\\" W. Silver frame: 19\\" L x 19\\" W. This item is non-returnable."]', '["The Seaton Delaval stables, located in Northumberland, England, were built in 1762 and designed by architect Sir John Vanbrugh for Admiral George Delaval. The stables were a wonderful architectural afterthought, finished 30 years after Vanbrugh completed the house in 1732. This timeless photograph was taken by William Curtis Rolf as part of his collection of British and French stable images."]', '$695.00', '$695.00', '2017-01-01 00:00:00', 0, 2, 360, 480, 0, 0, 0, 0, '11786255', 'https://www.ralphlauren.com/product/index.jsp?productId=11786255', '', 0, NULL, 'Seaton Delaval Stables - Artwork   Home - RalphLauren.com', 8, '', NULL, NULL, 0),
(3, 11, 'Paul Smith Mixed Charm Printed Swim Trunks', 'https://image.s5a.com/is/image/saks/0400093010160_500x500.jpg', '["Colorful mixed charm prints enhance these swim trunks. Elasticized waistband with drawstring closure. Angled slash pockets. Back zippered welt pocket. Recycled polyester/polyester. Machine wash. Made in Portugal."]', '["Mixed Charm Printed Swim Trunks"]', '$160.00', '$112.00', '2017-09-29 06:19:19', 3148, 13816, 300, 400, 0, 0, 0, 0, '', '', NULL, NULL, NULL, '', NULL, NULL, NULL, NULL, 0),
(4, 11, 'Orlebar Brown Felic Cotton Polo', 'https://image.s5a.com/is/image/saks/0400095253538_500x500.jpg', '["Short-sleeve cotton polo featuring a linear design. Spread collar. Short sleeves. Split hem. Cotton. Machine wash. Imported."]', '["Felic Cotton Polo"]', '', '', '2018-06-27 20:14:33', 6537, 13816, 300, 400, 0, 0, 2, 0, '845524447130579', '', NULL, NULL, NULL, '', NULL, NULL, '', NULL, 0),
(5, 1, 'Orlebar Brown Printed Swim Trunks', 'https://image.s5a.com/is/image/saks/0400095252942_500x500.jpg', '["Woven shorts featuring geometric print design. Banded waist. Buckle tab at sides. Back zip pocket. Polyamide. Machine wash. Imported."]', '["Printed Swim Trunks"]', '$275.00', '$275.00', '2018-04-05 10:32:58', 6537, 13816, 300, 400, 0, 0, 0, 0, '845524447130608', '', NULL, NULL, NULL, '', NULL, NULL, '', NULL, 0),
(6, 1, 'Vilebrequin Baratin Shorts', 'https://image.s5a.com/is/image/saks/0400095156069_500x500.jpg', '["Buttoned shorts with botanical graphic design. .Belt loops. .Partially elasticized waistband. .Back flap pocket. .Zip fly with button closure. .Rise, about 10\\". .Inseam, about 9\\". .Polyamide. .Machine wash. .Imported."]', '["Baratin Shorts"]', '$230.00', '$230.00', '2017-11-26 14:36:18', 4066, 13816, 300, 400, 0, 0, 0, 0, '', '', NULL, NULL, NULL, '', NULL, NULL, NULL, NULL, 0),
(7, 11, 'Rivieras Long Sleeve Jacket', 'https://image.s5a.com/is/image/saks/0400088097483_500x500.jpg', '["Glossy long sleeve jacket for an uber cool look. Spread collar. Buttoned front with concealed zipper. Long sleeves. Slash pockets. Lined. About 38\\" from shoulder to hem. Polyester. Dry clean. Imported."]', '["Long Sleeve Jacket"]', '$650.00', '$243.75', '2018-01-21 14:14:34', 18245, 13816, 300, 400, 0, 0, 0, 0, '845524446871961', '', NULL, NULL, NULL, '', NULL, NULL, NULL, NULL, 0),
(8, 1, 'RALPH LAUREN HOME Where\'s Spot?', 'http://www.ralphlauren.com/graphics/product_images/pPOLO2-16755161_standard_v360x480.jpg', '["24 pages. 9\\" L x 8½\\" W.","Hardcover.","This item is not eligible for promotional discounts."]', '["It\'s time to celebrate Spot\'s 30th birthday! For three decades, children have been looking everywhere for Spot in this classic, lift-the-flap book, the first of its kind. Is he in the piano? Is he under the stairs? After the reader finds other familiar animals, there Spot is in his basket! A bold, colorful anniversary seal is a splendid way to dress up this perennial favorite."]', '$12.99', '$12.99', '2017-01-01 00:00:00', 4253, 2, 360, 480, 1, 0, 0, 0, '23841866', 'https://www.ralphlauren.com/product/index.jsp?productId=23841866', '', 0, NULL, 'Where\'s Spot? - Baby Books    The Book Shop - RalphLauren.com', 8, '', NULL, NULL, 0),
(9, 11, 'Orlebar Brown Plain Cotton Tee', 'https://image.s5a.com/is/image/saks/0400095254231_500x500.jpg', '["Short-sleeve cotton tee with minimalistic design.V-neck. Short sleeves. Curved hem. Cotton. Machine wash. Imported."]', '["Plain Cotton Tee"]', '$95.00', '$95.00', '2017-12-19 14:04:45', 6537, 13816, 300, 400, 0, 0, 0, 0, '', '', NULL, NULL, NULL, '', NULL, NULL, NULL, NULL, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`product_id`),
  ADD KEY `product_title_idx` (`product_title`),
  ADD KEY `brand_id_idx` (`brand_id`),
  ADD KEY `merge_column_idx` (`brand_id`,`product_title`),
  ADD KEY `merge_column_idx2` (`source_id`,`source_product_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `product_id` bigint(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10849327;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
