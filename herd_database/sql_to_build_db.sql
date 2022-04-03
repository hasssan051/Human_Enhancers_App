-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema herd
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema herd
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `herd` DEFAULT CHARACTER SET utf8 ;
USE `herd` ;

-- -----------------------------------------------------
-- Table `herd`.`merged_peak`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `herd`.`merged_peak` (
  `mergedPeakId` INT NOT NULL,
  `chrom` VARCHAR(5) NOT NULL,
  `herdAccessionNum` VARCHAR(50) NOT NULL,
  `chromStart` INT UNSIGNED NOT NULL,
  `chromEnd` INT UNSIGNED NOT NULL,
  `Prefixes` VARCHAR(10) NOT NULL,
  `Location` VARCHAR(50) NULL,
  PRIMARY KEY (`mergedPeakId`),
  UNIQUE INDEX `herdAccessionNum_UNIQUE` (`herdAccessionNum` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `herd`.`vista`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `herd`.`vista` (
  `vistaId` INT NOT NULL,
  `chrom` VARCHAR(10) NOT NULL,
  `chromStart` INT UNSIGNED NOT NULL,
  `chromEnd` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`vistaId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `herd`.`mp_overlap_vista`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `herd`.`mp_overlap_vista` (
  `mergedPeakId` INT NOT NULL,
  `vistaId` INT NOT NULL,
  INDEX `fk_mpOverlapVista_mergedPeak_idx` (`mergedPeakId` ASC) VISIBLE,
  INDEX `fk_mpOverlapVista_vista1_idx` (`vistaId` ASC) VISIBLE,
  PRIMARY KEY (`mergedPeakId`, `vistaId`),
  CONSTRAINT `fk_mpOverlapVista_mergedPeak`
    FOREIGN KEY (`mergedPeakId`)
    REFERENCES `herd`.`merged_peak` (`mergedPeakId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_mpOverlapVista_vista1`
    FOREIGN KEY (`vistaId`)
    REFERENCES `herd`.`vista` (`vistaId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `herd`.`vista_in_mp`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `herd`.`vista_in_mp` (
  `mergedPeakId` INT NOT NULL,
  `vista_vistaId` INT NOT NULL,
  INDEX `fk_table2_mergedPeak1_idx` (`mergedPeakId` ASC) VISIBLE,
  INDEX `fk_table2_vista1_idx` (`vista_vistaId` ASC) VISIBLE,
  PRIMARY KEY (`mergedPeakId`, `vista_vistaId`),
  CONSTRAINT `fk_table2_mergedPeak1`
    FOREIGN KEY (`mergedPeakId`)
    REFERENCES `herd`.`merged_peak` (`mergedPeakId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_table2_vista1`
    FOREIGN KEY (`vista_vistaId`)
    REFERENCES `herd`.`vista` (`vistaId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `herd`.`erna`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `herd`.`erna` (
  `erna_id` INT NOT NULL,
  `chrom` VARCHAR(10) NULL,
  `chromStart` INT UNSIGNED NOT NULL,
  `chromEnd` INT UNSIGNED NOT NULL,
  `name` VARCHAR(100) NULL,
  PRIMARY KEY (`erna_id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `herd`.`mp_overlap_erna`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `herd`.`mp_overlap_erna` (
  `mergedPeakId` INT NOT NULL,
  `erna_erna_id` INT NOT NULL,
  INDEX `fk_mpOverlapErna_mergedPeak1_idx` (`mergedPeakId` ASC) VISIBLE,
  INDEX `fk_mpOverlapErna_erna1_idx` (`erna_erna_id` ASC) VISIBLE,
  PRIMARY KEY (`mergedPeakId`, `erna_erna_id`),
  CONSTRAINT `fk_mpOverlapErna_mergedPeak1`
    FOREIGN KEY (`mergedPeakId`)
    REFERENCES `herd`.`merged_peak` (`mergedPeakId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_mpOverlapErna_erna1`
    FOREIGN KEY (`erna_erna_id`)
    REFERENCES `herd`.`erna` (`erna_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `herd`.`erna_in_mp`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `herd`.`erna_in_mp` (
  `mergedPeakId` INT NOT NULL,
  `erna_id` INT NOT NULL,
  INDEX `fk_ernaInMp_mergedPeak1_idx` (`mergedPeakId` ASC) VISIBLE,
  INDEX `fk_ernaInMp_erna1_idx` (`erna_id` ASC) VISIBLE,
  PRIMARY KEY (`mergedPeakId`, `erna_id`),
  CONSTRAINT `fk_ernaInMp_mergedPeak1`
    FOREIGN KEY (`mergedPeakId`)
    REFERENCES `herd`.`merged_peak` (`mergedPeakId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ernaInMp_erna1`
    FOREIGN KEY (`erna_id`)
    REFERENCES `herd`.`erna` (`erna_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `herd`.`experiment_table`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `herd`.`experiment_table` (
  `experimentAccession` VARCHAR(50) NOT NULL,
  `system` VARCHAR(250) NOT NULL,
  `Organ` VARCHAR(250) NOT NULL,
  `tissue` VARCHAR(250) NOT NULL,
  `treated` VARCHAR(3) BINARY NULL,
  `diseased` VARCHAR(3) BINARY NULL,
  `biosampleSummary` VARCHAR(500) NULL,
  `Description` VARCHAR(500) NULL,
  `lifeStage` VARCHAR(45) NULL,
  `biosampleAge` INT UNSIGNED NULL,
  `narrowPeaksAccession` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`narrowPeaksAccession`),
  UNIQUE INDEX `narrowPeaksAccession_UNIQUE` (`narrowPeaksAccession` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `herd`.`mp_narrow_accession`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `herd`.`mp_narrow_accession` (
  `narrowPeaksAccession` VARCHAR(45) NOT NULL,
  `mergedPeak_mergedPeakId` INT NOT NULL,
  `chrom` VARCHAR(5) NOT NULL,
  INDEX `fk_mpNarrowAccession_experimentTable1_idx` (`narrowPeaksAccession` ASC) VISIBLE,
  INDEX `fk_mpNarrowAccession_mergedPeak1_idx` (`mergedPeak_mergedPeakId` ASC) VISIBLE,
  CONSTRAINT `fk_mpNarrowAccession_experimentTable1`
    FOREIGN KEY (`narrowPeaksAccession`)
    REFERENCES `herd`.`experiment_table` (`narrowPeaksAccession`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_mpNarrowAccession_mergedPeak1`
    FOREIGN KEY (`mergedPeak_mergedPeakId`)
    REFERENCES `herd`.`merged_peak` (`mergedPeakId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
