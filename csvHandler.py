#csvHandler.py
#imports the csv and dumps it into an sqlite3 database
import csv
import sqlite3

from student import Student

conn = sqlite3.connect(':memory:')
c = conn.cursor()

#used for debugging with :memory:
def createTable(self):
    c.execute("""CREATE TABLE students (
            first text,
            last text,
            major text,
            OA text,
            time text,
            status text
            )""")

# reads students from the CSV file and calls insertStudent to add them to the database
def insertAll(self):
    with open('OAroster.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        line_count = 0 #used to not include the first row
        for row in csv_reader:
            if line_count == 0: #first row is column names, printed just for debug
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                if(row[0] != ''): #if row contains data
                    longhorn = Student(row[2],row[1],row[3],row[6],row[7])
                    insertStudent(longhorn)
                else: #no data in the row
                    print("Skipped Row!")
                line_count += 1

# adds a student object to the database
def insertStudent(Student):
    with conn:
        c.execute("INSERT INTO students VALUES (:first, :last, :major, :OA, :time, :status)",
        {'first':Student.first,'last':Student.last,'major':Student.major,'OA':Student.OA,'time':Student.time,'status':Student.status})
        print("Added "+Student.first+" "+Student.last)

def display_all(self):
    with conn:
        c.execute("SELECT * FROM students")
        return(c.fetchall())

createTable(None) #used for debugging with :memory: table
insertAll(None)
print(display_all(None))

conn.commit()
conn.close()







# for row in csv_reader:
#     if line_count == 0:
#         print(f'Column names are {", ".join(row)}')
#         line_count += 1
#     else:
#         print(row[2] + ' ' + row[1])
#         line_count += 1
# print(line_count)