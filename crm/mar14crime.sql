/*
SQLyog Ultimate v11.32 (64 bit)
MySQL - 5.6.15 : Database - crime_scene_detection
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`chat_id`,`from_id`,`to_id`,`msg`,`date`,`time`) values (1,2,4,'mlkbrt','2020-03-13','13:21:17'),(2,2,4,'no','2020-03-13','13:23:23'),(3,2,4,'hai','2020-03-13','14:18:09'),(4,2,4,'hai','2020-03-13','16:11:32'),(5,2,4,' kj','2020-03-13','16:12:33'),(6,2,4,' kj','2020-03-13','16:14:27'),(7,2,4,'hjkk','2020-03-13','16:14:33'),(8,2,4,'hjkk','2020-03-13','16:15:54'),(9,2,4,'mmmm','2020-03-13','16:16:02'),(10,2,4,'mmmm','2020-03-13','16:16:43'),(11,2,4,'mmmm','2020-03-13','16:16:55');

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`complaint`,`complaint_date`,`u_id`,`reply`,`status`) values (1,'complaint','2020-03-13','1','nvuinvioer','reply_sent'),(2,'gssh\n','2020-03-13','4','','pending');

/*Table structure for table `crime` */

DROP TABLE IF EXISTS `crime`;

CREATE TABLE `crime` (
  `c_id` int(11) NOT NULL AUTO_INCREMENT,
  `crime_name` varchar(30) DEFAULT NULL,
  `details` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`c_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `crime` */

insert  into `crime`(`c_id`,`crime_name`,`details`) values (1,'murder','ertyuioijg'),(2,'robbery','nlnlk');

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `crime_scene` */

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `criminal` */

insert  into `criminal`(`cr_id`,`name`,`gender`,`dob`,`blood_group`,`identification_marks`,`house_no`,`street`,`place`,`post`,`pin`,`district`,`father`,`mother`,`crime_id`,`photo`,`pid`) values (1,'avinash','male','2020-03-18','vgjhbk','ghjkl','567','fghj','gj','vhj',6789,'kannur','vbunil','jhbnkl','1','20200313-131020Bluescreen_of_Death_HD_Wide_Wallpaper_for_4K_UHD_W.jpg',2);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`type`) values (1,'a','a','admin'),(2,'police@gmail.com','1189','police'),(4,'u','123456','user');

/*Table structure for table `lookout` */

DROP TABLE IF EXISTS `lookout`;

CREATE TABLE `lookout` (
  `lookout_id` int(11) NOT NULL AUTO_INCREMENT,
  `cr_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`lookout_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `lookout` */

insert  into `lookout`(`lookout_id`,`cr_id`) values (1,1);

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

insert  into `missingperson`(`missing_id`,`name`,`gender`,`dob`,`photo`,`house_no`,`street`,`city`,`district`,`state`,`height`,`weight`,`skin_tone`,`identification_marks`,`missing_place`,`last_seen`,`dress`,`contact`,`pid`) values (1,'aadhith edited','male','2020-03-03','20200313-114119Cristiano_Ronaldo_HD_Wide_Wallpaper_for_4K_UHD_Wid_-_Copy.jpg','201','street','city','distrcit','state','180','90','light brown','black mole under elbow','kozhikode','kozhikode','jean','123456789',NULL);

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

insert  into `notification`(`notification_id`,`subject`,`content`,`notification_date`,`type`) values (3,'trcvygh','rxctfv','2020-03-13','user');

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `police_station` */

insert  into `police_station`(`p_id`,`name`,`place`,`post`,`pin`,`city`,`district`,`photo`,`email`,`phone`,`fax`) values (1,'police edited','place','post',666666,'city','distrcit','20200313-112518BarcelonaFC_HD_Wide_Wallpaper_for_4K_UHD_Widescree_-_Copy.jpg','police@gmail.com','9999999999','1111111');

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `scene_object` */

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

insert  into `user`(`user_id`,`name`,`gender`,`place`,`pin`,`email`,`phone`,`login_id`) values (1,'user','male','place',12345,'user@g.com','123456789',4);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
