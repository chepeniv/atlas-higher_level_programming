-- sql script that creates a new table if it doesn't exist

-- create table
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
);
