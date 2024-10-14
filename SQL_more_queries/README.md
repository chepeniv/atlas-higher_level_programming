# SQL More Queries

![sql joins cheatsheet](./resources/sql_joins.png)

## Resources
- [youtube: mysql tutorial](https://www.youtube.com/watch?v=yPu6qV5byu4)
- [creating users and granting permisions](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
- [mysql GRANT](https://www.mysqltutorial.org/mysql-administration/mysql-grant/)
- [mysql constraints](https://zetcode.com/mysql/constraints/)
- [types of sql JOINS](https://tableplus.com/blog/2018/09/a-beginners-guide-to-seven-types-of-sql-joins.html)
- [database design and modeling](https://www.guru99.com/database-design.html)
- [database normalization](https://www.guru99.com/database-normalization.html)
- [entity relationship modeling](https://www.guru99.com/er-modeling.html)
- [mysql styleguide](https://www.sqlstyle.guide/)

## Goals
- how to create a new mysql user
- how to manage user privalages to both databases and tables
- what is `PRIMARY KEY` and a `FOREIGN KEY`
- how to use the `NOT NULL` and `UNIQUE` constraints
- how to retrieve data from multiple tables with one request
- what are subqueries
- what are `JOIN` and `UNION`, and what do they do

## Requirements
- task will be tested on `MySQL 8.0`
- all queries should be preceded by a comment
- all files should begin with a descriptive comment
- all sql keywords should be in uppercase

## Importing an SQL dump 
create database :
```bash
echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
```
import data into new database :
```bash
curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
```
check data in database:
```bash
echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
```
