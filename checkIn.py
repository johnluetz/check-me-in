#script for checking in students for their advising appointments
import tkinter as tk
from csvHandler import insertStudent, get_by_time, update_status

class Window(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("YEET") #title of master
        self.pack(fill = tk.BOTH, expand = 1) #widget takes full space
        timeButton = tk.Button(self, text="SELECT", command=self.display_names) #create a button (time)
        timeButton.place(x=100, y=23) #place button

        nameButton = tk.Button(self, text="CHECK IN", command=self.check_in) #name
        nameButton.place(x=100, y=75)

    #updates the second dropdown with the corresponding names
    def display_names(self):
        refresh_students(None)
        print(timevar.get())
    
    #checks a student in
    def check_in(self):
        print(studvar.get()) #call db with student name as arg and update the status

#basic GUI code     

root = tk.Tk()
root.geometry("400x300") #size of window
app = Window(root)

#time dropdown
timevar = tk.StringVar(root)
times = ['10:00 AM','10:15 AM','10:30 AM','10:45 AM','11:00 AM','11:15 AM','11:30 AM','11:45 AM','12:00 PM','12:15 PM','12:30 PM','12:45 PM','1:00 PM','1:15 PM','1:30 PM','1:45 PM','2:00 PM','2:15 PM','2:30 PM','2:45 PM','3:00 PM','3:15 PM','3:30 PM','3:45 PM','4:00 PM']
times_dict = {times[i] : i for i in range(0,len(times))} #lists all time slots
timevar.set('10:00 AM')
timeMenu = tk.OptionMenu(app, timevar, *times_dict)
tk.Label(app, text="Select a time").grid(row = 1, column = 1)
timeMenu.grid(row = 2, column = 1)

#student dropdown
studvar = tk.StringVar(root)
students = []
students_dict = {'Student'}
studentMenu = tk.OptionMenu(app, studvar, *students_dict)
tk.Label(app, text="Select your name").grid(row = 5, column = 1)
studentMenu.grid(row = 6, column = 1 )






def change_dropdown(item):
    studvar.set(item)

def refresh_students(self):
    studvar.set('')
    studentMenu['menu'].delete(0, 'end') #reset dropdown

    nss_dict = {'Longhorn','Bevo', 'Semokey'} #insert new list
    for item in nss_dict:
        studentMenu['menu'].add_command(label=item,command=tk._setit(studvar, item))


root.mainloop() #runs last!

