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

CREATE TABLE `semi_product` (
  `id` bigint(11) NOT NULL,
  `product_id` bigint(11) NOT NULL,
  `in_product` tinyint(1) NOT NULL DEFAULT '0',
  `beginning_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `product_title` varchar(512) NOT NULL,
  `product_image_link` varchar(256) NOT NULL,
  `product_detail` varchar(1024) NOT NULL,
  `product_description` varchar(1024) NOT NULL,
  `product_price` varchar(32) NOT NULL,
  `product_sale` varchar(32) NOT NULL,
  `last_checked_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `brand_id` int(11) DEFAULT NULL,
  `source_id` int(11) NOT NULL,
  `width` int(11) NOT NULL,
  `height` int(11) NOT NULL,
  `more_pictures` tinyint(1) NOT NULL DEFAULT '0',
  `has_smart_price` tinyint(1) NOT NULL DEFAULT '0',
  `availability` int(2) NOT NULL DEFAULT '0',
  `source_product_id` varchar(64) NOT NULL,
  `product_link` varchar(256) NOT NULL DEFAULT '',
  `coupon_price` varchar(128) DEFAULT NULL,
  `more_resolutions` tinyint(1) DEFAULT NULL,
  `ch_table_available` tinyint(1) DEFAULT NULL,
  `page_title` varchar(1024) NOT NULL DEFAULT '',
  `product_keywords` varchar(1024) DEFAULT NULL,
  `history_low_price` varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `product`
--
--
-- Indexes for dumped tables
--

--
-- Indexes for table `product`
--
ALTER TABLE `semi_product`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `semi_product`
  MODIFY `id` bigint(11) NOT NULL AUTO_INCREMENT;
