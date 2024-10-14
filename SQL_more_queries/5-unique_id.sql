-- sql script that creates a new table with the UNIQUE constraint on the id column

-- create table
CREATE TABLE IF NOT EXISTS unique_id (
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256)
);
