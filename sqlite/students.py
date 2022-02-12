import sqlite3
conn = sqlite3.connect("students_db.db")
c = conn.cursor()

# Create new Table
# c.execute("CREATE TABLE students (first_name TEXT, last_name TEXT, age INTEGER);")

# first_name = "Mike"
# last_name = "White"
# age = 25

# jane = ('Jane', 'Air', 18)
#
# students = [
#     ('Janny', 'Stone', 18),
#     ('Mike', 'Eastwood', 21),
#     ('Jon', 'Armstrong', 20),
#     ('Megan', 'Green', 19),
#     ('Anne', 'First', 22)
# ]

# c.execute("INSERT INTO students VALUES('James', 'Brown', 21);")


# Bad approach! SQL injection danger!
# insert_query = f"INSERT INTO students VALUES('{first_name}', '{last_name}', '{age}');"
# c.execute(insert_query)

# Good approach!
# insert_query = "INSERT INTO students VALUES(?, ?, ?);"
# c.execute(insert_query, (first_name, last_name, age))

# Also we can give "Tuple" object
# insert_query = "INSERT INTO students VALUES(?, ?, ?);"
# c.execute(insert_query, jane)

# With "FOR IN"
# insert_query = "INSERT INTO students VALUES(?, ?, ?);"
# for student in students:
#     c.execute(insert_query, student)


# insert_query = "INSERT INTO students VALUES(?, ?, ?);"
# c.executemany(insert_query, students)

# Reading
# c.execute("SELECT * FROM students WHERE first_name IS NOT 'Jon';")
# for row in c:
#     print(row)


# c.execute("SELECT * FROM students WHERE first_name IS NOT 'Jon';")
# print(c.fetchone())


# c.execute("SELECT * FROM students WHERE first_name IS NOT 'Jon';")
# print(c.fetchall())

c.execute("UPDATE students SET age='25'  WHERE last_name='Armstrong';")

c.execute("SELECT * FROM students")
data = c.fetchall()
[print(row) for row in data]

conn.commit()
conn.close()
