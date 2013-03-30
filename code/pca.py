#!/usr/bin/python2

import sqlite3 as sql
import numpy as np
import matplotlib.pyplot as mpl

con = sql.connect("DataminingAssignment2013.db")
cursor = con.cursor()

data = cursor.execute('select x1,x2,x3,x4,x5,x6,x7 from Seeds_Train_X').fetchall()

mean = sum(map(lambda x:np.array(x,ndmin=2),data)) / len(data)
ecm = sum((x-mean) * (x-mean).transpose() for x in data)/len(data)
w,v = np.linalg.eig(ecm)

a = []
for i in range(len(w)):
    a.append((w[i],v[:,i]))

s = sorted(a,key=lambda x: x[0],reverse=True)
print map(lambda x:x[0],s)

U_transposed = np.matrix(map(lambda x: x[1],s[:2]))
print U_transposed.transpose()

colors = [[(1,0,0)],
          [(0,1,0)],
          [(0,0,1)]]
colors = 'r','b','g'
for i in range(3):
    d = cursor.execute('select x1,x2,x3,x4,x5,x6,x7 from Seeds_Train_X natural join Seeds_Train_Y where y=%d' % i).fetchall()
    z = map(lambda x: (U_transposed * (np.matrix(x)-mean).transpose()).flatten().tolist()[0],d)
    z = np.matrix(z)
    mpl.plot(z[:,0],z[:,1],colors[i]+'o')

mpl.show()

cursor.close()
con.close()
