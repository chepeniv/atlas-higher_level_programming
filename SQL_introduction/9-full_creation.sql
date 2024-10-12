-- sql script that creates table with initial records

-- create table 
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(255),
	score INT
);

-- initialize data
INSERT INTO second_table VALUES 
	(1, 'John', 10),
	(2, 'Alex', 3),
	(3, 'Bob', 14),
	(4, 'George', 8);
