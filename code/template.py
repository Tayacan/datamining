#!/usr/bin/python2

import sqlite3 as sql

con = sql.connect("DataminingAssignment2013.db")
cursor = con.cursor()

cursor.execute('PRAGMA table_info(Sunspots_Train_Y);')

cursor.close()
con.close()
