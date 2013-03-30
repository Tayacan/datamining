import sqlite3 as sql
import math

conn = sql.connect("DataminingAssignment2013.db")
cursor = conn.cursor()

# Get the schema of a table
schema = cursor.execute('PRAGMA table_info(Sunspots_Train_Y);')

# Find some data
data = cursor.execute('select x1 from Sunspots_Train_X;')

# Get the data out of those ridiculous one-element tuples
xs = map(lambda x:x[0],data)

# Count the occurences of each element
counts = {}
for x in xs:
    if x in counts:
        counts[x] += 1
    else:
        counts[x] = 1

# This must be a float
n = float(len(xs))

# Calculate expected value of X
expected = sum(map(lambda x:x * (counts[x]/n),xs))
print "Expectation: %f" % (expected,)

variance = sum(map(lambda x:counts[x]/n*abs(x-expected),xs))
print "Variance: %f" % (variance,)
print "Standard deviation: %f" % (math.sqrt(variance),)

#for row in data:
#    print(row)

# Close off everything
cursor.close()
conn.close()
