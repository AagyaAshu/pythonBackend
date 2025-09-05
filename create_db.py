from db_config import mydb

# Create a cursor from the existing connection
mycursor = mydb.cursor()

# Define your insert query
sql = "INSERT INTO students (name, roll_no) VALUES (%s, %s)"
val = [("Abhilasha jha", 102),("aagya aashu",700)]

# Execute and commit
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")