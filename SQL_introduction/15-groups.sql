-- sql script that counts the number of equivalent values in given field
-- in all records

-- count the number of matching values and group
SELECT score, COUNT(score) AS 'number' FROM second_table 
GROUP BY score ORDER BY score DESC;
