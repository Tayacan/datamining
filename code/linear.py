#!/usr/bin/python2

import sqlite3 as sql
import numpy as np
import matplotlib.pyplot as mpl

con = sql.connect("DataminingAssignment2013.db")
cursor = con.cursor()

# Build the model
y_raw = cursor.execute('select y from Sunspots_Train_Y').fetchall()
ys = map(lambda y: y[0],y_raw)

x_raw = cursor.execute('select x1,x2,x3,x4 from Sunspots_Train_X').fetchall()
x_prep = map(lambda x: list(x) + [1],x_raw)

y_matrix = np.matrix(ys).transpose()
x_matrix = np.matrix(x_prep)

w = (x_matrix.transpose() * x_matrix).getI() * x_matrix.transpose() * y_matrix

b = w.tolist()[-1][0]
w = np.matrix(w.flatten().tolist()[0][:-1])

# Test the model
x_train_all = cursor.execute('select * from Sunspots_Train_X').fetchall()
x_test = cursor.execute('select * from Sunspots_Test_X').fetchall()
y_test = cursor.execute('select * from Sunspots_Test_Y').fetchall()

def f(x):
    xm = np.matrix(x)
    return (xm * w.transpose() + b).tolist()[0][0]

def g(row,table='Sunspots_Test_Y'):
    xid,x = row[0],row[1:]
    yval = cursor.execute('select Y from %s where id=%d' % (table,xid)).fetchone()[0]
    return (yval - f(x)) ** 2

print sum(map(lambda x: g(x,'Sunspots_Train_Y'),x_train_all))
print sum(map(g,x_test))

x_test = map(lambda x: x[1:], x_test)
y_test = map(lambda x: x[1:], y_test)
test = map(f,x_test)
mpl.plot(test,label='prediction')
mpl.plot(y_test,label='actual')
mpl.legend()
mpl.show()

cursor.close()
con.close()
