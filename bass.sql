/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - crime_scene_detection
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`crime_scene_detection` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `crime_scene_detection`;

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_id` int(11) DEFAULT NULL,
  `to_id` int(11) DEFAULT NULL,
  `msg` varchar(200) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  `time` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`chat_id`,`from_id`,`to_id`,`msg`,`date`,`time`) values (1,8,4,'hai police','2020-03-14','11:26:02'),(2,8,5,'hai police','2020-03-14','11:31:35'),(3,5,8,'wq','2020-03-14','11:32:53');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `complaint` varchar(300) DEFAULT NULL,
  `complaint_date` date DEFAULT NULL,
  `u_id` varchar(20) DEFAULT NULL,
  `reply` varchar(300) DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`complaint`,`complaint_date`,`u_id`,`reply`,`status`) values (1,'complaint','2020-03-14','8','abhjba','reply_sent');

/*Table structure for table `crime` */

DROP TABLE IF EXISTS `crime`;

CREATE TABLE `crime` (
  `c_id` int(11) NOT NULL AUTO_INCREMENT,
  `crime_name` varchar(30) DEFAULT NULL,
  `details` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`c_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `crime` */

insert  into `crime`(`c_id`,`crime_name`,`details`) values (1,' crime','details'),(2,' murder','bcuien');

/*Table structure for table `crime_scene` */

DROP TABLE IF EXISTS `crime_scene`;

