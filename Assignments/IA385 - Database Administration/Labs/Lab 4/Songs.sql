--------------------------------------------------------
--  File created - Sunday-February-28-2021   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Table SONGS
--------------------------------------------------------

  CREATE TABLE "SYSTEM"."SONGS" 
   (	"ID" NUMBER(*,0), 
	"TITLE" VARCHAR2(20 BYTE), 
	"ARTIST" NUMBER(*,0)
   ) PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "SYSTEM" ;
REM INSERTING into SYSTEM.SONGS
SET DEFINE OFF;
Insert into SYSTEM.SONGS (ID,TITLE,ARTIST) values (1,'"Thriller"
',1);
Insert into SYSTEM.SONGS (ID,TITLE,ARTIST) values (2,'"True Blue"',2);
Insert into SYSTEM.SONGS (ID,TITLE,ARTIST) values (3,'"Landslide"',5);
Insert into SYSTEM.SONGS (ID,TITLE,ARTIST) values (4,'"Beat It"',1);
Insert into SYSTEM.SONGS (ID,TITLE,ARTIST) values (5,'"Sussudio"',4);
Insert into SYSTEM.SONGS (ID,TITLE,ARTIST) values (6,'"Uptown Girl"',3);
