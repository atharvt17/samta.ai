#please run below command before running this program

#pip install mysql-connector-python

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root", #Enter your username here
    password="Your Password" #Enter your password here
)
cursor = con.cursor()


cursor.execute("CREATE DATABASE school")
cursor.execute("USE school")

cursor.execute("""
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT,
    grade FLOAT
)
""")


cursor.execute("""
INSERT INTO students (first_name, last_name, age, grade)
VALUES (%s, %s, %s, %s)
""", ("Alice", "Smith", 18, 95.5))

cursor.execute("""
INSERT INTO students (first_name, last_name, age, grade)
VALUES (%s, %s, %s, %s)
""", ("Atharva", "Tripathi", 18, 96.5))

cursor.execute("""
INSERT INTO students (first_name, last_name, age, grade)
VALUES (%s, %s, %s, %s)
""", ("Will", "Smith", 20, 90.5))


con.commit()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("\nDetails Before Updating:-\n")
for row in rows:
    print(row)

cursor.execute("""
UPDATE students
SET grade = %s
WHERE first_name = %s
""", (97.0, "Alice"))
con.commit()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("\nDetails After Updating:-\n")
for row in rows:
    print(row)



cursor.execute("""
DELETE FROM students
WHERE last_name = %s
""", ("Smith",))
con.commit()


print("\nDetails after deleting Smith:-\n")

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)



cursor.close()
con.close()
