-- MySQL dump 10.15  Distrib 10.0.34-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: diamond
-- ------------------------------------------------------
-- Server version	10.0.34-MariaDB-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `diamond`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `diamond` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `diamond`;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categories` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `category` varchar(12) NOT NULL,
  `description` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'女式皮带',NULL),(2,'男式皮带',NULL),(3,'男款双肩包',NULL),(4,'男款商务公文包',NULL),(5,'男式单肩包/斜挎包',NULL),(6,'男款钥匙包',NULL),(7,'男款手拿包',NULL),(8,'男款钱包',NULL),(9,'男款驾证包',NULL),(10,'男款卡包/名片包',NULL),(11,'女款手拿包',NULL),(12,'女款钱包',NULL),(13,'女式单肩/斜挎包',NULL),(14,'女款手提包',NULL),(15,'女款钥匙包',NULL),(16,'旅行包',NULL),(17,'女款双肩包',NULL);
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `factory`
--

DROP TABLE IF EXISTS `factory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `factory` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `no` varchar(12) NOT NULL,
  `name` varchar(12) DEFAULT NULL,
  `description` varchar(36) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `no` (`no`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `factory`
--

LOCK TABLES `factory` WRITE;
/*!40000 ALTER TABLE `factory` DISABLE KEYS */;
/*!40000 ALTER TABLE `factory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gender`
--

DROP TABLE IF EXISTS `gender`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gender` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `sex` varchar(6) NOT NULL,
  `description` varchar(24) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gender`
--

LOCK TABLES `gender` WRITE;
/*!40000 ALTER TABLE `gender` DISABLE KEYS */;
INSERT INTO `gender` VALUES (1,'男士','男性'),(2,'女士','女性'),(3,'中性','男女皆宜');
/*!40000 ALTER TABLE `gender` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `material`
--

DROP TABLE IF EXISTS `material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `material` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `material` varchar(8) NOT NULL,
  `description` varchar(24) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `material`
--

LOCK TABLES `material` WRITE;
/*!40000 ALTER TABLE `material` DISABLE KEYS */;
INSERT INTO `material` VALUES (1,'头层牛皮（革）','真皮、头层牛皮'),(2,'二层牛皮（革）','二层皮、剖层皮'),(3,'涤纶','');
/*!40000 ALTER TABLE `material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prices`
--

DROP TABLE IF EXISTS `prices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prices` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `product_id` int(10) unsigned NOT NULL,
  `sale_channel_id` int(10) unsigned NOT NULL,
  `price` decimal(8,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_prices_products_idx` (`product_id`),
  KEY `fk_prices_sale_channels_idx` (`sale_channel_id`),
  CONSTRAINT `fk_prices_products` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_prices_sale_channels` FOREIGN KEY (`sale_channel_id`) REFERENCES `sale_channels` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prices`
--

LOCK TABLES `prices` WRITE;
/*!40000 ALTER TABLE `prices` DISABLE KEYS */;
/*!40000 ALTER TABLE `prices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `style_no` varchar(10) NOT NULL,
  `item_no` varchar(10) NOT NULL,
  `barcode` varchar(32) NOT NULL,
  `brand` varchar(45) DEFAULT NULL,
  `product_abbreviation` varchar(45) DEFAULT NULL,
  `category_id` int(10) unsigned NOT NULL,
  `gender_id` int(10) unsigned NOT NULL,
  `color` varchar(8) NOT NULL,
  `main_material_id` int(10) unsigned NOT NULL,
  `vice_material_id` int(10) unsigned DEFAULT NULL,
  `interior_material_id` int(10) unsigned DEFAULT NULL,
  `exterior_structure` varchar(45) DEFAULT NULL,
  `interior_structure` varchar(45) DEFAULT NULL,
  `open_mode` varchar(12) DEFAULT NULL,
  `length` decimal(4,2) DEFAULT NULL,
  `width` decimal(4,2) DEFAULT NULL,
  `height` decimal(4,2) DEFAULT NULL,
  `weight` decimal(6,2) DEFAULT NULL,
  `supplier_id` int(10) unsigned DEFAULT NULL,
  `factory_price` decimal(8,2) DEFAULT NULL,
  `cost_price` decimal(8,2) DEFAULT NULL,
  `tag_price` decimal(8,2) DEFAULT NULL,
  `retail_price` decimal(8,2) DEFAULT NULL,
  `original_item_no` varchar(10) DEFAULT NULL,
  `image` varchar(45) DEFAULT NULL,
  `feature` varchar(45) DEFAULT NULL,
  `comment` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `item_no_UNIQUE` (`item_no`),
  UNIQUE KEY `barcode_UNIQUE` (`barcode`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'H85228','H85228A','NH85228A','海森梅尔HORSEMEN','女式双肩包',17,2,'黑色',2,2,3,'前后各1个拉链袋  ','1个大容量袋、1个内壁拉链袋、2个小夹层','拉链',27.00,20.00,15.00,NULL,3,137.00,137.00,799.00,328.00,NULL,'H85228A.jpg',NULL,NULL),(2,'H85228','H85228D','NH85228D','海森梅尔HORSEMEN','女式双肩包',17,2,'粉红',2,2,3,'前后各1个拉链袋   ','1个大容量袋、1个内壁拉链袋、2个小夹层','拉链',27.00,20.00,15.00,NULL,3,137.00,137.00,799.00,328.00,NULL,'H85228D.jpg',NULL,NULL);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sale_channels`
--

DROP TABLE IF EXISTS `sale_channels`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sale_channels` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `channel_name` varchar(8) NOT NULL,
  `description` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sale_channels`
--

LOCK TABLES `sale_channels` WRITE;
/*!40000 ALTER TABLE `sale_channels` DISABLE KEYS */;
INSERT INTO `sale_channels` VALUES (1,'POP平台','天猫、京东、淘宝、亚马逊、融易购'),(2,'京东自营','京东采销'),(3,'王府井商城','王府井网上商城'),(4,'唯品会','唯品会自营'),(5,'分销商','统一分销商售价');
/*!40000 ALTER TABLE `sale_channels` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplier`
--

DROP TABLE IF EXISTS `supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `supplier` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `supplier` varchar(12) NOT NULL,
  `description` varchar(36) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier`
--

LOCK TABLES `supplier` WRITE;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
INSERT INTO `supplier` VALUES (1,'星莲皮具厂','星莲'),(2,'东成皮具厂','东成'),(3,'欧罗迪皮具','');
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-08-11  7:19:28
