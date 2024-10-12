-- sql script that list all matching conditions

-- count the number of matching values and group
SELECT score, name FROM second_table 
	WHERE name IS NOT NULL 
	ORDER BY score DESC;
