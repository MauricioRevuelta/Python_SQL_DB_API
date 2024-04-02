!pip3 install ipython-sql
!pip install sqlalchemy==1.3.9

import sqlalchemy
import sqlite3
import pandas as pd

# Create the connect object
sqlconnection=sqlite3.connect("CP_records.db")

# Create cursor object
cursor=sqlconnection.cursor()

# Print a message if connection will be successful
print("Database connected successfully")

# Insert 10 new rows into the month1 table 
query="""INSERT INTO month1 VALUES(17, 45, 100, 130, 230.10), (18, 60, 110, 135, 200.10), (18, 60, 118, 110, 210.10), (19, 45, 120, 114, 230.42), (20, 45, 100, 130, 230.10),
 (21, 45, 150, 130, 230.70), (22, 60, 115, 130, 230.79), (23, 45, 109, 127, 230.45), (24, 45, 133, 122, 215.10), (25, 60, 110, 150, 256.09) """
cursor.execute(query)
sqlconnection.commit()

# Fetch all query to print the table after new data was added.
query="""SELECT * FROM month1 """
cursor.execute(query)
df = pd.DataFrame(cursor.fetchall())
print(df)

# Update values
query="""update month1 set Pulse=120 where field1=9 """
query1= """update month1 set Duration=45 where Pulse=184"""

# cursor.execute(query)
cursor.execute(query1)
sqlconnection.commit()

# Fetch all query to print the table values updated.
query="""SELECT * FROM month1 """
cursor.execute(query)
df = pd.DataFrame(cursor.fetchall())
print(df)

# Delete one record from the table
query="""delete from month1 where field1=20 """
cursor.execute(query)
sqlconnection.commit()
query="""SELECT * FROM month1 """
cursor.execute(query)
df = pd.DataFrame(cursor.fetchall())
print(df)