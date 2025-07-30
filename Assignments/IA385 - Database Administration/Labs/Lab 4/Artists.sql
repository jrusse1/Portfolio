--------------------------------------------------------
--  File created - Sunday-February-28-2021   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Table ARTISTS
--------------------------------------------------------

  CREATE TABLE "SYSTEM"."ARTISTS" 
   (	"ID" NUMBER(*,0), 
	"ARTIST" VARCHAR2(20 BYTE)
   ) PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "SYSTEM" ;
REM INSERTING into SYSTEM.ARTISTS
SET DEFINE OFF;
Insert into SYSTEM.ARTISTS (ID,ARTIST) values (1,'Michael Jackson');
Insert into SYSTEM.ARTISTS (ID,ARTIST) values (2,'Madonna');
Insert into SYSTEM.ARTISTS (ID,ARTIST) values (3,'Billy Joel');
Insert into SYSTEM.ARTISTS (ID,ARTIST) values (4,'Phil Collins');
Insert into SYSTEM.ARTISTS (ID,ARTIST) values (5,'Fleetwood Mac');
