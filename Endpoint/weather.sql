CREATE TABLE `weather`.`reading` (
  `readingID` INT NOT NULL AUTO_INCREMENT COMMENT '',
  `Temp1` DECIMAL(20,10) NULL COMMENT '',
  `Temp2` DECIMAL(20,10) NULL COMMENT '',
  `TempSensorAvg` DECIMAL(20,10) NULL COMMENT '',
  `Humidity` DECIMAL(20,10) NULL COMMENT '',
  `Pressure` DECIMAL(20,10) NULL COMMENT '',
  `SeaLevelPressure` DECIMAL(20,10) NULL COMMENT '',
  `TimeStamp` VARCHAR(45) NULL COMMENT '',
  PRIMARY KEY (`readingID`)  COMMENT '');
