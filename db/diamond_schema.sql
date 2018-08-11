-- 05/04/18 12:10:00
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema diamond
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `diamond` ;
CREATE SCHEMA IF NOT EXISTS `diamond` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `diamond` ;

-- -----------------------------------------------------
-- Table `diamond`.`categories`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `diamond`.`categories` ;

CREATE TABLE IF NOT EXISTS `diamond`.`categories` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `category` VARCHAR(12) NOT NULL,
  `description` VARCHAR(128) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `diamond`.`gender`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `diamond`.`gender` ;

CREATE TABLE IF NOT EXISTS `diamond`.`gender` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `sex` VARCHAR(6) NOT NULL,
  `description` VARCHAR(24) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `diamond`.`material`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `diamond`.`material` ;

CREATE TABLE IF NOT EXISTS `diamond`.`material` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `material` VARCHAR(8) NOT NULL,
  `description` VARCHAR(24) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `diamond`.`supplier`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `diamond`.`supplier` ;

CREATE TABLE IF NOT EXISTS `diamond`.`supplier` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `supplier` VARCHAR(12) NOT NULL,
  `description` VARCHAR(36) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `diamond`.`factory`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `diamond`.`factory` ;

CREATE TABLE IF NOT EXISTS `diamond`.`factory` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `no` VARCHAR(12) NOT NULL UNIQUE,
  `name` VARCHAR(12) NULL,
  `description` VARCHAR(36) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `diamond`.`products`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `diamond`.`products` ;

CREATE TABLE IF NOT EXISTS `diamond`.`products` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `style_no` VARCHAR(10) NOT NULL,
  `item_no` VARCHAR(10) NOT NULL,
  `barcode` VARCHAR(32) NOT NULL,
  `brand` VARCHAR(45) NULL,
  `product_abbreviation` VARCHAR(45) NULL,
  `category_id` INT UNSIGNED NOT NULL,
  `gender_id` INT UNSIGNED NOT NULL,
  `color` VARCHAR(8) NOT NULL,
  `main_material_id` INT UNSIGNED NOT NULL,
  `vice_material_id` INT UNSIGNED,
  `interior_material_id` INT UNSIGNED,
  `exterior_structure` VARCHAR(45) NULL,
  `interior_structure` VARCHAR(45) NULL,
  `open_mode` VARCHAR(12) NULL,
  `length` DECIMAL(4,2) NULL,
  `width` DECIMAL(4,2) NULL,
  `height` DECIMAL(4,2) NULL,
  `weight` DECIMAL(6,2) NULL,
  `supplier_id` INT UNSIGNED NULL,
  `factory_price` DECIMAL(8,2) NULL,
  `cost_price` DECIMAL(8,2) NULL,
  `tag_price` DECIMAL(8,2) NULL,
  `retail_price` DECIMAL(8,2) NULL,
  `original_item_no` VARCHAR(10) NULL,
  `image` VARCHAR(45) NULL,
  `feature` VARCHAR(45) NULL,
  `comment` TEXT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  UNIQUE INDEX `item_no_UNIQUE` (`item_no` ASC),
  UNIQUE INDEX `barcode_UNIQUE` (`barcode` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `diamond`.`sale_channels`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `diamond`.`sale_channels` ;

CREATE TABLE IF NOT EXISTS `diamond`.`sale_channels` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `channel_name` VARCHAR(8) NOT NULL,
  `description` VARCHAR(128) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `diamond`.`prices`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `diamond`.`prices` ;

CREATE TABLE IF NOT EXISTS `diamond`.`prices` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `product_id` INT UNSIGNED NOT NULL,
  `sale_channel_id` INT UNSIGNED NOT NULL,
  `price` DECIMAL(8,2) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  INDEX `fk_prices_products_idx` (`product_id` ASC),
  INDEX `fk_prices_sale_channels_idx` (`sale_channel_id` ASC),
  CONSTRAINT `fk_prices_products`
    FOREIGN KEY (`product_id`)
    REFERENCES `diamond`.`products` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_prices_sale_channels`
    FOREIGN KEY (`sale_channel_id`)
    REFERENCES `diamond`.`sale_channels` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
