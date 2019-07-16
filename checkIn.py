#script for checking in students for their advising appointments
import tkinter as tk
from tkinter import ttk
from csvHandler import insertStudent, get_by_time, update_status, get_by_status
import slackbot
from slackbot import notify_advisor#, start_bot
from multiprocessing import Process

class Window(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Engineering Advising Check-In") #title of master
        self.pack(fill = tk.BOTH, expand = 1) #widget takes full space
        timeButton = tk.Button(self, text="SELECT", command=self.display_names) #create a button (time)
        timeButton.place(x=200, y=23) #place button

        nameButton = tk.Button(self, text="CHECK IN", command=self.check_in) #name
        nameButton.place(x=200, y=75)

    #updates the second dropdown with the corresponding names
    def display_names(self):
        studnames = []
        nowtime = timevar.get() #get the selected time
        timedata = get_by_time(nowtime)
        for student in timedata:
            studnames.append(student[0]+" "+student[1])
        refresh_students(studnames) #refresh the dropdown
        
    
    #checks a student in
    def check_in(self):
        nowtime = timevar.get()
        selected_student = studvar.get()
        timedata = get_by_time(nowtime)
        for student in timedata:
            if selected_student == student[0]+" "+student[1]: #if the selected student is one in the database
                update_status(student[0],student[1],nowtime,"ARRIVED") #call db with student name as arg and update the status
                print(get_by_status('ARRIVED'))
                notify_advisor(student[3],(student[0]+" "+student[1]),student[2],student[4])#send notification
                popupmsg(selected_student+ " has been checked in!")
                break
         

#basic GUI code     

root = tk.Tk()
root.geometry("400x300") #size of window
app = Window(root)

#time dropdown
timevar = tk.StringVar(root)
times = ['9:45 AM','10:00 AM','10:15 AM','10:30 AM','10:45 AM','11:00 AM','11:15 AM','11:30 AM','11:45 AM','12:00 PM','12:15 PM','12:30 PM','12:45 PM','1:00 PM','1:15 PM','1:30 PM','1:45 PM','2:00 PM','2:15 PM','2:30 PM','2:45 PM','3:00 PM','3:15 PM','3:30 PM','3:45 PM','4:00 PM']
times_dict = {times[i] : i for i in range(0,len(times))} #lists all time slots
timevar.set('9:45 AM')
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

#creates a pop-up message to confirm check-in
def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()


#called by display_names to update the student selection list
def refresh_students(studnames):
    studvar.set('')
    studentMenu['menu'].delete(0, 'end') #reset dropdown

    nss_dict = {studnames[i] : i for i in range(0, len(studnames))} #insert new list
    for item in nss_dict:
        studentMenu['menu'].add_command(label=item,command=tk._setit(studvar, item))

#start_bot(None)
if __name__ == '__main__':
    #Process(root.mainloop()).start() #runs last!
    #Process(start_bot(None)).start()
    #start_bot(None)
    root.mainloop()


