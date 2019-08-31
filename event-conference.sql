-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: 127.0.0.1    Database: dbtest1
-- ------------------------------------------------------
-- Server version	8.0.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `activity_pictures`
--

DROP TABLE IF EXISTS `activity_pictures`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `activity_pictures` (
  `activity_id` int(11) NOT NULL,
  `picture_no` smallint(6) DEFAULT NULL,
  `picture_path` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Activity_picturescol` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `event_id` int(11) NOT NULL,
  PRIMARY KEY (`activity_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `activity_pictures`
--

LOCK TABLES `activity_pictures` WRITE;
/*!40000 ALTER TABLE `activity_pictures` DISABLE KEYS */;
/*!40000 ALTER TABLE `activity_pictures` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `advertisement`
--

DROP TABLE IF EXISTS `advertisement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `advertisement` (
  `advt_no` int(11) NOT NULL,
  `event_id` int(11) NOT NULL,
  `sponsor` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `advt_content` blob,
  `displayed_count` int(11) DEFAULT NULL,
  `advt_type` smallint(6) DEFAULT NULL COMMENT '1 - Banner\n2 - Interstitial',
  `last_displayed` datetime DEFAULT NULL,
  `frequency` int(11) DEFAULT NULL,
  `Advertisementcol` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Advertisementcol1` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Advertisementcol2` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Advertisementcol3` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Advertisementcol4` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Advertisementcol5` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`advt_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `advertisement`
--

LOCK TABLES `advertisement` WRITE;
/*!40000 ALTER TABLE `advertisement` DISABLE KEYS */;
/*!40000 ALTER TABLE `advertisement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `announcement`
--

DROP TABLE IF EXISTS `announcement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `announcement` (
  `announcement_no` int(11) NOT NULL,
  `event_id` int(11) NOT NULL,
  `announcement_text` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `announcement_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `announcement`
--

LOCK TABLES `announcement` WRITE;
/*!40000 ALTER TABLE `announcement` DISABLE KEYS */;
/*!40000 ALTER TABLE `announcement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attendee`
--

DROP TABLE IF EXISTS `attendee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `attendee` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `attendee_name` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `attendee_synopsis` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `attendee_email` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `attendee_contact_num` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `attendee_affiliation` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `attendee_linkedin_profile` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `attendee_areas_of_interest` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `attendee_links_to_research` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `attendee_first_login` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `attendee_research_websites` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `event_id` int(11) DEFAULT NULL,
  `attendee_password` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `attendee_facebook` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `attendee_twitter` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `attendee_tags` mediumtext COLLATE utf8mb4_unicode_ci,
  `prof_img` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `attendee_linkedin_profile_UNIQUE` (`attendee_linkedin_profile`)
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendee`
--

LOCK TABLES `attendee` WRITE;
/*!40000 ALTER TABLE `attendee` DISABLE KEYS */;
INSERT INTO `attendee` VALUES (10,'praveen','Praveen is a flutter develor.','praveenstark.india@gmail.com','9043961785',NULL,'https://www.linkedin.com/in/praveen-kumar-66aba317a','Coding and Market',NULL,NULL,'https://www.google.com/',1,'praveen007','https://www.facebook.com/praveenkumar','https://www.twitter.com','[\"Flutter\", \"vue.js\"]','10_Hotel-Promotional-Flyer-Template-440x570-1.jpg'),(11,'stark',NULL,'praveen@pk.com','12345',NULL,NULL,NULL,NULL,NULL,'https://www.google.com',1,'stark','https://www.facebook.com/praveenkumar','https://www.linkedin.com','[\"flutter\", \"dev ops\", \"python\", \"Testing\"]',NULL),(12,'sundhar',NULL,'sundhar@google.com','123456',NULL,NULL,NULL,NULL,NULL,NULL,1,'sundhar123','','',NULL,NULL),(13,'Thanos',NULL,'thanos@gmail.com','123',NULL,'https://www.facebook.com/dactsio',NULL,NULL,NULL,NULL,1,'thanos','https://www.facebook.com/dactsio/','https://www.facebook.com/dactsio/','[\"UxDev\"]',NULL),(14,'prasad','3Edge Solutions was established in 2006 as a Finishing School with the aim of transforming Engineering graduates into sought after IT professionals. Over the years, 3Edge has created strong partnerships in the industry that opened up various channels for employment of skilled resources. ','Prasad.kolisetty@gmail.com','9840818880',NULL,NULL,'Planning and marketting','[\"http://www.3edge.in\",\"http://www.google.com\"]',NULL,'3edge.in',1,'prasad','','','[\"flutter\",\"UxDev\"]',NULL),(15,'praveen',NULL,'praveen@gmail.com','9043961785',NULL,NULL,NULL,NULL,NULL,NULL,1,'pp','','',NULL,NULL),(16,'Sekar',NULL,'sekar@gmail.com','1254541245',NULL,NULL,NULL,NULL,NULL,NULL,1,'pp','','',NULL,NULL),(17,'Sandy',NULL,'sandy@gmail.com','1545421475',NULL,NULL,NULL,NULL,NULL,NULL,1,'pp','','',NULL,NULL),(18,'raja',NULL,'t.rajasekhar0707@gmail.com','8106600760',NULL,NULL,NULL,NULL,NULL,NULL,1,'raja',NULL,NULL,NULL,NULL),(19,'praveen',NULL,'praveendestraction@gmail.com','11',NULL,NULL,NULL,NULL,NULL,NULL,1,'kk',NULL,NULL,NULL,NULL),(22,'Praveen kumar',NULL,'praveenkumar@3edge.in','8667761244',NULL,'https://www.linkedin.com','To code flutter for IOT applications.','[\"https://www.dactsindia.ml\", \"https://www.google.com\"]',NULL,'https://www.google.com',1,'**********','https://www.facebook.com','https://www.twitter.com','[\"flutter\", \"devops\"]','22_iob.png'),(23,'Praveen kumar',NULL,'praveenkumar@3edge.inn','8667761244',NULL,NULL,NULL,NULL,NULL,NULL,1,'**********',NULL,NULL,NULL,NULL),(27,'Praveen kumar',NULL,'praveenkumar@3edge.m','8667761244',NULL,NULL,NULL,NULL,NULL,NULL,1,'**********',NULL,NULL,NULL,NULL),(28,'Praveen kumar',NULL,'praveenkumar@3edge.mbb','8667761244',NULL,NULL,NULL,NULL,NULL,NULL,1,'**********',NULL,NULL,NULL,NULL),(29,'Praveen kumar',NULL,'praveenkumar@3edge.mb','8667761244',NULL,NULL,NULL,NULL,NULL,NULL,1,'**********',NULL,NULL,NULL,NULL),(30,'pp',NULL,'pr@g.c','965817',NULL,NULL,NULL,NULL,NULL,NULL,1,'pp',NULL,NULL,NULL,NULL),(31,'p',NULL,'pu@g.g','55555',NULL,NULL,NULL,NULL,NULL,NULL,1,'qq',NULL,NULL,NULL,NULL),(32,'kshjdd',NULL,'praveendestraction@gmail.comm','66565',NULL,NULL,NULL,NULL,NULL,NULL,1,'pp',NULL,NULL,NULL,NULL),(33,'kshjdd',NULL,'praveendestraction@gmail.comm','66565',NULL,NULL,NULL,NULL,NULL,NULL,1,'pp',NULL,NULL,NULL,NULL),(34,'pfoc',NULL,'pr@gm.c','666',NULL,NULL,NULL,NULL,NULL,NULL,1,'pppp',NULL,NULL,NULL,NULL),(35,'pr',NULL,'pd@g.cc','96587',NULL,NULL,NULL,NULL,NULL,NULL,1,'pp',NULL,NULL,NULL,NULL),(36,'t',NULL,'uu@d.m','66',NULL,NULL,NULL,NULL,NULL,NULL,1,'pp',NULL,NULL,NULL,NULL),(37,'praveen',NULL,'pr@g.bb','9999',NULL,NULL,NULL,NULL,NULL,NULL,1,'pp',NULL,NULL,NULL,NULL),(38,'ajith',NULL,'ajithkumar.v@3edge.in','909090',NULL,NULL,NULL,NULL,NULL,NULL,1,'pp',NULL,NULL,NULL,NULL),(39,'p',NULL,'p@v.n','8885',NULL,NULL,NULL,NULL,NULL,NULL,1,'p',NULL,NULL,NULL,NULL),(40,'p',NULL,'p@z.m','88',NULL,NULL,NULL,NULL,NULL,NULL,1,'p',NULL,NULL,NULL,NULL),(41,'p',NULL,'p@s.n','66',NULL,NULL,NULL,NULL,NULL,NULL,1,'p',NULL,NULL,NULL,NULL),(42,'pp',NULL,'p@z.mm','5',NULL,NULL,NULL,NULL,NULL,NULL,2,'p',NULL,NULL,'[\"flutter\", \"development\", \"Ux\"]','42_storage_emulated_0_DCIM_Camera_IMG_20190608_134719.jpg'),(43,'p',NULL,'p@z.mp','66',NULL,NULL,NULL,NULL,NULL,NULL,1,'p',NULL,NULL,'[\"test\"]','43_storage_emulated_0_DCIM_Camera_IMG_20190413_162237.jpg'),(44,'p',NULL,'p@zx.m','6',NULL,NULL,NULL,NULL,NULL,NULL,1,'pp',NULL,NULL,'[\"test\"]','44_storage_emulated_0_WhatsApp_Media_WhatsApp_Images_IMG-20190616-WA0005.jpg'),(45,'praveenkumar',NULL,'dacts2019@gmail.com','9043961785',NULL,NULL,NULL,NULL,NULL,NULL,1,'praveen007',NULL,NULL,'[\"test\"]','45_storage_emulated_0_DCIM_Camera_IMG_20190622_113436.jpg'),(46,'pppppp',NULL,'p@z.mv','6666666666',NULL,NULL,NULL,NULL,NULL,NULL,1,'pp',NULL,NULL,NULL,NULL),(47,'ghkhjh',NULL,'p@z.mkl','666666',NULL,NULL,NULL,NULL,NULL,NULL,1,'pp',NULL,NULL,NULL,'47_storage_emulated_0_Pictures_Screenshots_Screenshot_20190630-203240.jpg'),(48,'Alekhya.@@@nn',NULL,'alekhya55majeti@gmail.com','8179401082njkk',NULL,NULL,NULL,NULL,NULL,NULL,1,'alekhya1996','http://www.facebook.com/poorna.alekhya?ref=bookmarks',NULL,'[]',NULL),(49,'praveen',NULL,'p@z.mnj','9090909090',NULL,NULL,NULL,NULL,NULL,NULL,1,'praveen',NULL,NULL,NULL,NULL),(50,'Praveen Kumar',NULL,'91563',NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,'resdfd@gm.com',NULL,NULL,NULL,NULL),(51,'Praveen Kumar',NULL,'50998',NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,'resdfd@gm.com',NULL,NULL,NULL,NULL),(52,'Praveen Kumar',NULL,'79993',NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,'resdfd@gm.com',NULL,NULL,NULL,NULL),(53,'Praveen Kumar',NULL,'resdfd@gm.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,'94690',NULL,NULL,NULL,NULL),(54,'Praveen',NULL,'resdfd@gm.c',NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,'99286',NULL,NULL,NULL,NULL),(55,'Praveenmmjjj',NULL,'resdfd@gm.cuuuuuu',NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,'23725',NULL,NULL,NULL,NULL),(56,'Praveenmmjjj',NULL,'resdfd@gm.cuuuuuu',NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,'39731',NULL,NULL,NULL,NULL),(57,'Praveenmmjjjlkk',NULL,'resdfd@gm.cuuuuuuhhhhh',NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,'12136',NULL,NULL,NULL,NULL),(58,'Praveenmmjjjlkklllll',NULL,'resdfd@gm.cuuuuuuhhhhhlllll',NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,'15655',NULL,NULL,NULL,NULL),(59,'name',NULL,'resdf@gjgjjgjgjg',NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,'79942',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `attendee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attendee_tag`
--

DROP TABLE IF EXISTS `attendee_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `attendee_tag` (
  `tag_id` int(11) NOT NULL AUTO_INCREMENT,
  `tag_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `event_id` int(11) NOT NULL,
  `count` int(11) NOT NULL,
  PRIMARY KEY (`tag_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendee_tag`
--

LOCK TABLES `attendee_tag` WRITE;
/*!40000 ALTER TABLE `attendee_tag` DISABLE KEYS */;
INSERT INTO `attendee_tag` VALUES (1,'Flutter',1,17),(2,'UX Developer',1,7),(3,'dev ops',1,7),(4,'python',1,13),(5,'java',1,7),(6,'devops',1,7),(7,'Testing',1,8),(8,'vue.js',1,8),(9,'Spring Boot',1,4),(10,'Flask',1,2),(11,'UI and UX Designer',1,5),(12,'C#',1,1);
/*!40000 ALTER TABLE `attendee_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `connection_request`
--

DROP TABLE IF EXISTS `connection_request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `connection_request` (
  `request_from_attendee` int(11) NOT NULL,
  `request_to_attendee` int(11) NOT NULL,
  `request_time` datetime DEFAULT NULL,
  `accept_time` datetime DEFAULT NULL,
  `event_id` int(11) NOT NULL,
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `connection_request`
--

LOCK TABLES `connection_request` WRITE;
/*!40000 ALTER TABLE `connection_request` DISABLE KEYS */;
INSERT INTO `connection_request` VALUES (10,15,'2019-06-27 13:16:01',NULL,1,11,0),(10,14,'2019-07-08 07:33:33',NULL,1,14,0),(14,10,'2019-07-11 05:12:03',NULL,1,16,1),(14,16,'2019-07-11 08:58:51',NULL,1,17,0),(14,22,'2019-07-11 09:04:52',NULL,1,18,0),(14,12,'2019-07-11 09:11:08',NULL,1,21,0),(48,13,'2019-07-18 09:45:00',NULL,1,25,0),(48,14,'2019-07-18 09:45:11',NULL,1,27,0),(13,11,'2019-08-07 11:59:07',NULL,1,30,0);
/*!40000 ALTER TABLE `connection_request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event_details`
--

DROP TABLE IF EXISTS `event_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `event_details` (
  `event_id` int(11) NOT NULL AUTO_INCREMENT,
  `event_name` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `event_desc` mediumtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `venue_name` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `venue_address` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `event_start_date` datetime DEFAULT NULL,
  `event_end_date` datetime DEFAULT NULL,
  `registration_start_date` datetime DEFAULT NULL,
  `registration_end_date` datetime DEFAULT NULL,
  `registration_fee` decimal(10,0) DEFAULT NULL,
  `venue_map1` blob,
  `venue_map2` blob,
  `current_status` int(11) DEFAULT NULL,
  `concepts` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`event_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_details`
--

LOCK TABLES `event_details` WRITE;
/*!40000 ALTER TABLE `event_details` DISABLE KEYS */;
INSERT INTO `event_details` VALUES (1,'Flutter i/o','Flutter is Google’s mobile UI framework for crafting high-quality native interfaces on iOS and Android in record time. Flutter works with existing code, is used by developers and organizations around the world, and is free and open source.','chepak','Chennai,TamilNadu','2019-05-14 05:30:00','2019-05-16 12:30:00','2019-05-12 16:25:18','2019-05-13 16:25:18',150,NULL,NULL,2,'[\"Flutter\",\"Product Management\",\"Web Development\",\"Stock Market\",\"DeskTop\",\"E-Commerce\"]'),(2,'Angular','Flutter is Google’s mobile UI framework for crafting high-quality native interfaces on iOS and Android in record time. Flutter works with existing code, is used by developers and organizations around the world, and is free and open source.','chepak','Chennai,TamilNadu','2019-05-14 05:30:00','2019-05-16 12:30:00','2019-05-12 16:25:18','2019-05-13 16:25:18',150,'?','?',1,'[\"Flutter\",\"Product Management\",\"Web Development\",\"Stock Market\",\"DeskTop\",\"E-Commerce\"]');
/*!40000 ALTER TABLE `event_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `follow_request`
--

DROP TABLE IF EXISTS `follow_request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `follow_request` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_attendee_id` int(11) NOT NULL,
  `to_attendee_id` int(11) NOT NULL,
  `time` datetime NOT NULL,
  `status` int(11) NOT NULL,
  `event_id` int(11) NOT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `follow_request`
--

LOCK TABLES `follow_request` WRITE;
/*!40000 ALTER TABLE `follow_request` DISABLE KEYS */;
/*!40000 ALTER TABLE `follow_request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `map_data`
--

DROP TABLE IF EXISTS `map_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `map_data` (
  `map_data_id` int(11) NOT NULL AUTO_INCREMENT,
  `map_id` int(11) NOT NULL,
  `hall_number` varchar(4) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `description` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `title` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`map_data_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `map_data`
--

LOCK TABLES `map_data` WRITE;
/*!40000 ALTER TABLE `map_data` DISABLE KEYS */;
INSERT INTO `map_data` VALUES (1,1,'12','This is the main entrance of the event which will be used for organizing the event in the venue and it will be also usefull for many things.','Hall 12'),(2,1,'1','This is the hall one for the users and for the attendees to attend the session1.','Hall 1'),(3,2,'2','Hall for flutter development.','Hall 2'),(4,2,'3','Hall for angular dart.','Hall 3'),(5,3,'4','Third floor hall with green door with key chain .','Hall 4'),(6,3,'6','Third floor for some issues for fixing food.','Hall 6'),(7,3,'12','Flooring. Flooring is the general term for a permanent covering of a floor, or for the work of installing such a floor covering. ... Both terms are used interchangeably but floor ','Hall 12'),(18,33,'2','DJFJJDJJFJJJGJHDFGJKK','HALL - 2'),(19,33,'10','DJFJJDJJFJJJGJHDFGJKK','HALL - 10');
/*!40000 ALTER TABLE `map_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `map_image`
--

DROP TABLE IF EXISTS `map_image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `map_image` (
  `map_id` int(11) NOT NULL AUTO_INCREMENT,
  `event_id` int(11) NOT NULL,
  `map_image` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `map_title` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`map_id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `map_image`
--

LOCK TABLES `map_image` WRITE;
/*!40000 ALTER TABLE `map_image` DISABLE KEYS */;
INSERT INTO `map_image` VALUES (1,1,'map1.png','Block - A'),(2,1,'map2.png','Block - B'),(3,1,'map1.png','Block - C');
/*!40000 ALTER TABLE `map_image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `poll`
--

DROP TABLE IF EXISTS `poll`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `poll` (
  `poll_id` int(11) NOT NULL AUTO_INCREMENT,
  `event_id` int(11) NOT NULL,
  `poll_type` smallint(6) DEFAULT NULL COMMENT '1 - session poll\n2 - session feedback\n3 - event feedback',
  `poll_title` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `poll_comments` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `poll_start_time` datetime DEFAULT NULL,
  `poll_end_time` datetime DEFAULT NULL,
  `poll_status` smallint(6) NOT NULL COMMENT '0 - Not active\n1 - Active\n2 - Closed',
  `session_id` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`poll_id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `poll`
--

LOCK TABLES `poll` WRITE;
/*!40000 ALTER TABLE `poll` DISABLE KEYS */;
INSERT INTO `poll` VALUES (32,1,0,'How was the Breakfast7778?','Tell our team about the Dinner you had today for making it even better if ppossible.','2019-08-19 15:00:00',NULL,1,'1'),(33,1,0,'How was the BREAK FAST 1?','Tell our team about the Dinner you had today for making it even better if ppossible.','2019-08-19 12:00:00',NULL,1,'1');
/*!40000 ALTER TABLE `poll` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `poll_answer`
--

DROP TABLE IF EXISTS `poll_answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `poll_answer` (
  `pol_answer_id` int(11) NOT NULL AUTO_INCREMENT,
  `poll_id` int(11) NOT NULL,
  `attendee_id` int(11) NOT NULL,
  `poll_answer` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `role` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`pol_answer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `poll_answer`
--

LOCK TABLES `poll_answer` WRITE;
/*!40000 ALTER TABLE `poll_answer` DISABLE KEYS */;
INSERT INTO `poll_answer` VALUES (1,32,13,'5','attendee'),(2,32,14,'5','attendee'),(3,33,14,'5','attendee'),(4,32,16,'The lunch was good , but the servic was not good.','attendee'),(5,33,13,'The lunch was good , but the servic was not good.','speaker');
/*!40000 ALTER TABLE `poll_answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `poll_line_items`
--

DROP TABLE IF EXISTS `poll_line_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `poll_line_items` (
  `poll_id` int(11) NOT NULL,
  `poll_line_item_no` smallint(6) DEFAULT NULL,
  `poll_line_item_desc` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `poll_line_itemcol` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `poll_line_items`
--

LOCK TABLES `poll_line_items` WRITE;
/*!40000 ALTER TABLE `poll_line_items` DISABLE KEYS */;
/*!40000 ALTER TABLE `poll_line_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `poll_values`
--

DROP TABLE IF EXISTS `poll_values`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `poll_values` (
  `poll_values_id` int(11) NOT NULL AUTO_INCREMENT,
  `poll_id` int(11) DEFAULT NULL,
  `name` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `val` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`poll_values_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `poll_values`
--

LOCK TABLES `poll_values` WRITE;
/*!40000 ALTER TABLE `poll_values` DISABLE KEYS */;
INSERT INTO `poll_values` VALUES (12,32,'Excellent','5'),(13,32,'Good','4'),(14,32,'Average','3'),(15,32,'Below average','2'),(16,32,'Worst cannot Eat','1'),(17,33,'Excellent','5'),(18,33,'Good','4'),(19,33,'Average','3'),(20,33,'Below average','2'),(21,33,'Worst cannot Eat','1');
/*!40000 ALTER TABLE `poll_values` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `question` (
  `question_id` int(11) NOT NULL,
  `question` varchar(250) COLLATE utf8mb4_unicode_ci NOT NULL,
  `displayable` smallint(6) NOT NULL,
  `session_id` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `raised_by` int(11) NOT NULL,
  `raised_to` int(11) DEFAULT NULL,
  `event_id` int(11) NOT NULL,
  `attendees` int(11) NOT NULL,
  `speakers` int(11) NOT NULL,
  PRIMARY KEY (`question_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recommended_activity`
--

DROP TABLE IF EXISTS `recommended_activity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recommended_activity` (
  `activity_id` int(10) unsigned NOT NULL,
  `event_id` int(11) NOT NULL,
  `activity_desc` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `activity_location` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `activity_timings` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `activity_cost` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Recommended_activitiescol` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Recommended_activitiescol1` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`activity_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recommended_activity`
--

LOCK TABLES `recommended_activity` WRITE;
/*!40000 ALTER TABLE `recommended_activity` DISABLE KEYS */;
/*!40000 ALTER TABLE `recommended_activity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `session`
--

DROP TABLE IF EXISTS `session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `session` (
  `session_id` int(11) NOT NULL AUTO_INCREMENT,
  `session_topic` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `session_desc` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `start_time` datetime DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `session_type` smallint(6) DEFAULT NULL,
  `location` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `event_id` int(11) NOT NULL,
  `concepts` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`session_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `session`
--

LOCK TABLES `session` WRITE;
/*!40000 ALTER TABLE `session` DISABLE KEYS */;
INSERT INTO `session` VALUES (1,'Flutter Web ','Flutter for web is a code-compatible implementation of Flutter that is rendered using standards-based web technologies: HTML, CSS and JavaScript. With Flutter for web, you can compile existing Flutter code written in Dart into a client experience that can be embedded in the browser and deployed to any web server. You can use all the features of Flutter, and you don’t need a browser plug-in.','2019-05-14 05:30:00','2019-05-14 06:30:00',1,'Hall 5',1,NULL),(2,'Flutter dart','Programming language tutorials which ','2019-05-14 07:30:00','2019-05-14 08:30:00',2,'Hall 8',1,NULL),(3,'Google angular dart','Develiping web sites using angular dart.','2019-05-14 11:30:00','2019-05-14 12:30:00',3,'Hall 5',1,'[\"Angular dart\",\"Web Framework\"]'),(4,'Flutter new plugins launch.','Developing a new plugin which will be used for both android and ios.','2019-05-14 13:30:00','2019-05-14 15:30:00',4,'Hall 6',1,NULL),(5,'Flutter Web ','Develope a responsive website using flutter.','2019-05-15 05:30:00','2019-05-15 07:30:00',1,'Hall 5',1,NULL),(6,'Flutter dart','Programming language tutorials which ','2019-05-15 07:30:00','2019-05-15 09:30:00',2,'Hall 8',1,NULL),(7,'Google angular dart','Develiping web sites using angular dart.','2019-05-15 12:30:00','2019-05-15 14:30:00',3,'Hall 5',1,NULL),(8,'Flutter new plugins launch.','Developing a new plugin which will be used for both android and ios.','2019-05-15 12:30:00','2019-05-15 14:30:00',4,'Hall 6',1,NULL),(9,'Flutter Web ','Develope a responsive website using flutter.','2019-05-16 11:00:00','2019-05-16 12:00:00',1,'Hall 5',1,NULL),(10,'Flutter dart','Programming language tutorials which ','2019-05-16 13:00:00','2019-05-16 15:00:00',2,'Hall 8',1,NULL),(11,'Google angular dart','Develiping web sites using angular dart.','2019-05-16 16:00:00','2019-05-16 18:00:00',3,'Hall 5',1,NULL),(12,'Flutter new plugins launch.','Developing a new plugin which will be used for both android and ios.','2019-05-16 18:00:00','2019-05-14 20:00:00',4,'Hall 6',1,NULL),(13,'Flutter beyond mobile','Flutter for desktop and websites','2019-05-14 11:30:00','2019-05-14 12:30:00',5,'Floor 1 , Hall 1',1,NULL),(14,'Flutter for server','Flutter for server side.','2019-05-14 12:30:00','2019-05-14 13:30:00',2,'Ground floor , Hall 10',1,NULL),(15,'Make different','Flutter difference','2019-05-14 11:30:00','2019-05-14 12:30:00',2,'Ground Floor , hall 9',1,NULL);
/*!40000 ALTER TABLE `session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `speaker`
--

DROP TABLE IF EXISTS `speaker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `speaker` (
  `speaker_id` int(11) NOT NULL,
  `role` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_id` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `speakercol` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `speakercol1` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `id_number` int(11) NOT NULL AUTO_INCREMENT,
  `event_id` int(11) NOT NULL,
  PRIMARY KEY (`id_number`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `speaker`
--

LOCK TABLES `speaker` WRITE;
/*!40000 ALTER TABLE `speaker` DISABLE KEYS */;
INSERT INTO `speaker` VALUES (13,'Hak Kai every things','1',NULL,NULL,1,1),(12,'Explain details','1',NULL,NULL,2,1),(11,'Google explaination.','2',NULL,NULL,3,1),(10,'Angular dart.','3',NULL,NULL,4,1),(13,'delete things','4',NULL,NULL,5,1),(12,'Explain details','5',NULL,NULL,6,1),(11,'Google explaination.','6',NULL,NULL,7,1),(10,'Angular dart.','7',NULL,NULL,8,1),(13,'Hak Kai every things','7',NULL,NULL,9,1),(12,'Explain details','8',NULL,NULL,10,1),(11,'Google explaination.','9',NULL,NULL,11,1),(10,'Angular dart.','10',NULL,NULL,12,1),(15,'Flutter for webdevelopment','13',NULL,NULL,15,1),(16,'Flutter for desktop','13',NULL,NULL,16,1),(11,'Server side','14',NULL,NULL,17,1),(14,'Difference using Flutter','15',NULL,NULL,18,1),(49,'Something','2',NULL,NULL,23,1),(58,'Something','2',NULL,NULL,24,1),(59,'Something','4',NULL,NULL,25,1);
/*!40000 ALTER TABLE `speaker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_access`
--

DROP TABLE IF EXISTS `user_access`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_access` (
  `user_access_id` int(11) NOT NULL AUTO_INCREMENT,
  `attendee_id` int(11) NOT NULL,
  `session_id` int(11) NOT NULL,
  PRIMARY KEY (`user_access_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_access`
--

LOCK TABLES `user_access` WRITE;
/*!40000 ALTER TABLE `user_access` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_access` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `attendee_id` int(11) NOT NULL,
  `access` int(11) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-31 14:57:56
