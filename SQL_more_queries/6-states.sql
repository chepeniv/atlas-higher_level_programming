-- sql script that creates a database and table

-- create new database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- alternatively, i could've name-spaced `states` when creating the table: `hbtn_0d_usa.states`
USE hbtn_0d_usa;

-- create table
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
