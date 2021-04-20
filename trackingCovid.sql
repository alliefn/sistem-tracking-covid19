-- MariaDB dump 10.18  Distrib 10.5.8-MariaDB, for osx10.16 (x86_64)
--
-- Host: localhost    Database: trackingCovid
-- ------------------------------------------------------
-- Server version	10.5.8-MariaDB

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
-- Current Database: `trackingCovid`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `trackingCovid` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `trackingCovid`;

--
-- Table structure for table `DataCovid`
--

DROP TABLE IF EXISTS `DataCovid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DataCovid` (
  `tanggal_input` date NOT NULL,
  `kasus_aktif` int(11) DEFAULT NULL,
  `kasus_sembuh` int(11) DEFAULT NULL,
  `kasus_meninggal` int(11) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`tanggal_input`),
  KEY `FK_DataCovid_User` (`username`),
  CONSTRAINT `FK_DataCovid_User` FOREIGN KEY (`username`) REFERENCES `User` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DataCovid`
--

LOCK TABLES `DataCovid` WRITE;
/*!40000 ALTER TABLE `DataCovid` DISABLE KEYS */;
INSERT INTO `DataCovid` (`tanggal_input`, `kasus_aktif`, `kasus_sembuh`, `kasus_meninggal`, `username`) VALUES ('2021-04-19',2000,150000,10000,'admin1'),('2021-04-20',3000,151000,11000,'admin2'),('2021-04-21',2500,152000,12000,'admin1'),('2021-04-22',2000,153000,13000,'admin2'),('2021-04-23',3000,154000,14000,'admin1');
/*!40000 ALTER TABLE `DataCovid` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Kamar`
--

DROP TABLE IF EXISTS `Kamar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Kamar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rumah_sakit_id` int(11) NOT NULL,
  `harga` decimal(10,2) NOT NULL,
  `jumlah` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rumah_sakit_id` (`rumah_sakit_id`),
  CONSTRAINT `kamar_ibfk_1` FOREIGN KEY (`rumah_sakit_id`) REFERENCES `RumahSakit` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Kamar`
--

