#!/usr/bin/python2

import sqlite3 as sql
import numpy as np

class NearestNeighbour:
    def __init__(self,train):
        """train is a dict of { x : y } (training data), where x is a list"""
        self.train = train

    def _dist(self,a,b):
        """Return the euclidian distance between two vectors.

        The points should be np arrays."""
        return np.linalg.norm(np.array(a) - np.array(b))

    def _loss(self,y,y1):
        if y == y1:
            return 0
        return 1

    def _nearest_label(self,x):
        """Find the label of the point closest to x."""
        nearest = self.train.keys()[0]
        for x1 in self.train.keys():
            if self._dist(x,x1) < self._dist(x,nearest):
                nearest = x1

        return self.train[nearest]

    def test(self,test):
        """test is a dict of { x : y } (test data + answers), where is a list"""
        return sum(self._loss(self._nearest_label(x),real_y) for x,real_y in test.items())

# Connect to the database
con = sql.connect("DataminingAssignment2013.db")
cursor = con.cursor()

# Fetch data
train_x = cursor.execute('select * from Seeds_Train_X;').fetchall()
test_x = cursor.execute('select * from Seeds_Test_X;').fetchall()

# Build dictionaries
train_d = {}
for row in train_x:
    xid = row[0]
    label = cursor.execute('select y from Seeds_Train_Y where id=%d' % xid).fetchone()[0]
    train_d[row[1:]] = label

test_d = {}
for row in test_x:
    xid = row[0]
    label = cursor.execute('select y from Seeds_Test_Y where id=%d' % xid).fetchone()[0]
    test_d[row[1:]] = label

# Close connection
cursor.close()
con.close()

# Calculate stuff
nn = NearestNeighbour(train_d)
print "Total loss: %d" % nn.test(test_d)
