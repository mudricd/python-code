from tkinter import *
from tkinter import ttk
from tkinter import filedialog

#Function that converts KMs in miles and inserts the result in textbox(E2)
def calc():
    KM=E1.get()
    miles = int(KM)*0.62137
    E2.insert(1.0,miles)
	
#Open main window
window = Tk() 

#Creates LabelFrame in main window
F1 = LabelFrame(window, text="Mile calculator")
F1.grid(row=0, column=0, padx=3)

#Create Entry widget and Label for it
E1 = Entry(F1)
E1.grid(row=0,column=1)
L1 = Label(F1,text="KMs")
L1.grid(row=0,column=0,padx = 3)

#Create Text widget and Label for it
E2 = Text(F1,height = 1, width = 15,)
E2.grid(row=1,column=1)
L2 = Label(F1,text="Miles")
L2.grid(row=1,column=0)

#Create button which calls function calc() 
B1= Button(F1,text="Calculate",command = calc)
B1.grid(row=1,column=2)

#Close main window
window.mainloop() 

