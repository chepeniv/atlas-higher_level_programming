-- sql script that list all records from one table matching a field of another table

-- list matching records
SELECT cities.id, cities.name, states.name FROM cities 
LEFT JOIN states ON cities.state_id = states.id
ORDER BY cities.id; 
