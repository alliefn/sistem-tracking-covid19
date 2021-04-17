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
  `kasus_total` int(11) DEFAULT NULL,
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
/*!40000 ALTER TABLE `DataCovid` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Kamar`
--

DROP TABLE IF EXISTS `Kamar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Kamar` (
  `id_kamar` int(11) NOT NULL,
  `id_RS` int(11) DEFAULT NULL,
  `harga` int(11) DEFAULT NULL,
  `jumlah` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_kamar`),
  KEY `FK_Kamar_RumahSakit` (`id_RS`),
  CONSTRAINT `FK_Kamar_RumahSakit` FOREIGN KEY (`id_RS`) REFERENCES `RumahSakit` (`id_RS`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Kamar`
--

LOCK TABLES `Kamar` WRITE;
/*!40000 ALTER TABLE `Kamar` DISABLE KEYS */;
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
  CONSTRAINT `FK_Pesanan_Kamar` FOREIGN KEY (`id_kamar`) REFERENCES `Kamar` (`id_kamar`),
  CONSTRAINT `FK_Pesanan_User` FOREIGN KEY (`username`) REFERENCES `User` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Pesanan`
--

LOCK TABLES `Pesanan` WRITE;
/*!40000 ALTER TABLE `Pesanan` DISABLE KEYS */;
/*!40000 ALTER TABLE `Pesanan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RumahSakit`
--

DROP TABLE IF EXISTS `RumahSakit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `RumahSakit` (
  `id_RS` int(11) NOT NULL,
  `nama` varchar(255) DEFAULT NULL,
  `alamat` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_RS`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RumahSakit`
--

LOCK TABLES `RumahSakit` WRITE;
/*!40000 ALTER TABLE `RumahSakit` DISABLE KEYS */;
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
  `membership_status` bit(1) DEFAULT NULL,
  `role` enum('admin','pengguna') DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
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

-- Dump completed on 2021-04-17 23:53:59
