-- ----------------------------
-- Table structure for article
-- ----------------------------
DROP TABLE IF EXISTS `article`;
CREATE TABLE `article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comment_count` int(11) DEFAULT NULL,
  `content` text,
  `down` int(11) DEFAULT NULL,
  `down_ids` text,
  `good` bit(1) DEFAULT NULL,
  `in_time` datetime NOT NULL,
  `last_comment_time` datetime DEFAULT NULL,
  `modify_time` datetime DEFAULT NULL,
  `tag` varchar(255) DEFAULT NULL,
  `title` varchar(255) NOT NULL,
  `top` bit(1) DEFAULT NULL,
  `up` int(11) DEFAULT NULL,
  `up_ids` text,
  `user_id` int(11) DEFAULT NULL,
  `view` int(11) NOT NULL,
  `weight` double DEFAULT '0',
  `user` tinyblob,
  `logo_url` varchar(255) DEFAULT NULL,
  `nick_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UK_2983inw6rc5ogqomaguywqy5x` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for article_product
-- ----------------------------
DROP TABLE IF EXISTS `article_product`;
CREATE TABLE `article_product` (
  `article_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for article_resource
-- ----------------------------
DROP TABLE IF EXISTS `article_resource`;
CREATE TABLE `article_resource` (
  `article_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT 0,
  `resource_url` varchar(255) DEFAULT NULL,
  `resource_type` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for article_tag
-- ----------------------------
DROP TABLE IF EXISTS `article_tag`;
CREATE TABLE `article_tag` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `tag_id` int(11) DEFAULT NULL,
  `article_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;


-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comment_id` int(11) DEFAULT NULL,
  `content` text NOT NULL,
  `down` int(11) NOT NULL,
  `down_ids` text,
  `in_time` datetime DEFAULT NULL,
  `article_id` int(11) DEFAULT NULL,
  `up` int(11) NOT NULL,
  `up_ids` text,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for follow
-- ----------------------------
DROP TABLE IF EXISTS `follow`;
CREATE TABLE `follow` (
  `id` varchar(19) NOT NULL,
  `follower_id` varchar(19) NOT NULL,
  `following_id` varchar(19) NOT NULL,
  `following_type` int(11) NOT NULL COMMENT '0: user, 1: tag, 2: article collect, 3: article watch',
  `in_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
