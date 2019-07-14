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

#returns all students in the database
def get_all(self):
        c.execute("SELECT * FROM students")
        return(c.fetchall())

#returns all students at the given appointment time
def get_by_time(time):
    try:
        c.execute("SELECT * FROM students WHERE time=:time", {'time':time})
        return c.fetchall()
    except:
        print("An invalid time was entered")

#returns all students assigned to a certain OA
def get_by_oa(oa_name):
    try:
        c.execute("SELECT * FROM students WHERE OA=:OA", {'OA':oa_name})
        return c.fetchall()
    except:
        print("An invalid OA name was entered")

#returns all students with a certian status
def get_by_status(status):
    try:
        c.execute("SELECT * FROM students WHERE status=:status", {'status':status})
        return c.fetchall()
    except:
        print("An invalid status was entered")

#updates a student's status
def update_status(first, last, major, time, newstatus):
    first = first.upper() #likely not the best way, but sets all inputs to uppercase to mitigate case errors
    last = last.upper()
    major = major.upper()
    time = time.upper()
    newstatus = newstatus.upper()
    with conn:
        try:
            c.execute("""UPDATE students SET status=:status
                        WHERE first=:first AND last=:last AND time=:time AND major=:major""",
                        {'first':first, 'last':last, 'time':time, 'major':major, 'status':newstatus})
        except:
            print("An invalid input was entered")


createTable(None) #used for debugging with :memory: table
insertAll(None) #inserts all students from csv into the table
update_status('john','smith','ME','9:45 AM', 'ARRIVED')
print(get_by_status('ARRIVED'))


conn.commit()
#conn.close()
