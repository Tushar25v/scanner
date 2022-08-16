import sqlite3, csv

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

with open('data.csv','r') as file:
    count = 0
    for row in file:
        cursor.execute("INSERT INTO DATA VALUES (?,?,?,?,?,?,?,?,?,?,?)",row.split(","))
        connection.commit()
        count +=1
connection.close()
print(f"Records Transfered are {count}")