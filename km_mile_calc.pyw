from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def calc():
    KM=E1.get()
    miles = int(KM)*0.62137
    E2.insert(1.0,miles)

window = Tk()

F1 = LabelFrame(window, text="Mile calculator")
F1.grid(row=0, column=0, padx=3)

E1 = Entry(F1)
E1.grid(row=0,column=1)
L1 = Label(F1,text="KMs")
L1.grid(row=0,column=0,padx = 3)

E2 = Text(F1,height = 1, width = 15,)
E2.grid(row=1,column=1)
L2 = Label(F1,text="Miles")
L2.grid(row=1,column=0)

B1= Button(F1,text="Calculate",command = calc)
B1.grid(row=1,column=2)

window.mainloop()