CREATE TABLE `crime_scene` (
  `c_id` int(11) NOT NULL AUTO_INCREMENT,
  `cr_id` int(11) DEFAULT NULL,
  `scene_no` int(11) DEFAULT NULL,
  `scene_details` varchar(300) DEFAULT NULL,
  `scene_date` date DEFAULT NULL,
  `scene_time` time DEFAULT NULL,
  `scene_file` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`c_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `crime_scene` */

insert  into `crime_scene`(`c_id`,`cr_id`,`scene_no`,`scene_details`,`scene_date`,`scene_time`,`scene_file`) values (1,1,1,'delts','0000-00-00','00:00:02','1.jpg');

/*Table structure for table `criminal` */

DROP TABLE IF EXISTS `criminal`;

CREATE TABLE `criminal` (
  `cr_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `blood_group` varchar(20) DEFAULT NULL,
  `identification_marks` varchar(50) DEFAULT NULL,
  `house_no` varchar(20) DEFAULT NULL,
  `street` varchar(20) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `post` varchar(20) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `district` varchar(20) DEFAULT NULL,
  `father` varchar(20) DEFAULT NULL,
  `mother` varchar(20) DEFAULT NULL,
  `crime_id` varchar(20) DEFAULT NULL,
  `photo` varchar(300) DEFAULT NULL,
  `pid` int(11) DEFAULT NULL,
  PRIMARY KEY (`cr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `criminal` */

insert  into `criminal`(`cr_id`,`name`,`gender`,`dob`,`blood_group`,`identification_marks`,`house_no`,`street`,`place`,`post`,`pin`,`district`,`father`,`mother`,`crime_id`,`photo`,`pid`) values (2,'abay','male','2020-03-27','a+ve','black mole on face','728','bsb','kozhikode','post',677777,'kannur','siv','mother','1','20200314-103508na1.jpg',6),(3,'aadith','male','2020-03-23','b+ve','black mole on left elbow','2929','41street','payambra','post',673571,'kozhikod','ravi','sheeba','2','20200314-103631q3.jpg',6);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`type`) values (1,'a','a','admin'),(3,'ngo@gmail.com','6428','police'),(4,'','6764','police'),(5,'aa@gmail.com','a','police'),(6,'p@g.com','65','police'),(7,'aaaaa@gmail.com','6112','police'),(8,'aadithlal6@gmail.com','111111','user');

/*Table structure for table `lookout` */

DROP TABLE IF EXISTS `lookout`;

CREATE TABLE `lookout` (
  `lookout_id` int(11) NOT NULL AUTO_INCREMENT,
  `cr_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`lookout_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `lookout` */

insert  into `lookout`(`lookout_id`,`cr_id`) values (1,3);

/*Table structure for table `missingperson` */

DROP TABLE IF EXISTS `missingperson`;

CREATE TABLE `missingperson` (
  `missing_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `photo` varchar(300) DEFAULT NULL,
  `house_no` varchar(20) DEFAULT NULL,
  `street` varchar(20) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  `district` varchar(20) DEFAULT NULL,
  `state` varchar(20) DEFAULT NULL,
  `height` varchar(20) DEFAULT NULL,
  `weight` varchar(20) DEFAULT NULL,
  `skin_tone` varchar(20) DEFAULT NULL,
  `identification_marks` varchar(50) DEFAULT NULL,
  `missing_place` varchar(20) DEFAULT NULL,
  `last_seen` varchar(20) DEFAULT NULL,
  `dress` varchar(20) DEFAULT NULL,
  `contact` varchar(20) DEFAULT NULL,
  `pid` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`missing_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `missingperson` */

insert  into `missingperson`(`missing_id`,`name`,`gender`,`dob`,`photo`,`house_no`,`street`,`city`,`district`,`state`,`height`,`weight`,`skin_tone`,`identification_marks`,`missing_place`,`last_seen`,`dress`,`contact`,`pid`) values (1,'aviansh','female','2020-03-18','20200314-104516a1.jpg','66','street','city','distrcit','srate','170','90','light brown','black mole on hand','kozhikode','calicut','jeabs and shirt','9999999999','6');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `subject` varchar(50) DEFAULT NULL,
  `content` varchar(200) DEFAULT NULL,
  `notification_date` date DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`notification_id`,`subject`,`content`,`notification_date`,`type`) values (2,'police notification','police notification','2019-12-12','Police'),(3,'user notification','user notification','2019-12-12','User');

/*Table structure for table `object` */

DROP TABLE IF EXISTS `object`;

CREATE TABLE `object` (
  `obj_id` int(11) NOT NULL AUTO_INCREMENT,
  `obj_name` varchar(20) DEFAULT NULL,
  `obj_images` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`obj_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `object` */

/*Table structure for table `police_station` */

DROP TABLE IF EXISTS `police_station`;

CREATE TABLE `police_station` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `post` varchar(20) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `city` varchar(30) DEFAULT NULL,
  `district` varchar(20) DEFAULT NULL,
  `photo` varchar(300) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `fax` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `police_station` */

insert  into `police_station`(`p_id`,`name`,`place`,`post`,`pin`,`city`,`district`,`photo`,`email`,`phone`,`fax`) values (4,'police','place','post',666666,'kozhikode','calicut','20200314-102907bullet-electra-blue.jpg','p@g.com','9999999999','123'),(5,'avinash','odumbra','odumbra post',677382,'kozhikode','kozhikode','20200314-103930b4.png','aaaaa@gmail.com','9999999999','1616');

/*Table structure for table `report` */

DROP TABLE IF EXISTS `report`;

CREATE TABLE `report` (
  `report_id` int(11) NOT NULL AUTO_INCREMENT,
  `manmissing_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `latitude` varchar(20) DEFAULT NULL,
  `longitude` varchar(20) DEFAULT NULL,
  `place` varchar(30) DEFAULT NULL,
  `information` varchar(200) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`report_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `report` */

/*Table structure for table `scene_object` */

DROP TABLE IF EXISTS `scene_object`;

CREATE TABLE `scene_object` (
  `scene_obj_id` int(11) NOT NULL AUTO_INCREMENT,
  `cr_id` int(11) DEFAULT NULL,
  `scn_id` int(11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `details` varchar(200) DEFAULT NULL,
  `st_pos_x` varchar(50) DEFAULT NULL,
  `st_pos_y` varchar(50) DEFAULT NULL,
  `end_pos_x` varchar(50) DEFAULT NULL,
  `end_pos_y` varchar(50) DEFAULT NULL,
  `path` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`scene_obj_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `scene_object` */

insert  into `scene_object`(`scene_obj_id`,`cr_id`,`scn_id`,`name`,`details`,`st_pos_x`,`st_pos_y`,`end_pos_x`,`end_pos_y`,`path`) values (1,1,1,'hhd','detlis','527',' 577','634',' 704','1#1#.jpg'),(2,1,1,'wa','detlis','216',' 68','276',' 164','1#1#hhd.jpg');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `place` varchar(30) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `login_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`name`,`gender`,`place`,`pin`,`email`,`phone`,`login_id`) values (1,'user','male','place',666666,'aadithlal6@gmail.com','9495189217',8);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
