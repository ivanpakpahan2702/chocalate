-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.4.14-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for cochalate_db
CREATE DATABASE IF NOT EXISTS `cochalate_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `cochalate_db`;

-- Dumping structure for table cochalate_db.tbl_accounts
CREATE TABLE IF NOT EXISTS `tbl_accounts` (
  `Id_Account` int(11) NOT NULL AUTO_INCREMENT,
  `Full_Name` varchar(50) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Username` varchar(50) DEFAULT NULL,
  `Password` varchar(50) DEFAULT NULL,
  `Role` varchar(50) DEFAULT NULL,
  `Question` text DEFAULT NULL,
  `Answer` text DEFAULT NULL,
  `Created_At` date DEFAULT NULL,
  `Updated_At` date DEFAULT NULL,
  PRIMARY KEY (`Id_Account`),
  UNIQUE KEY `Username` (`Username`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table cochalate_db.tbl_accounts: ~4 rows (approximately)
/*!40000 ALTER TABLE `tbl_accounts` DISABLE KEYS */;
INSERT INTO `tbl_accounts` (`Id_Account`, `Full_Name`, `Email`, `Username`, `Password`, `Role`, `Question`, `Answer`, `Created_At`, `Updated_At`) VALUES
	(5, NULL, 'ivanpakpahanchrst@gmail.com', 'ivan27', '400cd8036423ee9725c4078320d1c81b', 'Admin', '', '2', '2023-07-27', '2023-07-27'),
	(10, NULL, 'ivanpakpahanchrst@gmail.com', 'Vale', '81dc9bdb52d04dc20036dbd8313ed055', 'User', '2 + 4', '6', NULL, NULL),
	(13, NULL, 'ivanime027@gmail.com', 'Buli', '81dc9bdb52d04dc20036dbd8313ed055', 'User', '', '', NULL, NULL),
	(14, NULL, 'ivanpakpahanchrst@gmail.com', 'admin', '202cb962ac59075b964b07152d234b70', 'User', '', '', NULL, NULL);
/*!40000 ALTER TABLE `tbl_accounts` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
