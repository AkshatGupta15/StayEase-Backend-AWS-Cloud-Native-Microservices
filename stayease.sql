-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Host: stayease-db.cy360swu2vq9.us-east-1.rds.amazonaws.com:3306
-- Generation Time: Jun 23, 2025 at 09:28 PM
-- Server version: 8.0.41
-- PHP Version: 8.2.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `stayease`
--

-- --------------------------------------------------------

--
-- Table structure for table `properties`
--

CREATE TABLE `properties` (
  `id` varchar(99) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `description` text,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `properties`
--

INSERT INTO `properties` (`id`, `name`, `location`, `description`, `created_at`) VALUES
('PNY01', 'Hotel New York 1', 'New York', 'Luxury stay 1 in New York', '2025-06-23 18:52:13'),
('PNY02', 'Hotel New York 2', 'New York', 'Luxury stay 2 in New York', '2025-06-23 18:52:15'),
('PNY03', 'Hotel New York 3', 'New York', 'Luxury stay 3 in New York', '2025-06-23 18:52:18'),
('PNY04', 'Hotel New York 4', 'New York', 'Luxury stay 4 in New York', '2025-06-23 18:52:21'),
('PNY05', 'Hotel New York 5', 'New York', 'Luxury stay 5 in New York', '2025-06-23 18:52:23'),
('PSG01', 'Hotel Singapore 1', 'Singapore', 'Luxury stay 1 in Singapore', '2025-06-23 17:24:27'),
('PSG02', 'Hotel Singapore 2', 'Singapore', 'Luxury stay 2 in Singapore', '2025-06-23 17:24:30'),
('PSG03', 'Hotel Singapore 3', 'Singapore', 'Luxury stay 3 in Singapore', '2025-06-23 17:24:33'),
('PSG04', 'Hotel Singapore 4', 'Singapore', 'Luxury stay 4 in Singapore', '2025-06-23 17:24:37'),
('PSG05', 'Hotel Singapore 5', 'Singapore', 'Luxury stay 5 in Singapore', '2025-06-23 17:24:40'),
('PSG06', 'Hotel Singapore 6', 'Singapore', 'Luxury stay 6 in Singapore', '2025-06-23 17:24:44'),
('PSG07', 'Hotel Singapore 7', 'Singapore', 'Luxury stay 7 in Singapore', '2025-06-23 17:24:47'),
('PSG08', 'Hotel Singapore 8', 'Singapore', 'Luxury stay 8 in Singapore', '2025-06-23 17:24:51'),
('PSG09', 'Hotel Singapore 9', 'Singapore', 'Luxury stay 9 in Singapore', '2025-06-23 17:24:55'),
('PSG10', 'Hotel Singapore 10', 'Singapore', 'Luxury stay 10 in Singapore', '2025-06-23 17:24:59'),
('PSG11', 'Hotel Singapore 11', 'Singapore', 'Luxury stay 11 in Singapore', '2025-06-23 17:25:02'),
('PSG12', 'Hotel Singapore 12', 'Singapore', 'Luxury stay 12 in Singapore', '2025-06-23 17:25:06'),
('PSG13', 'Hotel Singapore 13', 'Singapore', 'Luxury stay 13 in Singapore', '2025-06-23 17:25:11'),
('PSG14', 'Hotel Singapore 14', 'Singapore', 'Luxury stay 14 in Singapore', '2025-06-23 17:25:14'),
('PSG15', 'Hotel Singapore 15', 'Singapore', 'Luxury stay 15 in Singapore', '2025-06-23 17:25:17'),
('PSG16', 'Hotel Singapore 16', 'Singapore', 'Luxury stay 16 in Singapore', '2025-06-23 17:25:21'),
('PSG17', 'Hotel Singapore 17', 'Singapore', 'Luxury stay 17 in Singapore', '2025-06-23 17:25:24'),
('PSG18', 'Hotel Singapore 18', 'Singapore', 'Luxury stay 18 in Singapore', '2025-06-23 17:25:28'),
('PSG19', 'Hotel Singapore 19', 'Singapore', 'Luxury stay 19 in Singapore', '2025-06-23 17:25:31'),
('PSG20', 'Hotel Singapore 20', 'Singapore', 'Luxury stay 20 in Singapore', '2025-06-23 17:25:34'),
('PSG21', 'Hotel Singapore 21', 'Singapore', 'Luxury stay 21 in Singapore', '2025-06-23 17:25:38'),
('PSG22', 'Hotel Singapore 22', 'Singapore', 'Luxury stay 22 in Singapore', '2025-06-23 17:25:41'),
('PSG23', 'Hotel Singapore 23', 'Singapore', 'Luxury stay 23 in Singapore', '2025-06-23 17:25:44'),
('PSG24', 'Hotel Singapore 24', 'Singapore', 'Luxury stay 24 in Singapore', '2025-06-23 17:25:47'),
('PSG25', 'Hotel Singapore 25', 'Singapore', 'Luxury stay 25 in Singapore', '2025-06-23 17:25:51'),
('PSG26', 'Hotel Singapore 26', 'Singapore', 'Luxury stay 26 in Singapore', '2025-06-23 17:25:55'),
('PSG27', 'Hotel Singapore 27', 'Singapore', 'Luxury stay 27 in Singapore', '2025-06-23 17:25:58'),
('PSG28', 'Hotel Singapore 28', 'Singapore', 'Luxury stay 28 in Singapore', '2025-06-23 17:26:01'),
('PSG29', 'Hotel Singapore 29', 'Singapore', 'Luxury stay 29 in Singapore', '2025-06-23 17:26:05'),
('PSG30', 'Hotel Singapore 30', 'Singapore', 'Luxury stay 30 in Singapore', '2025-06-23 17:26:08'),
('PSG31', 'Hotel Singapore 31', 'Singapore', 'Luxury stay 31 in Singapore', '2025-06-23 17:26:11'),
('PSG32', 'Hotel Singapore 32', 'Singapore', 'Luxury stay 32 in Singapore', '2025-06-23 17:26:15'),
('PSG33', 'Hotel Singapore 33', 'Singapore', 'Luxury stay 33 in Singapore', '2025-06-23 17:26:18'),
('PSG34', 'Hotel Singapore 34', 'Singapore', 'Luxury stay 34 in Singapore', '2025-06-23 17:26:22'),
('PSG35', 'Hotel Singapore 35', 'Singapore', 'Luxury stay 35 in Singapore', '2025-06-23 17:26:25'),
('PSG36', 'Hotel Singapore 36', 'Singapore', 'Luxury stay 36 in Singapore', '2025-06-23 17:26:28'),
('PSG37', 'Hotel Singapore 37', 'Singapore', 'Luxury stay 37 in Singapore', '2025-06-23 17:26:31'),
('PSG38', 'Hotel Singapore 38', 'Singapore', 'Luxury stay 38 in Singapore', '2025-06-23 17:26:34'),
('PSG39', 'Hotel Singapore 39', 'Singapore', 'Luxury stay 39 in Singapore', '2025-06-23 17:26:38'),
('PSG40', 'Hotel Singapore 40', 'Singapore', 'Luxury stay 40 in Singapore', '2025-06-23 17:26:42'),
('PSG41', 'Hotel Singapore 41', 'Singapore', 'Luxury stay 41 in Singapore', '2025-06-23 17:26:45'),
('PSG42', 'Hotel Singapore 42', 'Singapore', 'Luxury stay 42 in Singapore', '2025-06-23 17:26:49'),
('PSG43', 'Hotel Singapore 43', 'Singapore', 'Luxury stay 43 in Singapore', '2025-06-23 17:26:52'),
('PSG44', 'Hotel Singapore 44', 'Singapore', 'Luxury stay 44 in Singapore', '2025-06-23 17:26:56'),
('PSG45', 'Hotel Singapore 45', 'Singapore', 'Luxury stay 45 in Singapore', '2025-06-23 17:27:00'),
('PSG46', 'Hotel Singapore 46', 'Singapore', 'Luxury stay 46 in Singapore', '2025-06-23 17:27:03'),
('PSG47', 'Hotel Singapore 47', 'Singapore', 'Luxury stay 47 in Singapore', '2025-06-23 17:27:06'),
('PSG48', 'Hotel Singapore 48', 'Singapore', 'Luxury stay 48 in Singapore', '2025-06-23 17:27:10'),
('PSG49', 'Hotel Singapore 49', 'Singapore', 'Luxury stay 49 in Singapore', '2025-06-23 17:27:14'),
('PSG50', 'Hotel Singapore 50', 'Singapore', 'Luxury stay 50 in Singapore', '2025-06-23 17:27:18');

-- --------------------------------------------------------

--
-- Table structure for table `rooms`
--

CREATE TABLE `rooms` (
  `id` int NOT NULL,
  `property_id` varchar(99) NOT NULL,
  `room_type` varchar(99) NOT NULL,
  `price_per_night` float NOT NULL,
  `available` tinyint(1) DEFAULT '1',
  `max_guests` int NOT NULL,
  `image_url` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `rooms`
--

INSERT INTO `rooms` (`id`, `property_id`, `room_type`, `price_per_night`, `available`, `max_guests`, `image_url`, `created_at`) VALUES
(20, 'P01', 'Executive Suite', 300, 0, 4, NULL, '2025-06-21 19:10:56'),
(21, 'P01', 'Deluxe King', 250, 1, 3, NULL, '2025-06-21 19:13:04'),
(22, 'P01', 'Deluxe King', 250, 1, 3, NULL, '2025-06-21 19:15:24'),
(23, 'P01', 'Deluxe King', 250, 1, 3, NULL, '2025-06-21 19:16:21'),
(24, 'P01', 'Executive Suite', 300, 0, 4, 'https://stayease-room-images.s3.amazonaws.com/rooms/24/room1.jpg', '2025-06-21 19:17:54'),
(25, 'P01', 'Executive Suite', 300, 0, 4, 'https://stayease-room-images.s3.amazonaws.com/rooms/25/room1.jpg', '2025-06-21 21:59:56'),
(26, 'P01', 'Executive Suite', 300, 0, 4, 'https://stayease-room-images.s3.amazonaws.com/rooms/26/room1.jpg', '2025-06-21 22:01:36'),
(27, 'P01', 'Executive Suite', 300, 0, 4, 'https://stayease-room-images.s3.amazonaws.com/rooms/27/room1.jpg', '2025-06-22 15:39:50'),
(28, 'PSG01', 'Standard', 276, 1, 4, NULL, '2025-06-23 17:24:28'),
(29, 'PSG02', 'Suite', 198, 1, 2, NULL, '2025-06-23 17:24:31'),
(30, 'PSG03', 'Standard', 284, 1, 3, NULL, '2025-06-23 17:24:35'),
(31, 'PSG04', 'Suite', 104, 1, 3, NULL, '2025-06-23 17:24:38'),
(32, 'PSG05', 'Standard', 330, 1, 2, NULL, '2025-06-23 17:24:41'),
(33, 'PSG06', 'Standard', 320, 1, 4, NULL, '2025-06-23 17:24:45'),
(34, 'PSG07', 'Standard', 427, 1, 1, NULL, '2025-06-23 17:24:49'),
(35, 'PSG08', 'Standard', 293, 1, 3, NULL, '2025-06-23 17:24:52'),
(36, 'PSG09', 'Standard', 286, 1, 2, NULL, '2025-06-23 17:24:56'),
(37, 'PSG10', 'Standard', 295, 1, 3, NULL, '2025-06-23 17:25:00'),
(38, 'PSG11', 'Suite', 130, 1, 2, NULL, '2025-06-23 17:25:03'),
(39, 'PSG12', 'Standard', 321, 1, 1, NULL, '2025-06-23 17:25:08'),
(40, 'PSG13', 'Suite', 430, 1, 4, NULL, '2025-06-23 17:25:12'),
(41, 'PSG14', 'Suite', 447, 1, 3, NULL, '2025-06-23 17:25:15'),
(42, 'PSG15', 'Suite', 483, 1, 4, NULL, '2025-06-23 17:25:19'),
(43, 'PSG16', 'Standard', 305, 1, 1, NULL, '2025-06-23 17:25:22'),
(44, 'PSG17', 'Deluxe', 426, 1, 1, NULL, '2025-06-23 17:25:26'),
(45, 'PSG18', 'Deluxe', 395, 1, 3, NULL, '2025-06-23 17:25:29'),
(46, 'PSG19', 'Suite', 129, 1, 1, NULL, '2025-06-23 17:25:32'),
(47, 'PSG20', 'Standard', 339, 1, 1, NULL, '2025-06-23 17:25:35'),
(48, 'PSG21', 'Standard', 197, 1, 1, NULL, '2025-06-23 17:25:39'),
(49, 'PSG22', 'Deluxe', 479, 1, 3, NULL, '2025-06-23 17:25:42'),
(50, 'PSG23', 'Suite', 381, 1, 4, NULL, '2025-06-23 17:25:45'),
(51, 'PSG24', 'Standard', 442, 1, 3, NULL, '2025-06-23 17:25:49'),
(52, 'PSG25', 'Suite', 470, 1, 4, NULL, '2025-06-23 17:25:52'),
(53, 'PSG26', 'Suite', 315, 1, 4, NULL, '2025-06-23 17:25:56'),
(54, 'PSG27', 'Standard', 286, 1, 4, NULL, '2025-06-23 17:25:59'),
(55, 'PSG28', 'Deluxe', 197, 1, 2, NULL, '2025-06-23 17:26:02'),
(56, 'PSG29', 'Suite', 156, 1, 2, NULL, '2025-06-23 17:26:06'),
(57, 'PSG30', 'Deluxe', 393, 1, 2, NULL, '2025-06-23 17:26:09'),
(58, 'PSG31', 'Deluxe', 434, 1, 2, NULL, '2025-06-23 17:26:13'),
(59, 'PSG32', 'Deluxe', 136, 1, 3, NULL, '2025-06-23 17:26:16'),
(60, 'PSG33', 'Suite', 174, 1, 2, NULL, '2025-06-23 17:26:19'),
(61, 'PSG34', 'Deluxe', 354, 1, 3, NULL, '2025-06-23 17:26:23'),
(62, 'PSG35', 'Suite', 354, 1, 4, NULL, '2025-06-23 17:26:26'),
(63, 'PSG36', 'Suite', 496, 1, 2, NULL, '2025-06-23 17:26:29'),
(64, 'PSG37', 'Deluxe', 346, 1, 4, NULL, '2025-06-23 17:26:32'),
(65, 'PSG38', 'Standard', 113, 1, 4, NULL, '2025-06-23 17:26:36'),
(66, 'PSG39', 'Standard', 303, 1, 4, NULL, '2025-06-23 17:26:40'),
(67, 'PSG40', 'Deluxe', 421, 1, 1, NULL, '2025-06-23 17:26:43'),
(68, 'PSG41', 'Suite', 294, 1, 2, NULL, '2025-06-23 17:26:46'),
(69, 'PSG42', 'Suite', 184, 1, 4, NULL, '2025-06-23 17:26:50'),
(70, 'PSG43', 'Suite', 198, 1, 1, NULL, '2025-06-23 17:26:53'),
(71, 'PSG44', 'Suite', 104, 1, 2, NULL, '2025-06-23 17:26:57'),
(72, 'PSG45', 'Deluxe', 481, 1, 2, NULL, '2025-06-23 17:27:01'),
(73, 'PSG46', 'Standard', 241, 1, 3, NULL, '2025-06-23 17:27:04'),
(74, 'PSG47', 'Standard', 441, 1, 1, NULL, '2025-06-23 17:27:08'),
(75, 'PSG48', 'Deluxe', 379, 1, 2, NULL, '2025-06-23 17:27:12'),
(76, 'PSG49', 'Deluxe', 247, 1, 1, NULL, '2025-06-23 17:27:15'),
(77, 'PSG50', 'Standard', 330, 1, 2, NULL, '2025-06-23 17:27:19'),
(78, 'PSG01', 'Standard', 433, 1, 2, NULL, '2025-06-23 18:44:26'),
(79, 'PSG02', 'Suite', 158, 1, 1, NULL, '2025-06-23 18:44:28'),
(80, 'PNY01', 'Deluxe', 112, 1, 3, NULL, '2025-06-23 18:52:14'),
(81, 'PNY02', 'Deluxe', 231, 1, 4, NULL, '2025-06-23 18:52:16'),
(82, 'PNY03', 'Suite', 213, 1, 2, NULL, '2025-06-23 18:52:19'),
(83, 'PNY04', 'Deluxe', 155, 1, 1, NULL, '2025-06-23 18:52:21'),
(84, 'PNY05', 'Deluxe', 283, 1, 3, NULL, '2025-06-23 18:52:24');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `properties`
--
ALTER TABLE `properties`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rooms`
--
ALTER TABLE `rooms`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `rooms`
--
ALTER TABLE `rooms`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=85;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
