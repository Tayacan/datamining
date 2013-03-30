#!/usr/bin/env python

import sqlite3 as sql

# Fetch data
con = sql.connect("DataminingAssignment2013.db")
cursor = con.cursor()

train_y_raw = cursor.execute("select y from Sunspots_Train_Y")

# Turn the one-element-tuple-list into a list of numbers
train_y = map(lambda x:x[0],train_y_raw)

cursor.close()
con.close()

# Computation

# Compute the mean
mean = sum(train_y) / float(len(train_y))
# Compute the biased sample variance
bsv = sum(map(lambda y:pow(y-mean,2),train_y)) / float(len(train_y))

print mean
print bsv
