#script for checking in students for their advising appointments
from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("YEET") #title of master
        self.pack(fill = BOTH, expand = 1) #widget takes full space
        timeButton = Button(self, text="SELECT", command=self.client_exit) #create a button
        timeButton.place(x=85, y=23) #place button

    def client_exit(self):
        exit()

#basic GUI code     

root = Tk()
root.geometry("400x300") #size of window
app = Window(root)
tkvar = StringVar(root)
choices = {'yadda','yeet','boys'}
tkvar.set('yadda')
popupMenu = OptionMenu(app, tkvar, *choices)
Label(app, text="Select a time").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

def change_dropdown(*args):
    print(tkvar.get())

root.mainloop() #runs last!

