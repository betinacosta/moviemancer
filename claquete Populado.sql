-- phpMyAdmin SQL Dump
-- version 4.0.4.2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 20, 2016 at 01:07 AM
-- Server version: 5.6.13
-- PHP Version: 5.4.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `claquete`
--
CREATE DATABASE IF NOT EXISTS `claquete` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `claquete`;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=25 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add question', 1, 'add_question'),
(2, 'Can change question', 1, 'change_question'),
(3, 'Can delete question', 1, 'delete_question'),
(4, 'Can add choice', 2, 'add_choice'),
(5, 'Can change choice', 2, 'change_choice'),
(6, 'Can delete choice', 2, 'delete_choice'),
(7, 'Can add log entry', 3, 'add_logentry'),
(8, 'Can change log entry', 3, 'change_logentry'),
(9, 'Can delete log entry', 3, 'delete_logentry'),
(10, 'Can add permission', 4, 'add_permission'),
(11, 'Can change permission', 4, 'change_permission'),
(12, 'Can delete permission', 4, 'delete_permission'),
(13, 'Can add user', 5, 'add_user'),
(14, 'Can change user', 5, 'change_user'),
(15, 'Can delete user', 5, 'delete_user'),
(16, 'Can add group', 6, 'add_group'),
(17, 'Can change group', 6, 'change_group'),
(18, 'Can delete group', 6, 'delete_group'),
(19, 'Can add content type', 7, 'add_contenttype'),
(20, 'Can change content type', 7, 'change_contenttype'),
(21, 'Can delete content type', 7, 'delete_contenttype'),
(22, 'Can add session', 8, 'add_session'),
(23, 'Can change session', 8, 'change_session'),
(24, 'Can delete session', 8, 'delete_session');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `cast`
--

