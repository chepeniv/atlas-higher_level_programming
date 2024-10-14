-- sql script that list all records from one table matching a field of another table

-- list matching records
SELECT cities.id, cities.name, states.name FROM cities 
-- both LEFT JOIN and INNER JOIN seem to work the same here
JOIN states ON cities.state_id = states.id
ORDER BY cities.id; 
