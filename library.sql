-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 02, 2018 at 10:18 PM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` varchar(16) NOT NULL,
  `password` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `password`) VALUES
('admin', '123');

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `book_name` varchar(60) NOT NULL,
  `isbn` bigint(13) NOT NULL,
  `quantity` bigint(6) NOT NULL,
  `issued` bigint(6) NOT NULL,
  `available` bigint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`book_name`, `isbn`, `quantity`, `issued`, `available`) VALUES
('Head First PHP', 9780596006303, 300, 1, 299),
('Head First Java', 9780596009205, 350, 0, 350),
('Head First C#', 9781449343507, 300, 2, 298),
('Head First Python', 9781449382674, 400, 2, 398);

-- --------------------------------------------------------

--
-- Table structure for table `issuebook`
--

CREATE TABLE `issuebook` (
  `rollno` bigint(10) NOT NULL,
  `book_name` varchar(60) NOT NULL,
  `isbn` bigint(13) NOT NULL,
  `issue_date` date NOT NULL,
  `return_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `issuebook`
--

INSERT INTO `issuebook` (`rollno`, `book_name`, `isbn`, `issue_date`, `return_date`) VALUES
(181001, 'Head First C#', 9781449343507, '2018-10-21', '2018-11-04'),
(181001, 'Head First Python', 9781449382674, '2018-10-19', '2018-11-02'),
(181007, 'Head First PHP', 9780596006303, '2018-10-21', '2018-11-04'),
(181007, 'Head First C#', 9781449343507, '2018-10-18', '2018-11-01'),
(181007, 'Head First Python', 9781449382674, '2018-10-18', '2018-11-01');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `rollno` bigint(10) NOT NULL,
  `student_name` varchar(20) NOT NULL,
  `father_name` varchar(20) NOT NULL,
  `contact` bigint(10) NOT NULL,
  `dob` date NOT NULL,
  `branch` char(3) NOT NULL,
  `fine` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`rollno`, `student_name`, `father_name`, `contact`, `dob`, `branch`, `fine`) VALUES
(181001, 'Atul Kumar', 'Bhushan Kumar', 9823421314, '1998-01-10', 'CSE', 0),
(181002, 'Anand Jangra', 'Pulkit Jangra', 9842131413, '1998-06-21', 'CSE', 0),
(181007, 'Rohan Dagar', 'Vikram Dagar', 9876543210, '1994-12-30', 'CSE', 0),
(181010, 'Bhaskar Verma', 'Mohit Verma', 8013526363, '1998-06-19', 'CSE', 0),
(181023, 'Janki Raman', 'Mohit Raman', 8012135263, '1998-04-12', 'CSE', 0),
(181040, 'Mukul Gupta', 'Govind Gupta', 9723479376, '1998-09-21', 'CSE', 0),
(182001, 'Ankit Tomar', 'Ranvir Tomar', 7812573948, '1998-03-10', 'IT', 8),
(182017, 'Keshav Nand', 'Suresh Nand', 9812345241, '1998-01-20', 'IT', 0),
(182034, 'Mohit Singh', 'Pankaj Singh', 9812345678, '1998-02-12', 'IT', 0),
(182039, 'Rahul Joshi', 'Puskar Joshi', 8056382647, '1997-04-14', 'IT', 0),
(182054, 'Neha Singh', 'Natwar Singh', 9826318912, '1998-01-11', 'IT', 0),
(183003, 'Anjali Rana', 'Ankit Rana', 9817237263, '1999-07-17', 'ECE', 0),
(183020, 'Kiran Negi', 'Pawan Negi', 7813227245, '2000-12-12', 'ECE', 0),
(183024, 'Aman Shukla', 'Anand Shukla', 7812448492, '1999-03-19', 'ECE', 0),
(183042, 'Rohit Ranjan', 'Rakesh Ranjan', 8032938294, '2001-08-16', 'ECE', 0),
(183048, 'Hemant Jha', 'Mukul Jha', 7812132572, '1997-11-12', 'ECE', 0),
(184001, 'Aman Kumar', 'Anand Kumar', 7812324222, '1999-04-13', 'ME', 0),
(184006, 'Bharti Shaw', 'Pawan Shaw', 9872525363, '1999-02-27', 'ME', 0),
(184029, 'Naveen Dagar', 'Anshul Dagar', 9823143525, '1998-11-15', 'ME', 0),
(184055, 'Pulkit Kumar', 'Hemant Kumar', 8012246226, '1999-05-16', 'ME', 0),
(184057, 'Ankit Rana', 'Shukhdev Rana', 8908271417, '1998-11-12', 'ME', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`isbn`);

--
-- Indexes for table `issuebook`
--
ALTER TABLE `issuebook`
  ADD PRIMARY KEY (`rollno`,`isbn`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`rollno`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
