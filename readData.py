#!/usr/bin/python2

"""
DBDM Exam 2013 - sqlite example
"""

import sqlite3 as sql

__author__='Schulz, Albert'
__version__='1.0'
__modified__='20130303'


# open connection to database, create cursor
sqlserver = sql.connect("DataminingAssignment2013.db")
cursor = sqlserver.cursor()

# execute sql-statement
tables = cursor.execute('select name from sqlite_master').fetchall()

for row in tables:
  print row[0]

# close cursor, connection to database
cursor.close()
sqlserver.close()
