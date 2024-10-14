-- sql script that list all records from one table matching a field of another table

-- list matching records
SELECT id, name FROM cities 
WHERE states.name = 'California' AND states.id = cities.state_id 
ORDER BY cities.id; 
