-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Host: 52.42.165.126:3306
-- Generation Time: May 30, 2018 at 04:29 AM
-- Server version: 5.7.22-0ubuntu0.16.04.1-log
-- PHP Version: 7.0.30-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `piwik_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `piwik_log_action`
--

CREATE TABLE `piwik_log_action` (
  `idaction` int(10) UNSIGNED NOT NULL,
  `name` text,
  `hash` int(10) UNSIGNED NOT NULL,
  `type` tinyint(3) UNSIGNED DEFAULT NULL,
  `url_prefix` tinyint(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `piwik_log_action`
--

INSERT INTO `piwik_log_action` (`idaction`, `name`, `hash`, `type`, `url_prefix`) VALUES
(1, 'Jinbag', 3032067318, 4, NULL),
(101, 'jinbag_id', 3858149512, 12, NULL),
(195, 'Thrive', 1293026513, 12, NULL),
(196, 'product_id', 1166304858, 12, NULL),
(197, 'channel_id', 1928700330, 12, NULL),
(199, 'data_id', 938844476, 12, NULL),
(200, 'datetime', 2482226890, 12, NULL),
(235, 'test piwik', 3080036527, 4, NULL),
(244, 'view', 4278037390, 12, NULL),
(246, 'collect', 2751881972, 12, NULL),
(248, 'order', 4113142680, 12, NULL),
(471, 'bought', 78198511, 12, NULL),
(585, 'screen/menu', 2221486035, 4, NULL),
(587, 'screen/view1/view2/Home', 1603139419, 4, NULL),
(589, 'screen/Home', 680048302, 4, NULL),
(594, 'exception/caught/Send a fake exception from my app', 3974168537, 4, NULL),
(599, 'View', 1590625456, 12, NULL),
(602, 'screen/home', 2293897616, 4, NULL),
(604, 'screen/view1/view2', 2128116781, 4, NULL),
(606, 'screen/home/detail', 2195120949, 4, NULL),
(1990, 'weixin:/private/setresult/SCENE_FETCHQUEUE&amp;eyJmdW5jIjoibG9nIiwicGFyYW1zIjp7Im1zZyI6Il9ydW5PbjNyZEFwaUxpc3QgOiBtZW51OnNoYXJlOnRpbWVsaW5lLG1lbnU6c2hhcmU6YXBwbWVzc2FnZSxvblZvaWNlUmVjb3JkRW5kLG9uVm9pY2VQbGF5QmVnaW4sb25Wb2ljZVBsYXlFbmQsb25Mb2NhbEltYWdlVXBsb2FkUHJvZ3Jlc3Msb25JbWFnZURvd25sb2FkUHJvZ3Jlc3Msb25Wb2ljZVVwbG9hZFByb2dyZXNzLG9uVm9pY2VEb3dubG9hZFByb2dyZXNzLG1lbnU6c2V0Zm9udCxtZW51OnNoYXJlOndlaWJvLG1lbnU6c2hhcmU6ZW1haWwsd3hkb3dubG9hZDpzdGF0ZV9jaGFuZ2UsaGRPbkRldmljZVN0YXRlQ2hhbmdlZCxhY3Rpdml0eTpzdGF0ZV9jaGFuZ2UifSwiX19tc2dfdHlwZSI6ImNhbGwiLCJfX2NhbGxiYWNrX2lkIjoiMTAwMCJ9', 1408753093, 4, NULL),
(2137, '268714', 625187455, 12, NULL),
(2140, 'screen/detail/Sanibel Twill Swim Trunk', 2654220271, 4, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `piwik_log_action`
--
ALTER TABLE `piwik_log_action`
  ADD PRIMARY KEY (`idaction`),
  ADD KEY `index_type_hash` (`type`,`hash`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `piwik_log_action`
--
ALTER TABLE `piwik_log_action`
  MODIFY `idaction` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16672;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
