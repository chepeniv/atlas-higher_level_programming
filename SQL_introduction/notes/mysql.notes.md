# mysql.notes

### man pages
location : `/usr/local/share/man/`

run : `man mysql`


## basic commands
comments:
```sql
-- this is an sql comment
```

create database:
```sql
CREATE DATABASE database_name;
```

show databases:
```sql
SHOW DATABASES;
```

create table:
```sql
CREATE TABLE table_name;
```

create table with rows:
```sql
CREATE TABLE users(
	id INT PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	bio TEXT,
	country VARCHAR(2)
);
```

adding a single row-entry into table:
```sql
INSERT INTO users (email, bio, country)
VALUES (
	'jonh_doe@homepage.com',
	'hello, world!',
	'US'
);
```

adding multiple row-entries into a table:
```sql
INSERT INTO users (email, bio, country)
VALUES 
	('jonh_doe@homepage.com', 'hello, world!', 'US'),
	('maria_estrada@homepage.com', 'saludos!', 'MX'),
	('jean_pierre@homepage.com', 'bonjour, monsieur!', 'FR');
```

read entire table:
```sql
SELECT * FROM table_name;
```

read selected columns from table:
```sql
SELECT fieldA, fieldB, fieldC FROM table_name;
```

read only n entries from table:
```sql
SELECT * FROM table_name LIMIT n;
```

return entries in a desired order:
```sql
SELECT * FROM table_name ORDER BY fieldN ASC;
```

return only entries matching a given condition:
```sql
SELECT * FROM table_name WHERE fieldA = 'value';
```

return entries matching a set of chained condition:
```sql
SELECT * FROM table_name 
WHERE fieldA = 'value'
AND fieldB > N;
```

return entries filtered through a pattern:
```sql
SELECT * FROM table_name 
WHERE fieldA LIKE 'pattern';
```

## indeces

these are lookup tables for specific columns

these result in slower writes and more storage usage,
but the data will be retrieved much faster

creating an index:
```sql
CREATE INDEX filedA_index ON table_A(fieldA);
```
this will allow queries based on patterns to complete much faster

to create a one-to-many relationship from one table to another,
only link the rows of one table to the ids of another.
these are called foreign keys, of which there can be many
```sql
CREATE TABLE tableB (
	id INT AUTO_INCREMENT,	-- primary key
	name VARCHAR(255),
	owner_id INT NOT NULL,	-- foreign key
	-- these set the roles of the previous entries
	PRIMARY KEY (id),
	FOREIGN KEY (owner_id) REFERENCES tableA(id)
	-- these guarantee data integrity
);
```

relational queries using `JOIN`; joins read data from two 
different tables where values of columns can be matched,
typically primary keys on one against the foreign keys of 
another. there are four kinds of joins: inner, left, 
right, and outer. since right joins can be writen as left
joins, they are rarely seen. an outer join, sometimes refered
to as a full join, is basically a left join followed by a
right join
```sql
SELECT * FROM tableA
INNER JOIN tableB -- inner joins are the default
ON tableA.id = tableB.owner_id;

```

a union is similar to a join, but instead it stacks the rows
rather than appending them. union by itself ignores duplicate vales
```sql
SELECT fieldN FROM tableA
UNION -- ALL, if used will not ignore duplicates
SELECT fieldM FROM tableB;
```

a less common join is the cross-join wherein based on given 
fields, all possible side-by-side combinations are displayed
```sql
SELECT
	tableA.fieldN,
	tableB.fieldM
FROM tableA
CROSS JOIN tableB;
```

```sql
USE database_name;
```

```sql
DESCRIBE table_name;
```

modify the fields in an already existing table:
```sql
ALTER TABLE name ADD new_field type_name;
```

conflicting names in sql are namespaced by their table name.
names of fields can be cast to different names with the `AS`
operator:

finally, `DROP` statements deletes various types of elements (databases, tables, etc)

