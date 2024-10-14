-- sql script that creates a new mysql database and user if they doesn't exist followed by explicit permissions

-- create new user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- create new database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- specify new user permissions
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';
GRANT SELECT ON hbt_0d_2.* TO 'user_0d_2'@'localhost';
