-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: fm
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `add_product`
--

DROP TABLE IF EXISTS `add_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `add_product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_id` varchar(200) DEFAULT NULL,
  `product_name` varchar(200) DEFAULT NULL,
  `valve_size` varchar(100) DEFAULT NULL,
  `valve_class` varchar(100) DEFAULT NULL,
  `product_description` varchar(255) DEFAULT NULL,
  `actuator_type` varchar(100) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `flanged_type` varchar(100) DEFAULT NULL,
  `airshell_setpressure` varchar(255) DEFAULT NULL,
  `airshell_holdingtime` varchar(100) DEFAULT NULL,
  `airshell_testduration` varchar(100) DEFAULT NULL,
  `airshell_allowedleak` varchar(100) DEFAULT NULL,
  `airshell_leakoption` int DEFAULT NULL,
  `airseat_setpressure` varchar(255) DEFAULT NULL,
  `airseat_holdingtime` varchar(100) DEFAULT NULL,
  `airseat_testduration` varchar(100) DEFAULT NULL,
  `airseat_allowedleak` varchar(100) DEFAULT NULL,
  `airseat_leakoption` int DEFAULT NULL,
  `hydroshell_setpressure` varchar(255) DEFAULT NULL,
  `hydroshell_holdingtime` varchar(100) DEFAULT NULL,
  `hydroshell_testduration` varchar(100) DEFAULT NULL,
  `hydroshell_allowedleak` varchar(100) DEFAULT NULL,
  `hydroshell_leakoption` int DEFAULT NULL,
  `hydroseat_setpressure` varchar(255) DEFAULT NULL,
  `hydroseat_holdingtime` varchar(100) DEFAULT NULL,
  `hydroseat_testduration` varchar(100) DEFAULT NULL,
  `hydroseat_allowedleak` varchar(100) DEFAULT NULL,
  `hydroseat_leakoption` int DEFAULT NULL,
  `bubbleseat_setpressure` varchar(255) DEFAULT NULL,
  `bubbleseat_holdingtime` varchar(100) DEFAULT NULL,
  `bubbleseat_testduration` varchar(100) DEFAULT NULL,
  `bubbleseat_allowedleak` varchar(100) DEFAULT NULL,
  `bubbleseat_leakoption` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `add_product`
--

LOCK TABLES `add_product` WRITE;
/*!40000 ALTER TABLE `add_product` DISABLE KEYS */;
INSERT INTO `add_product` VALUES (65,'1','valve','hubj','bbj','nknk','nkkl','jn','njkn','hjh','bjbn','jnkjn','jnjn',1,'njn','nj','jn','nj',0,'knkm','nkn','kmnk','mm',1,'bjhij','jnj','k','lkmlk',1,'bijh','ijij','jjk','jnkj',0);
/*!40000 ALTER TABLE `add_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'!','2025-05-12 09:00:52.039675',1,'admin','','','',1,1,'2025-05-12 08:44:24.115425');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `crud`
--

DROP TABLE IF EXISTS `crud`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `crud` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `age` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `crud`
--

