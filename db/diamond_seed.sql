
USE `diamond` ;

--
-- Data for table `categories`
--
INSERT INTO `categories` 
(`category`, `description`)
  VALUES 
('女式皮带', NULL),
('男式皮带', NULL),
('男款双肩包', NULL),
('男款商务公文包', NULL),
('男式单肩包/斜挎包', NULL),
('男款钥匙包', NULL),
('男款手拿包', NULL),
('男款钱包', NULL),
('男款驾证包', NULL),
('男款卡包/名片包', NULL),
('女款手拿包', NULL),
('女款钱包', NULL),
('女式单肩/斜挎包', NULL),
('女款手提包', NULL),
('女款钥匙包', NULL),
('旅行包', NULL),
('女款双肩包', NULL);


--
-- Data for table `gender`
--
INSERT INTO `gender` 
(`sex`, `description`)
  VALUES 
('男士','男性'),
('女士','女性'),
('中性','男女皆宜');


--
-- Data for table `material`
--
INSERT INTO `material`
(`material`, `description`)
  VALUES
('头层牛皮（革）','真皮、头层牛皮'),
('二层牛皮（革）','二层皮、剖层皮');


--
-- Data for table `sale_channels`
--
INSERT INTO `sale_channels` 
(`channel_name`, `description`)
  VALUES 
('POP平台','天猫、京东、淘宝、亚马逊、融易购'),
('京东自营','京东采销'),
('王府井商城','王府井网上商城'),
('唯品会','唯品会自营'),
('分销商','统一分销商售价');


--
-- Data for table `supplier`
--
INSERT INTO `supplier`
(`supplier`, `description`)
  VALUES
('星莲皮具厂','星莲'),
('东成皮具厂','东成');

