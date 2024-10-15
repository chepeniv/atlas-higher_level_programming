# Python - Object Relational Mapping

the purpose of an ORM is to abstract storage and usage of sql databases.
this will permit us to have storage-independent python code.

## Resources
- [youtube: intro to sqlalchemy](https://www.youtube.com/watch?v=woKYyhLCcnU)
- [youtube playlist: flask-sqlalchemy](https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW)

- [sqlalchemy tutorial](https://overiq.com/sqlalchemy-101/)
- [python sqlalchemy orm tutorial](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
- [common sqlalchemy stumbling blocks](https://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html)
- [python sqlalchemy cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)

- [object relational mappers in python](https://www.fullstackpython.com/object-relational-mappers-orms.html)
- [github: mysqlclient](https://github.com/PyMySQL/mysqlclient)
- [MySQLdb documentation](https://mysqlclient.readthedocs.io/)
- [Python MySQL documentation](https://www.mikusa.com/python-mysql-docs/index.html)
- [SQLAlchemy documentation](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)

## Goals
- how to connect a mysql db in a python script
- how to `SELECT` rows from a python script
- how to `INSERT` rows from a python script
- what is an ORM
- how to map python classes to mysql tables

## Requirements
- files will be executed with `MySQLdb` and `SQLAlchemy`
- document all modules, classes, and functions
- `execute` with `SQLAlchemy` is **NOT** allowed

## Reference
### installing `MySQLdb`
```sh
sudo apt-get install python3-dev
sudo apt-get install libmysqlclient-dev
sudo apt-get install zlib1g-dev
sudo pip3 install mysqlclient
...
python3
>>> import MySQLdb
```
### installing `SQLAlchemy`
```sh
sudo pip3 install SQLAlchemy
...
python3
>>> import sqlalchemy
```