LOCK TABLES `crud` WRITE;
/*!40000 ALTER TABLE `crud` DISABLE KEYS */;
INSERT INTO `crud` VALUES (2,'njkmk','6'),(3,'bfddf','5'),(4,'tr','1');
/*!40000 ALTER TABLE `crud` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-03-03 09:03:50.739307'),(2,'auth','0001_initial','2025-03-03 09:03:51.344378'),(3,'admin','0001_initial','2025-03-03 09:03:51.483664'),(4,'admin','0002_logentry_remove_auto_add','2025-03-03 09:03:51.494726'),(5,'admin','0003_logentry_add_action_flag_choices','2025-03-03 09:03:51.506313'),(6,'contenttypes','0002_remove_content_type_name','2025-03-03 09:03:51.638462'),(7,'auth','0002_alter_permission_name_max_length','2025-03-03 09:03:51.738854'),(8,'auth','0003_alter_user_email_max_length','2025-03-03 09:03:51.779815'),(9,'auth','0004_alter_user_username_opts','2025-03-03 09:03:51.791005'),(10,'auth','0005_alter_user_last_login_null','2025-03-03 09:03:51.887041'),(11,'auth','0006_require_contenttypes_0002','2025-03-03 09:03:51.890135'),(12,'auth','0007_alter_validators_add_error_messages','2025-03-03 09:03:51.890135'),(13,'auth','0008_alter_user_username_max_length','2025-03-03 09:03:52.005001'),(14,'auth','0009_alter_user_last_name_max_length','2025-03-03 09:03:52.098183'),(15,'auth','0010_alter_group_name_max_length','2025-03-03 09:03:52.124264'),(16,'auth','0011_update_proxy_permissions','2025-03-03 09:03:52.133696'),(17,'auth','0012_alter_user_first_name_max_length','2025-03-03 09:03:52.222712'),(18,'sessions','0001_initial','2025-03-03 09:03:52.273983');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1wllfwl8rg6adnmg386le4d4qvzipoqa','eyJzdXBlcnVzZXIiOiJUcnVlIn0:1uCFpA:VVECD-FQ3UoD6nBDQg_aBpntvdf_6ykoFjMlCpM7iak','2025-05-20 10:46:56.129163'),('aynkirhye68unjmsou409ujhfepo7qp8','.eJxVjLEOwiAUAP-F2RAotPIc3d3cm_fgYaumNFAm478rSZeud5f7iFJXzrVwFhdxz5XFSYxYt2lsbJzDH-sjI_QvXpoIT1weSfq0bHkm2RK52yJvKfD7ureHwYRlalsXwRiGfrCoHAxRUacs4eCIbNSGA2ilKfQOAChCb9xZdR4ta7aBvfj-AGfYPiw:1uEOls:7M4Yq0HrFBUOC89ALuFF5QJOEBQ9daov-M2Jb872n6k','2025-05-26 08:44:24.152863'),('lo0acszv2qnh3eqd9pdkgxu3vcrupk83','eyJzdXBlcnVzZXIiOiJUcnVlIn0:1uCy2V:VwJiVirOrfH3pFqPCc_J2WTDpRImNz5Ga7nTH_AlTcM','2025-05-22 09:59:39.972005'),('n8m8ihm7gwaf1d5hz4sl278rzqt1jyk4','eyJzdXBlcnVzZXIiOm51bGx9:1uCALW:sEfh5tIy6fXAcQ_aw4YtKfvSAyD-WUhRXgLg-8oYMFs','2025-05-20 04:55:58.037464'),('qfshqalcg7lgerr2gmbsos0y6dzan16p','eyJzdXBlcnVzZXIiOiJUcnVlIn0:1uDbdt:CnDXRZOI4z1DaxpzkQfZSVFImXPwO8aH7tgtUgkkWZQ','2025-05-24 04:16:53.557813'),('r122lfwh0hidan1zkik54t52domkwa1z','eyJzdXBlcnVzZXIiOiJUcnVlIn0:1uDLgb:LdkYOnArVZpEmhB2vGywuvKAYk-g-QjJ8F678ZgYZfw','2025-05-23 11:14:37.694356');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `example`
--

DROP TABLE IF EXISTS `example`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `example` (
  `id` int NOT NULL AUTO_INCREMENT,
  `uname` varchar(20) DEFAULT NULL,
  `empid` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `example`
--

LOCK TABLES `example` WRITE;
/*!40000 ALTER TABLE `example` DISABLE KEYS */;
INSERT INTO `example` VALUES (1,'vfdv','vds'),(2,'dharani','123'),(3,'ilan','456'),(4,'cdc','cas'),(5,'bjnknkkkkkk','bjnkn'),(6,'bfgb','vdfv'),(7,'manikdharani','987'),(8,'bottlee','001');
/*!40000 ALTER TABLE `example` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fm_project`
--

DROP TABLE IF EXISTS `fm_project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fm_project` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `employee_id` varchar(100) DEFAULT NULL,
  `is_superuser` varchar(100) DEFAULT NULL,
  `login_time` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=171 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fm_project`
--

LOCK TABLES `fm_project` WRITE;
/*!40000 ALTER TABLE `fm_project` DISABLE KEYS */;
INSERT INTO `fm_project` VALUES (1,'admin','admin','admin','admin','123456','True',NULL),(63,'Dharani','dharani','Dharani','M','634327',NULL,NULL),(132,'manik','123','manik','r','123',NULL,NULL),(133,'mk','mk','mk','mk','mk',NULL,NULL),(134,'teslead','t','Teslead','T','1234567',NULL,NULL),(135,'t','t','t','t','t',NULL,NULL),(136,'g','g','g','g','g',NULL,NULL),(137,'tt','t','t','t','tt',NULL,NULL),(138,'l','l','j','j','l',NULL,NULL),(139,'tg','tg','t','t','gt',NULL,NULL),(140,'ty','ty','t','h','ty',NULL,NULL),(141,'gg','g','g','g','gg',NULL,NULL),(142,'undefined','g','g','g','undefined',NULL,NULL),(143,'undefined','g','g','g','undefined',NULL,NULL),(144,'gt','r','t','t','12',NULL,NULL),(145,'hy','hy','g','g','hy',NULL,NULL),(146,'undefined','hy','g','g','undefined',NULL,NULL),(147,'hu','hu','f','f','hu',NULL,NULL),(148,'er','er','ht','ht','er',NULL,NULL),(149,'n','n','n','n','n',NULL,NULL),(150,'gtrg','b','h','h','bfg',NULL,NULL),(151,'tr','b','g','g','tr',NULL,NULL),(152,'m','m','m','m','m',NULL,NULL),(153,'nh','nh','h','h','nh',NULL,NULL),(154,'undefined','nh','h','h','undefined',NULL,NULL),(155,'undefined','nh','h','h','undefined',NULL,NULL),(156,'undefined','nh','h','h','undefined',NULL,NULL),(157,'undefined','nh','h','h','undefined',NULL,NULL),(158,'ju','ju','gt','gt','ju',NULL,NULL),(159,'gtgd','h','gt','gt','nhghn',NULL,NULL),(160,'cd','f','v','v','vd',NULL,NULL),(161,'f','f','f','f','f',NULL,NULL),(162,'nj','1','j','m','nk',NULL,NULL),(163,'dharanim','12','dharani','m','12345678',NULL,NULL),(164,'nhnh','nh','bg','bg','nhnh',NULL,NULL),(165,'dharanii','123','dharani','m','1234',NULL,NULL),(166,'fr','fr','fr','fr','fr',NULL,'2025-03-24 14:57:38'),(167,'hello','987','hello','hi','987',NULL,'2025-03-26 09:30:31'),(168,'kishore','123','kishore','k','159',NULL,'2025-03-26 10:02:00'),(169,'hytyh','1','vdsv','vsdcds','1',NULL,'2025-05-06 12:45:57'),(170,'adminn','1','vbfdgv','bfdfvbdf','12345',NULL,'2025-05-08 15:27:49');
/*!40000 ALTER TABLE `fm_project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fm_r12`
--

DROP TABLE IF EXISTS `fm_r12`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fm_r12` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `employee_id` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fm_r12`
--

LOCK TABLES `fm_r12` WRITE;
/*!40000 ALTER TABLE `fm_r12` DISABLE KEYS */;
INSERT INTO `fm_r12` VALUES (1,'dharani','123456','dharani'),(2,'teslead','654321','teslead');
/*!40000 ALTER TABLE `fm_r12` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `othersetting`
--

DROP TABLE IF EXISTS `othersetting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `othersetting` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Good_result` varchar(100) DEFAULT NULL,
  `Bad_result` varchar(100) DEFAULT NULL,
  `cell_id` int DEFAULT NULL,
  `Hydro_leak` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `othersetting`
--

LOCK TABLES `othersetting` WRITE;
/*!40000 ALTER TABLE `othersetting` DISABLE KEYS */;
INSERT INTO `othersetting` VALUES (1,'1','2',5,'no');
/*!40000 ALTER TABLE `othersetting` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pressure_data`
--

DROP TABLE IF EXISTS `pressure_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pressure_data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `timestamp` datetime NOT NULL,
  `pressure_value` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pressure_data`
--

LOCK TABLES `pressure_data` WRITE;
/*!40000 ALTER TABLE `pressure_data` DISABLE KEYS */;
INSERT INTO `pressure_data` VALUES (11,'2025-03-15 10:00:00',90.00),(12,'2025-03-15 10:00:00',1000.00),(13,'2025-03-15 10:11:00',200.00),(14,'2025-03-15 10:11:00',500.00),(15,'2025-03-15 16:51:42',90.00),(16,'2025-03-15 16:51:58',90.00),(17,'2025-03-15 16:52:21',250.00),(18,'2025-03-15 16:52:38',300.00),(19,'2025-03-15 16:53:20',550.00),(20,'2025-03-15 16:54:07',600.00),(21,'2025-03-15 17:00:19',400.00),(22,'2025-03-15 17:00:44',200.00),(23,'2025-03-15 17:02:13',400.00),(24,'2025-03-15 17:04:32',300.00),(25,'2025-03-15 17:04:42',500.00),(26,'2025-03-15 17:05:00',300.00),(27,'2025-03-15 17:05:11',500.00),(28,'2025-03-15 17:05:36',1000.00),(29,'2025-03-15 17:05:45',100.00),(30,'2025-03-15 17:05:58',200.00),(31,'2025-03-15 17:07:22',100.00),(32,'2025-03-15 17:07:33',300.00),(33,'2025-03-15 17:07:48',350.00),(34,'2025-03-15 17:09:47',500.00),(35,'2025-03-15 17:09:54',400.00),(36,'2025-03-15 17:10:12',600.00),(37,'2025-03-15 17:10:42',800.00),(38,'2025-03-15 17:11:09',500.00),(39,'2025-03-15 17:11:32',700.00),(40,'2025-03-15 17:16:54',800.00),(41,'2025-03-15 17:17:07',200.00),(42,'2025-03-15 17:17:31',400.00),(43,'2025-03-15 17:18:00',500.00),(44,'2025-03-15 17:18:15',800.00),(45,'2025-03-15 17:18:35',800.00),(46,'2025-03-15 17:19:52',80.00),(47,'2025-03-15 17:20:03',40.00),(48,'2025-03-15 17:20:12',90.00),(49,'2025-03-15 17:20:26',90.00),(50,'2025-03-15 17:24:00',200.00),(51,'2025-03-15 17:24:17',30.00),(52,'2025-03-15 17:25:36',50.00),(53,'2025-03-15 17:27:45',200.00),(54,'2025-03-15 17:34:22',250.00),(55,'2025-03-15 17:34:34',500.00),(56,'2025-03-15 17:36:28',30.00),(57,'2025-03-15 17:36:46',40.00),(58,'2025-03-15 17:39:02',70.00),(59,'2025-03-15 17:39:15',80.00),(60,'2025-03-15 17:39:35',90.00),(61,'2025-03-15 17:41:03',400.00),(62,'2025-03-15 17:41:23',800.00),(63,'2025-03-15 17:41:43',800.00),(64,'2025-03-15 17:44:43',600.00),(65,'2025-03-15 17:44:57',900.00),(66,'2025-03-15 17:46:36',200.00),(67,'2025-03-15 17:47:56',10.00),(68,'2025-03-15 17:53:46',200.00),(69,'2025-03-15 17:54:03',300.00),(70,'2025-03-15 17:55:00',600.00),(71,'2025-03-15 17:57:32',400.00),(72,'2025-03-15 17:57:43',450.00),(73,'2025-03-15 17:58:31',450.00),(74,'2025-03-15 17:59:07',800.00),(75,'2025-03-15 17:59:23',1000.00),(76,'2025-03-15 17:59:42',500.00),(77,'2025-03-15 18:01:43',200.00),(78,'2025-03-15 18:01:52',250.00),(79,'2025-03-15 18:04:20',300.00),(80,'2025-03-15 18:04:36',800.00),(81,'2025-03-15 18:04:59',100.00),(82,'2025-03-15 18:06:38',200.00),(83,'2025-03-15 18:06:46',500.00),(84,'2025-03-18 11:57:23',300.00),(85,'2025-03-18 11:58:01',90.00),(86,'2025-03-18 12:06:41',600.00),(87,'2025-03-18 12:06:48',90.00),(88,'2025-03-18 12:09:13',200.00),(89,'2025-03-18 12:09:23',90.00),(90,'2025-03-18 12:29:57',800.00),(91,'2025-03-18 12:32:30',400.00),(92,'2025-03-18 12:32:53',900.00),(93,'2025-03-18 12:33:19',90.00),(94,'2025-03-18 12:33:36',900.00),(95,'2025-03-18 12:33:55',90.00),(96,'2025-03-18 12:34:12',500.00),(97,'2025-03-18 12:34:23',900.00),(98,'2025-03-18 12:34:35',90.00),(99,'2025-03-18 12:36:05',900.00);
/*!40000 ALTER TABLE `pressure_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recent_login`
--

DROP TABLE IF EXISTS `recent_login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recent_login` (
  `username` varchar(100) DEFAULT NULL,
  `employee_id` varchar(100) DEFAULT NULL,
  `current_datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recent_login`
--

LOCK TABLES `recent_login` WRITE;
/*!40000 ALTER TABLE `recent_login` DISABLE KEYS */;
INSERT INTO `recent_login` VALUES ('admin','123456','2025-05-12 14:30:52');
/*!40000 ALTER TABLE `recent_login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `valve_actuator`
--

DROP TABLE IF EXISTS `valve_actuator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `valve_actuator` (
  `actuator_type_id` int NOT NULL AUTO_INCREMENT,
  `actuator_type_name` varchar(100) DEFAULT NULL,
  `actuator_type_description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`actuator_type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `valve_actuator`
--

LOCK TABLES `valve_actuator` WRITE;
/*!40000 ALTER TABLE `valve_actuator` DISABLE KEYS */;
INSERT INTO `valve_actuator` VALUES (2,'actuator','actuatorr'),(3,'nknkjhjkh','nkm');
/*!40000 ALTER TABLE `valve_actuator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `valve_class`
--

DROP TABLE IF EXISTS `valve_class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `valve_class` (
  `valve_class_id` int NOT NULL AUTO_INCREMENT,
  `valve_class_name` varchar(100) DEFAULT NULL,
  `valve_class_description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`valve_class_id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `valve_class`
--

LOCK TABLES `valve_class` WRITE;
/*!40000 ALTER TABLE `valve_class` DISABLE KEYS */;
INSERT INTO `valve_class` VALUES (2,'valve class','hellooo'),(3,'fd','ds'),(4,'jnkm','njkn'),(5,'vfddddd','vfd'),(6,'gff','gf'),(7,'ngfgf','vbfd'),(8,'nkm','knkm'),(10,'bfd','bdf'),(11,'kmkm','lklklk'),(12,'hf','hf'),(13,'gr','gr'),(14,'bg','bg'),(15,'vf','vfd'),(16,'jnkm','jnjn'),(17,'nj','mkl'),(18,'nkm','kmlk'),(19,'nkm','mkmlk'),(20,'njn','kmk'),(21,'njnm','kmm'),(30,'bjn','knk'),(31,'ml,','lmlml'),(50,'nkjk','mkm');
/*!40000 ALTER TABLE `valve_class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `valve_flanged`
--

DROP TABLE IF EXISTS `valve_flanged`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `valve_flanged` (
  `flanged_type_id` int NOT NULL AUTO_INCREMENT,
  `flanged_type_name` varchar(100) DEFAULT NULL,
  `flanged_type_description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`flanged_type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `valve_flanged`
--

LOCK TABLES `valve_flanged` WRITE;
/*!40000 ALTER TABLE `valve_flanged` DISABLE KEYS */;
INSERT INTO `valve_flanged` VALUES (1,'normal','okk'),(4,'vfd','vfd'),(5,'nh','ny'),(6,'bgf','bf'),(7,'bfg','bfg'),(10,'bgf','bfg'),(11,'bfd','b'),(12,'flang','flang type'),(13,'flang','flang'),(14,'flang','flang'),(15,'flang','flang');
/*!40000 ALTER TABLE `valve_flanged` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `valve_size`
--

DROP TABLE IF EXISTS `valve_size`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `valve_size` (
  `valve_size_id` int NOT NULL AUTO_INCREMENT,
  `valve_size_name` varchar(100) DEFAULT NULL,
  `valve_size_description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`valve_size_id`)
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `valve_size`
--

LOCK TABLES `valve_size` WRITE;
/*!40000 ALTER TABLE `valve_size` DISABLE KEYS */;
INSERT INTO `valve_size` VALUES (2,'valve','kmlml'),(3,'nnmklm','kkmlkm'),(4,'njnk','mkmlkl');
/*!40000 ALTER TABLE `valve_size` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `valve_type`
--

DROP TABLE IF EXISTS `valve_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `valve_type` (
  `valve_type_id` int NOT NULL AUTO_INCREMENT,
  `valve_type_name` varchar(100) DEFAULT NULL,
  `valve_type_description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`valve_type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=568 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `valve_type`
--

LOCK TABLES `valve_type` WRITE;
/*!40000 ALTER TABLE `valve_type` DISABLE KEYS */;
INSERT INTO `valve_type` VALUES (1,'dharani','nkjnk'),(2,'ilan','kmk'),(3,'csd','cds'),(5,'vfd','vd'),(6,'vfd','vfd'),(7,'bf','bf');
/*!40000 ALTER TABLE `valve_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `valve_unit`
--

DROP TABLE IF EXISTS `valve_unit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `valve_unit` (
  `unit_id` int NOT NULL AUTO_INCREMENT,
  `unit_name` varchar(100) DEFAULT NULL,
  `unit_description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`unit_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `valve_unit`
--

LOCK TABLES `valve_unit` WRITE;
/*!40000 ALTER TABLE `valve_unit` DISABLE KEYS */;
INSERT INTO `valve_unit` VALUES (2,'unit','bfd'),(4,'fd','dsdssss'),(5,'hbjn','jnklk');
/*!40000 ALTER TABLE `valve_unit` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-12 14:37:09
