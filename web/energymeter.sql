-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 24, 2019 at 11:52 PM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 7.2.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `energymeter`
--

-- --------------------------------------------------------

--
-- Table structure for table `bill`
--

CREATE TABLE `bill` (
  `unit` varchar(10) NOT NULL,
  `charges` varchar(10) NOT NULL,
  `meter_number` varchar(10) NOT NULL,
  `location` varchar(20) NOT NULL,
  `past_unit` varchar(10) NOT NULL,
  `current_unit` varchar(10) NOT NULL,
  `consumed_unit` varchar(10) NOT NULL,
  `charges_per_unit` varchar(10) NOT NULL,
  `total_charges` varchar(10) NOT NULL,
  `tax` varchar(10) NOT NULL,
  `bill` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bill`
--

INSERT INTO `bill` (`unit`, `charges`, `meter_number`, `location`, `past_unit`, `current_unit`, `consumed_unit`, `charges_per_unit`, `total_charges`, `tax`, `bill`) VALUES
('<100', '5.7', '1', 'room 1', '300', '400', '100', '6.5', '650', '0', '650'),
('<200', '6.5', '2', 'room 2', '500', '800', '300', '8.5', '2550', '0', '2550'),
('<300', '7.5', '3', 'room 3', '700', '1700', '1000', '10.5', '10500', '25', '10525'),
('<600', '8.5', '', '', '', '', '', '', '', '', ''),
('<1000', '9.5', '', '', '', '', '', '', '', '', ''),
('>=1000', '10.5', '', '', '', '', '', '', '', '', '');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
