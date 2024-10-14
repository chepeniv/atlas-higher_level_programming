-- sql script that list all records from one table matching a field of another table

-- list matching records
SELECT id, name FROM cities 
WHERE state_id IN
	(SELECT id FROM states 
		WHERE states.name = 'California')
ORDER BY id; 
