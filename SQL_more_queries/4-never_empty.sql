-- sql script that creates a new table with the DEFAULT constraint

-- create table
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
);