LOCK TABLES `Kamar` WRITE;
/*!40000 ALTER TABLE `Kamar` DISABLE KEYS */;
INSERT INTO `Kamar` (`id`, `rumah_sakit_id`, `harga`, `jumlah`, `nama`) VALUES (1,1,150000.00,10,'Anggrek'),(2,1,200000.00,5,'Melati'),(3,2,175000.00,10,'Puspa'),(4,2,300000.00,5,'Matahari'),(5,3,200000.00,20,'Dandelion'),(6,3,400000.00,10,'Deluxe'),(7,4,250000.00,25,'Juyeun'),(8,4,500000.00,10,'Lily');
/*!40000 ALTER TABLE `Kamar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Pesanan`
--

DROP TABLE IF EXISTS `Pesanan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Pesanan` (
  `id_pesanan` int(11) NOT NULL,
  `id_kamar` int(11) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `status` enum('On Hold','Diterima','Ditolak') DEFAULT NULL,
  `tanggal_pesan` date DEFAULT NULL,
  PRIMARY KEY (`id_pesanan`),
  KEY `FK_Pesanan_Kamar` (`id_kamar`),
  KEY `FK_Pesanan_User` (`username`),
  CONSTRAINT `FK_Pesanan_Kamar` FOREIGN KEY (`id_kamar`) REFERENCES `Kamar` (`id`),
  CONSTRAINT `FK_Pesanan_User` FOREIGN KEY (`username`) REFERENCES `User` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Pesanan`
--

LOCK TABLES `Pesanan` WRITE;
/*!40000 ALTER TABLE `Pesanan` DISABLE KEYS */;
INSERT INTO `Pesanan` (`id_pesanan`, `id_kamar`, `username`, `status`, `tanggal_pesan`) VALUES (701,1,'aretha','Diterima','2021-04-21'),(702,6,'gray','Ditolak','2021-04-23'),(703,8,'elena','On Hold','2021-04-19'),(704,4,'gillian','On Hold','2021-04-21'),(705,1,'ryann','On Hold','2021-04-22');
/*!40000 ALTER TABLE `Pesanan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RumahSakit`
--

DROP TABLE IF EXISTS `RumahSakit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `RumahSakit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nama` varchar(255) NOT NULL,
  `alamat` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RumahSakit`
--

LOCK TABLES `RumahSakit` WRITE;
/*!40000 ALTER TABLE `RumahSakit` DISABLE KEYS */;
INSERT INTO `RumahSakit` (`id`, `nama`, `alamat`) VALUES (1,'Rumah Sakit Sembuh Covid Amin','Jalan Semoga Lekas Sembuh'),(2,'Rumah Sakit Sembuh Covid Bismillah','Jalan Cepat Sembuh'),(3,'Rumah Sakit Tidak Meninggal','Jalan Bismillah Sembuh'),(4,'Rumah Sakit Tidak Covid','Jalan Aamiin Sembuh');
/*!40000 ALTER TABLE `RumahSakit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Suhu`
--

DROP TABLE IF EXISTS `Suhu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Suhu` (
  `id_suhu` int(11) NOT NULL,
  `tanggal_input` date DEFAULT NULL,
  `value` float DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_suhu`),
  KEY `FK_Suhu_User` (`username`),
  CONSTRAINT `FK_Suhu_User` FOREIGN KEY (`username`) REFERENCES `User` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Suhu`
--

LOCK TABLES `Suhu` WRITE;
/*!40000 ALTER TABLE `Suhu` DISABLE KEYS */;
INSERT INTO `Suhu` (`id_suhu`, `tanggal_input`, `value`, `username`) VALUES (1,'2021-04-19',37.5,'gillian'),(2,'2021-04-20',38,'gillian'),(3,'2021-04-21',38.5,'gillian'),(4,'2021-04-22',37.7,'gillian'),(5,'2021-04-23',36.9,'gillian'),(6,'2021-04-19',38.3,'russell'),(7,'2021-04-20',37.9,'russell'),(8,'2021-04-21',38.8,'russell'),(9,'2021-04-22',39.2,'russell'),(10,'2021-04-23',39,'russell'),(11,'2021-04-19',35.9,'chloe'),(12,'2021-04-20',36.1,'chloe'),(13,'2021-04-21',36.3,'chloe'),(14,'2021-04-22',36.2,'chloe'),(15,'2021-04-23',36.9,'chloe'),(16,'2021-04-19',38,'haylee'),(17,'2021-04-20',38.2,'haylee'),(18,'2021-04-21',38.3,'haylee'),(19,'2021-04-22',38.6,'haylee'),(20,'2021-04-23',38.5,'haylee'),(21,'2021-04-19',39.3,'elena'),(22,'2021-04-20',39.2,'elena'),(23,'2021-04-21',39.4,'elena'),(24,'2021-04-22',39.8,'elena'),(25,'2021-04-23',39.3,'elena'),(26,'2021-04-19',37.6,'ryann'),(27,'2021-04-20',37.8,'ryann'),(28,'2021-04-21',37.3,'ryann'),(29,'2021-04-22',38.2,'ryann'),(30,'2021-04-23',38,'ryann'),(31,'2021-04-19',38,'aretha'),(32,'2021-04-20',38.1,'aretha'),(33,'2021-04-21',38.2,'aretha'),(34,'2021-04-22',38.3,'aretha'),(35,'2021-04-23',38.9,'aretha'),(36,'2021-04-19',36.1,'kimberly'),(37,'2021-04-20',36.5,'kimberly'),(38,'2021-04-21',36.4,'kimberly'),(39,'2021-04-22',36.9,'kimberly'),(40,'2021-04-23',38,'kimberly'),(41,'2021-04-19',37.4,'rodney'),(42,'2021-04-20',37.7,'rodney'),(43,'2021-04-21',37.6,'rodney'),(44,'2021-04-22',37.3,'rodney'),(45,'2021-04-23',37.2,'rodney'),(46,'2021-04-19',35.9,'gray'),(47,'2021-04-20',36,'gray'),(48,'2021-04-21',36.5,'gray'),(49,'2021-04-22',37.4,'gray'),(50,'2021-04-23',38.3,'gray');
/*!40000 ALTER TABLE `Suhu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `username` varchar(50) NOT NULL,
  `nama` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `no_telp` varchar(20) DEFAULT NULL,
  `role` enum('admin','pengguna') DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` (`username`, `nama`, `email`, `password`, `no_telp`, `role`) VALUES ('admin1','Florentino Perez','florentino@gmail.id','florentino123','081281281282','admin'),('admin2','Syekh Mansur','mansur@gmail.id','mansur123','08787654321','admin'),('aretha','August Aretha','aretha@gmail.id','aretha123','2062009760','pengguna'),('chloe','Norwood Chloe','chloe@gmail.id','chloe123','3192005425','pengguna'),('elena','Luvinia Elena','elena@gmail.id','elena123','6052001570','pengguna'),('gillian','Minerva Gillian','gillian@gmail.id','gillian123','2702000623','pengguna'),('gray','Gray Libby','gray@gmail.id','gray123','2032005054','pengguna'),('haylee','Haylee Edna','haylee@gmail.id','haylee123','2292003825','pengguna'),('kimberly','Kimberly Whitney','kimberly@gmail.id','kimberly','2122001848','pengguna'),('rodney','Hayden Rodney','rodney@gmail.id','rodney123','2762007792','pengguna'),('russell','Russell Adamina','russell@gmail.id','russell123','4792004966','pengguna'),('ryann','Ryann Jaqueline','ryann@gmail.id','ryann123','2252004545','pengguna');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-20 23:25:20
