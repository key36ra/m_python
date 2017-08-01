import sqlite3


"""
Overview
"""
# Create "connection" obect.
conn = sqlite3.connect('example.db')

# Create "cursor" onject from "connection" object.
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()


"""
Rule to input securely
"""

# Never do this -- insecure!
symbol = 'RHAT'
c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

# Do this instead
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(c.fetchone())

# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
             ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)


"""
Get data from 'SELECT' command
"""

# Iterator
for row in c.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)

# fetchone()
c.execute('SELECT * FROM stocks ORDER BY price')
print(c.fetchone())

# fetchall()
c.execute('SELECT * FROM stocks ORDER BY prince')
print(c.fetchall())


"""
Cursor object
"""
# class sqlite3.connect().cursor()

# execute(sql[,parameters)
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("create table peaple (name_last, age)")
# This is the qmark style:
cur.execute("insert into people values (?,?)",(who,age))
# And this is the named style:
cur.execute("select * from people where name_last=:who and age=:age",{"who":who,"age":age})
print(cur.fetchone())

# executemany(sql, seq_of_parameters)


# executescript(sql_script)


# fetchone(), fetchmany(size=cursor.arraysize), fetchall()


# close()


"""
Row object
"""
# class sqlite3.Row

