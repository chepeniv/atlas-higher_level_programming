-- sql script that creates a database and table

-- create new database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- create table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL,
	state_id INT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (state_id) REFERENCES states(id)
);
