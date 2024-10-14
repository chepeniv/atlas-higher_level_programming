# mysql_users_and_permissions

# creating a user
```sql
CREATE USER 'username'@'host' IDENTIFIED WITH authentication_plugin BY 'password';
```
if `username` is only accessed locally from then sot `host` to `localhost`

for the `authentication_plugin` argument, setting it to `auth_socket` ought to be enough.
alternatively the `IDENTIFIED WITH ...` portion of the statement may be leftout completely.
mysql recommends leaving the default `caching_sha2_password`

if the authentication plugin needs to be changed after the fact:
```sql
ALTER USER 'sammy'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
```

# granting permissions

```sql 
GRANT PRIVILEGE ON database.table TO 'username'@'host';
```
multiple privileges may be granted in a single statement by comma-separating each.
setting privaleges to all databases and tables may be granted with `*`.
it is recomended that only _needed_ privaleges be granted.

example: 
```sql
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'sammy'@'localhost' WITH GRANT OPTION;
```
the `WITH GRANT OPTION` clause allows the user to grant any permission it posseses to other users

to grant _all_ permissions use:
```sql
GRANT ALL PRIVILEGES ON *.* TO 'sammy'@'localhost' WITH GRANT OPTION;
```

immediately after `CREATE USER` and `GRANT` statements in order to reload the grant tables and to ensure that the new privilages are active, run:
```sql
FLUSH PRIVILEGES;
```
this isn't really always necessary. but it doesn't hurt

inorder to remove permissions from a user run:
```sql
REVOKE type_of_permission ON database_name.table_name FROM 'username'@'host';
```

to display a given users permissions: 
```sql
SHOW GRANTS FOR 'username'@'host';
```

to remove a user:
```sql
DROP USER 'username'@'localhost';
```

to login as a given user:
```bash
mysql -u sammy -p
```
the `-p` flag will prompt you for the user's password 