CREATE TABLE IF NOT EXISTS `cast` (
  `cast_ID` int(11) NOT NULL AUTO_INCREMENT,
  `tmdb_cast_ID` int(11) NOT NULL,
  PRIMARY KEY (`cast_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(3, 'admin', 'logentry'),
(6, 'auth', 'group'),
(4, 'auth', 'permission'),
(5, 'auth', 'user'),
(7, 'contenttypes', 'contenttype'),
(2, 'recommendation', 'choice'),
(1, 'recommendation', 'question'),
(8, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=16 ;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2016-09-28 23:43:29.704000'),
(2, 'auth', '0001_initial', '2016-09-28 23:43:42.155000'),
(3, 'admin', '0001_initial', '2016-09-28 23:43:44.803000'),
(4, 'admin', '0002_logentry_remove_auto_add', '2016-09-28 23:43:44.853000'),
(5, 'contenttypes', '0002_remove_content_type_name', '2016-09-28 23:43:46.367000'),
(6, 'auth', '0002_alter_permission_name_max_length', '2016-09-28 23:43:47.199000'),
(7, 'auth', '0003_alter_user_email_max_length', '2016-09-28 23:43:48.175000'),
(8, 'auth', '0004_alter_user_username_opts', '2016-09-28 23:43:48.219000'),
(9, 'auth', '0005_alter_user_last_login_null', '2016-09-28 23:43:49.151000'),
(10, 'auth', '0006_require_contenttypes_0002', '2016-09-28 23:43:49.184000'),
(11, 'auth', '0007_alter_validators_add_error_messages', '2016-09-28 23:43:49.230000'),
(12, 'auth', '0008_alter_user_username_max_length', '2016-09-28 23:43:50.253000'),
(13, 'recommendation', '0001_initial', '2016-09-28 23:43:52.741000'),
(14, 'recommendation', '0002_auto_20160919_0220', '2016-09-28 23:43:52.843000'),
(15, 'sessions', '0001_initial', '2016-09-28 23:43:53.585000');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `genre`
--

CREATE TABLE IF NOT EXISTS `genre` (
  `genre_ID` int(11) NOT NULL AUTO_INCREMENT,
  `tmdb_genre_ID` int(11) NOT NULL,
  `genre_name` varchar(50) NOT NULL,
  PRIMARY KEY (`genre_ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=20 ;

--
-- Dumping data for table `genre`
--

INSERT INTO `genre` (`genre_ID`, `tmdb_genre_ID`, `genre_name`) VALUES
(1, 28, 'Ação'),
(2, 12, 'Aventura'),
(3, 16, 'Animação'),
(4, 35, 'Comédia'),
(5, 80, 'Crime'),
(6, 99, 'Documentário'),
(7, 18, 'Drama'),
(8, 10751, 'Família'),
(9, 14, 'Fantasia'),
(10, 36, 'História'),
(11, 27, 'Terror'),
(12, 10402, 'Música'),
(13, 9648, 'Mistério'),
(14, 10749, 'Romance'),
(15, 878, 'Ficcção Científica'),
(16, 10770, 'Cinema TV'),
(17, 53, 'Thriller'),
(18, 10752, 'Guerra'),
(19, 37, 'Faroeste');

-- --------------------------------------------------------

--
-- Table structure for table `list`
--

CREATE TABLE IF NOT EXISTS `list` (
  `list_ID` int(11) NOT NULL AUTO_INCREMENT,
  `user_ID` int(11) NOT NULL,
  `type_ID` int(11) NOT NULL,
  PRIMARY KEY (`list_ID`),
  KEY `type_ID` (`type_ID`),
  KEY `user_ID` (`user_ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=79 ;

--
-- Dumping data for table `list`
--

INSERT INTO `list` (`list_ID`, `user_ID`, `type_ID`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 2, 1),
(4, 2, 2),
(5, 2, 3),
(6, 3, 1),
(7, 3, 2),
(8, 3, 3),
(9, 4, 1),
(10, 4, 2),
(11, 4, 3),
(12, 5, 1),
(13, 5, 2),
(14, 5, 3),
(15, 6, 1),
(16, 6, 2),
(17, 6, 3),
(18, 7, 1),
(19, 7, 2),
(20, 7, 3),
(21, 8, 1),
(22, 8, 2),
(23, 8, 3),
(24, 9, 1),
(25, 9, 2),
(26, 9, 3),
(27, 10, 1),
(28, 10, 2),
(29, 10, 3),
(30, 11, 1),
(31, 11, 2),
(32, 11, 3),
(33, 12, 1),
(34, 12, 2),
(35, 12, 3),
(36, 13, 1),
(37, 13, 2),
(38, 13, 3),
(39, 14, 1),
(40, 14, 2),
(41, 14, 3),
(42, 15, 1),
(43, 15, 2),
(44, 15, 3),
(45, 16, 1),
(46, 16, 2),
(47, 16, 3),
(48, 17, 1),
(49, 17, 2),
(50, 17, 3),
(51, 18, 1),
(52, 18, 2),
(53, 18, 3),
(54, 19, 1),
(55, 19, 2),
(56, 19, 3),
(57, 20, 1),
(58, 20, 2),
(59, 20, 3),
(60, 21, 1),
(61, 21, 2),
(62, 21, 3),
(63, 22, 1),
(64, 22, 2),
(65, 22, 3),
(66, 23, 1),
(67, 23, 2),
(68, 23, 3),
(69, 24, 1),
(70, 24, 2),
(71, 24, 3),
(72, 25, 1),
(73, 25, 2),
(74, 25, 3),
(75, 26, 1),
(76, 26, 2),
(77, 26, 3),
(78, 1, 3);

-- --------------------------------------------------------

--
-- Table structure for table `movie`
--

CREATE TABLE IF NOT EXISTS `movie` (
  `movie_ID` int(11) NOT NULL AUTO_INCREMENT,
  `tmdb_movie_ID` int(11) NOT NULL,
  PRIMARY KEY (`movie_ID`),
  UNIQUE KEY `tmdb_movie_ID` (`tmdb_movie_ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=44 ;

--
-- Dumping data for table `movie`
--

INSERT INTO `movie` (`movie_ID`, `tmdb_movie_ID`) VALUES
(4, 101),
(5, 155),
(28, 272),
(27, 278),
(2, 603),
(38, 675),
(30, 680),
(37, 2501),
(6, 9648),
(1, 27205),
(13, 43074),
(21, 47933),
(10, 76341),
(12, 87101),
(22, 118340),
(8, 135397),
(11, 140607),
(7, 157336),
(42, 168259),
(9, 188927),
(33, 198663),
(25, 206647),
(16, 209112),
(34, 210577),
(20, 241259),
(39, 246655),
(40, 258489),
(31, 259693),
(3, 271110),
(29, 273248),
(36, 273481),
(19, 278154),
(18, 290250),
(17, 291805),
(15, 293660),
(23, 297761),
(26, 300669),
(43, 302946),
(24, 325789),
(32, 332567),
(35, 333371),
(14, 333484),
(41, 343611);

-- --------------------------------------------------------

--
-- Table structure for table `movie_list`
--

CREATE TABLE IF NOT EXISTS `movie_list` (
  `movie_list_ID` int(11) NOT NULL AUTO_INCREMENT,
  `movie_ID` int(11) NOT NULL,
  `list_ID` int(11) NOT NULL,
  PRIMARY KEY (`movie_list_ID`),
  KEY `movie_ID` (`movie_ID`,`list_ID`),
  KEY `list_ID` (`list_ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=49 ;

--
-- Dumping data for table `movie_list`
--

INSERT INTO `movie_list` (`movie_list_ID`, `movie_ID`, `list_ID`) VALUES
(1, 1, 1),
(39, 1, 50),
(2, 2, 1),
(3, 3, 1),
(11, 3, 29),
(19, 3, 32),
(4, 4, 1),
(46, 5, 62),
(5, 6, 20),
(13, 7, 29),
(14, 8, 29),
(15, 9, 29),
(16, 10, 29),
(17, 11, 29),
(18, 12, 29),
(20, 13, 32),
(21, 14, 35),
(22, 15, 38),
(23, 16, 38),
(6, 17, 20),
(7, 18, 20),
(9, 19, 23),
(10, 20, 23),
(12, 21, 29),
(24, 22, 38),
(25, 23, 41),
(26, 24, 41),
(27, 25, 41),
(28, 26, 41),
(29, 27, 41),
(30, 28, 41),
(8, 29, 20),
(31, 29, 41),
(32, 30, 47),
(33, 31, 47),
(34, 32, 47),
(36, 33, 50),
(37, 34, 50),
(38, 35, 50),
(40, 36, 50),
(41, 37, 50),
(42, 38, 53),
(43, 39, 53),
(44, 40, 53),
(35, 41, 50),
(45, 41, 56),
(47, 42, 62),
(48, 43, 62);

-- --------------------------------------------------------

--
-- Table structure for table `profile`
--

CREATE TABLE IF NOT EXISTS `profile` (
  `profile_ID` int(11) NOT NULL AUTO_INCREMENT,
  `user_ID` int(11) NOT NULL,
  PRIMARY KEY (`profile_ID`),
  UNIQUE KEY `user_ID_2` (`user_ID`),
  KEY `user_ID` (`user_ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=31 ;

--
-- Dumping data for table `profile`
--

INSERT INTO `profile` (`profile_ID`, `user_ID`) VALUES
(5, 1),
(6, 2),
(7, 3),
(8, 4),
(9, 5),
(30, 6),
(10, 7),
(11, 8),
(12, 9),
(13, 10),
(14, 11),
(15, 12),
(16, 13),
(17, 14),
(18, 15),
(19, 16),
(20, 17),
(21, 18),
(22, 19),
(23, 20),
(24, 21),
(25, 22),
(26, 23),
(27, 24),
(28, 25),
(29, 26);

-- --------------------------------------------------------

--
-- Table structure for table `profile_cast`
--

CREATE TABLE IF NOT EXISTS `profile_cast` (
  `profile_cast_ID` int(11) NOT NULL AUTO_INCREMENT,
  `profile_ID` int(11) NOT NULL,
  `cast_ID` int(11) NOT NULL,
  PRIMARY KEY (`profile_cast_ID`),
  KEY `profile_ID` (`profile_ID`,`cast_ID`),
  KEY `cast_ID` (`cast_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `profile_genre`
--

CREATE TABLE IF NOT EXISTS `profile_genre` (
  `profile_genre_ID` int(11) NOT NULL AUTO_INCREMENT,
  `profile_ID` int(11) NOT NULL,
  `genre_ID` int(11) NOT NULL,
  PRIMARY KEY (`profile_genre_ID`),
  KEY `profile_ID` (`profile_ID`,`genre_ID`),
  KEY `genre_ID` (`genre_ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=81 ;

--
-- Dumping data for table `profile_genre`
--

INSERT INTO `profile_genre` (`profile_genre_ID`, `profile_ID`, `genre_ID`) VALUES
(5, 5, 1),
(4, 5, 5),
(1, 5, 13),
(7, 6, 6),
(8, 6, 7),
(6, 6, 10),
(10, 7, 6),
(11, 7, 7),
(9, 7, 10),
(12, 8, 10),
(14, 8, 14),
(13, 8, 18),
(16, 9, 6),
(15, 9, 10),
(17, 9, 18),
(22, 10, 4),
(21, 10, 13),
(23, 10, 19),
(24, 11, 1),
(26, 11, 3),
(25, 11, 8),
(27, 12, 5),
(28, 12, 12),
(29, 12, 17),
(31, 13, 9),
(30, 13, 13),
(32, 13, 15),
(33, 14, 1),
(34, 14, 2),
(35, 14, 17),
(37, 15, 1),
(38, 15, 2),
(36, 15, 13),
(40, 16, 1),
(41, 16, 4),
(39, 16, 5),
(42, 17, 5),
(44, 17, 8),
(43, 17, 13),
(46, 18, 1),
(47, 18, 3),
(45, 18, 13),
(49, 19, 1),
(48, 19, 5),
(50, 19, 11),
(52, 20, 1),
(53, 20, 5),
(51, 20, 13),
(55, 21, 1),
(56, 21, 5),
(54, 21, 13),
(58, 22, 1),
(59, 22, 5),
(57, 22, 13),
(61, 23, 1),
(62, 23, 5),
(60, 23, 13),
(64, 24, 1),
(65, 24, 5),
(63, 24, 13),
(67, 25, 4),
(68, 25, 8),
(66, 25, 12),
(71, 26, 9),
(69, 26, 17),
(70, 26, 19),
(73, 27, 2),
(74, 27, 4),
(72, 27, 19),
(76, 28, 7),
(77, 28, 9),
(75, 28, 14),
(79, 29, 9),
(80, 29, 12),
(78, 29, 15),
(19, 30, 6),
(20, 30, 7),
(18, 30, 10);

-- --------------------------------------------------------

--
-- Table structure for table `rate`
--

CREATE TABLE IF NOT EXISTS `rate` (
  `rate_ID` int(11) NOT NULL AUTO_INCREMENT,
  `rate` int(11) NOT NULL,
  PRIMARY KEY (`rate_ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `rate`
--

INSERT INTO `rate` (`rate_ID`, `rate`) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

-- --------------------------------------------------------

--
-- Table structure for table `rating`
--

CREATE TABLE IF NOT EXISTS `rating` (
  `rating_ID` int(11) NOT NULL AUTO_INCREMENT,
  `user_ID` int(11) NOT NULL,
  `movie_ID` int(11) NOT NULL,
  `rate_ID` int(11) NOT NULL,
  PRIMARY KEY (`rating_ID`),
  KEY `user_ID` (`user_ID`,`movie_ID`,`rate_ID`),
  KEY `movie_ID` (`movie_ID`),
  KEY `rate_ID` (`rate_ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=45 ;

--
-- Dumping data for table `rating`
--

INSERT INTO `rating` (`rating_ID`, `user_ID`, `movie_ID`, `rate_ID`) VALUES
(1, 7, 6, 5),
(2, 7, 17, 2),
(3, 7, 18, 5),
(4, 7, 29, 3),
(5, 8, 19, 5),
(6, 8, 20, 1),
(7, 10, 3, 3),
(9, 10, 7, 5),
(10, 10, 8, 3),
(11, 10, 9, 5),
(12, 10, 10, 5),
(13, 10, 11, 5),
(14, 10, 12, 2),
(8, 10, 21, 1),
(15, 11, 3, 1),
(16, 11, 13, 1),
(17, 12, 14, 5),
(18, 13, 15, 4),
(19, 13, 16, 1),
(20, 13, 22, 2),
(21, 14, 23, 5),
(22, 14, 24, 3),
(23, 14, 25, 4),
(24, 14, 26, 2),
(25, 14, 27, 5),
(26, 14, 28, 4),
(27, 14, 29, 2),
(28, 16, 30, 5),
(29, 16, 31, 3),
(30, 16, 32, 4),
(35, 17, 1, 4),
(32, 17, 33, 2),
(33, 17, 34, 5),
(34, 17, 35, 5),
(36, 17, 36, 5),
(37, 17, 37, 2),
(31, 17, 41, 2),
(38, 18, 38, 4),
(39, 18, 39, 1),
(40, 18, 40, 2),
(41, 19, 41, 5),
(42, 21, 5, 5),
(43, 21, 42, 5),
(44, 21, 43, 5);

-- --------------------------------------------------------

--
-- Table structure for table `type`
--

CREATE TABLE IF NOT EXISTS `type` (
  `type_ID` int(11) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(100) NOT NULL,
  PRIMARY KEY (`type_ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `type`
--

INSERT INTO `type` (`type_ID`, `type_name`) VALUES
(1, 'recommendation'),
(2, 'watchlist'),
(3, 'watchedlist');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `user_ID` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
  `description` varchar(255) NOT NULL,
  PRIMARY KEY (`user_ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=27 ;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_ID`, `name`, `email`, `password`, `description`) VALUES
(1, 'Betina Costa', 'bmcosta@gmail.com', '1234', 'Oi, eu sou o Goku'),
(2, 'Thayse Klain', 'thayse@gmail.com', '1234', 'Chrommagia'),
(3, 'Yuri Lima', 'yuri@gmail.com', '1234', 'bla bla bla'),
(4, 'Fernanda Rodrigues', 'fernanda@gmail.com', '1234', 'blablabal'),
(5, 'Alice Cárcamo', 'alice@gmail.com', '1234', 'lyschan'),
(6, 'Ana Lídia', 'analidia@gmail.com', '12345', 'sou legal'),
(7, 'Beula Bucker', 'beula@gmail.com', '12345', 'Lorem ipsum dolor sit amet, consectetur adipiscing.'),
(8, 'Lindsy Nystrom', 'lindsay@gmail.com', '12345', 'Lorem ipsum dolor sit amet, consectetur adipiscing.'),
(9, 'Jolyn Leiter', 'jolyn@gmail.com', '12345', 'Lorem ipsum dolor sit amet, consectetur adipiscing.'),
(10, 'Bryant Mercer', 'bryant@gmail.com', '12345', 'Lorem ipsum dolor sit amet, consectetur adipiscing.'),
(11, 'Jone Heinz', 'jone@gmail.com', '12345', 'Lorem ipsum dolor sit amet, consectetur adipiscing.'),
(12, 'Rosalie Sanor', 'rosalie@gmail.com', '12345', 'Lorem ipsum dolor sit amet, consectetur adipiscing.'),
(13, 'Katharine Denniston', 'katharine@gmail.com', '12345', 'Lorem ipsum dolor sit amet, consectetur adipiscing.'),
(14, 'Rodger Magda', 'rodger@gmail.com', '12345', 'Lorem ipsum dolor sit amet, consectetur adipiscing.'),
(15, 'Julia Luthy', 'julia@gmail.com', '12345', 'Lorem ipsum dolor sit amet, consectetur adipiscing.'),
(16, 'Nolan Pidgeon', 'nolan@gmail.com', '12345', 'Lorem ipsum dolor sit amet, consectetur adipiscing.'),
(17, 'Sherise Ruggles', 'sherise@gmail.com', '12345', 'Lorem ipsum dolor sit amet, consectetur adipiscing.'),
(18, 'Susanne Pace', 'susanne@gmail.com', '12345', 'Lorem ipsum dolor sit amet, consectetur adipiscing.'),
(19, 'Carey Nathan', 'carey@gmail.com', '12345', 'Lorem ipsum dolor sit amet, consectetur adipiscing.'),
(20, 'Marcel Perez', 'marcel@gmail.com', '12345', 'Lorem ipsum dolor sit amet, consectetur adipiscing.'),
(21, 'Tuan Snelgrove', 'tuan@gmail.com', '12345', 'Lorem ipsum dolor sit amet, consectetur adipiscing.'),
(22, 'Mable Martina', 'mable@gmail.com', '12345', 'Lorem ipsum dolor sit amet, consectetur adipiscing.'),
(23, 'Robt Kempton', 'robt@gmail.com', '12345', 'Lorem ipsum dolor sit amet, consectetur adipiscing.'),
(24, 'Alison Bormann', 'alison@gmail.com', '12345', 'Lorem ipsum dolor sit amet, consectetur adipiscing.'),
(25, 'Elinore Nold', 'elinore@gmail.com', '12345', 'Lorem ipsum dolor sit amet, consectetur adipiscing.'),
(26, 'Ardelle Loredos', 'ardelle@gmail.com', '12345', 'Lorem ipsum dolor sit amet, consectetur adipiscing.');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `list`
--
ALTER TABLE `list`
  ADD CONSTRAINT `list_ibfk_1` FOREIGN KEY (`user_ID`) REFERENCES `user` (`user_ID`),
  ADD CONSTRAINT `list_ibfk_2` FOREIGN KEY (`type_ID`) REFERENCES `type` (`type_ID`);

--
-- Constraints for table `movie_list`
--
ALTER TABLE `movie_list`
  ADD CONSTRAINT `movie_list_ibfk_1` FOREIGN KEY (`movie_ID`) REFERENCES `movie` (`movie_ID`),
  ADD CONSTRAINT `movie_list_ibfk_2` FOREIGN KEY (`list_ID`) REFERENCES `list` (`list_ID`);

--
-- Constraints for table `profile`
--
ALTER TABLE `profile`
  ADD CONSTRAINT `profile_ibfk_1` FOREIGN KEY (`user_ID`) REFERENCES `user` (`user_ID`);

--
-- Constraints for table `profile_cast`
--
ALTER TABLE `profile_cast`
  ADD CONSTRAINT `profile_cast_ibfk_1` FOREIGN KEY (`profile_ID`) REFERENCES `profile` (`profile_ID`),
  ADD CONSTRAINT `profile_cast_ibfk_2` FOREIGN KEY (`cast_ID`) REFERENCES `cast` (`cast_ID`);

--
-- Constraints for table `profile_genre`
--
ALTER TABLE `profile_genre`
  ADD CONSTRAINT `profile_genre_ibfk_1` FOREIGN KEY (`profile_ID`) REFERENCES `profile` (`profile_ID`),
  ADD CONSTRAINT `profile_genre_ibfk_2` FOREIGN KEY (`genre_ID`) REFERENCES `genre` (`genre_ID`);

--
-- Constraints for table `rating`
--
ALTER TABLE `rating`
  ADD CONSTRAINT `rating_ibfk_1` FOREIGN KEY (`user_ID`) REFERENCES `user` (`user_ID`),
  ADD CONSTRAINT `rating_ibfk_2` FOREIGN KEY (`movie_ID`) REFERENCES `movie` (`movie_ID`),
  ADD CONSTRAINT `rating_ibfk_3` FOREIGN KEY (`rate_ID`) REFERENCES `rate` (`rate_ID`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;