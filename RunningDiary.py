from tkinter import *
import sqlite3
from PIL import Image, ImageTk


class MainGUI(object):
        
    def __init__(self,window,db):
         
        self.window=window
        self.db=db
        self.window.wm_title("Running Diary") #Main window label/title

        F1 = LabelFrame(window, text="Dragan Mudric", borderwidth=2, relief="groove")  #Create LabelFrame widget in main window 
        F1.grid(row=0, column=0, padx=3, sticky="EW")             #Put LabelFrame widget in row 0 column 0
        
        self.E1 = Entry(F1)                           #Create Entry widget (for date) 
        self.E1.grid(row=1, column=0, padx=15)
        
        L1 = Label(F1, text="Date:")              #Add label "Date"
        L1.grid(row=0, column=0,padx=3,sticky="S")
        
        self.E2 = Entry(F1)                           #Create Entry widget (for location) 
        self.E2.grid(row=1, column=1, padx=15)
        
        L2 = Label(F1, text="Location:")              #Add label "Location"
        L2.grid(row=0, column=1,padx=3,sticky="S")
        
        self.E3 = Entry(F1)                           #Create Entry widget (for distance) 
        self.E3.grid(row=1, column=2, padx=15)
        
        L3 = Label(F1, text="Distance in km:")              #Add label "Distance in km"
        L3.grid(row=0, column=2,padx=3,sticky="S")
        
        runphoto=PhotoImage(file="run.gif")                   #Add photo 1
        L4 = Label(F1, image=runphoto)                        
        L4.grid(row=3, column=4, padx=7, pady=10,ipady=30, sticky="S")  
        
        myphoto=PhotoImage(file="me.gif")                     #Add photo 2
        L5 = Label(F1, image=myphoto)                         
        L5.grid(row=3, column=4, padx=7, pady=130, sticky="S" )  
        
        self.E4 = Listbox(F1,height=20, width=10)                           #Create Listbox widget (for run details output) 
        self.E4.grid(row=2, rowspan=4, columnspan=3, padx=15, pady=4,  sticky="EW")
        self.E4.bind("<<ListboxSelect>>",self.get_selected_row)    #Call function get_selected_row when click on activity in listbox. Function returns the index (id) of the row. 
                
        B1 = Button(F1, text="Add run", width=12, command=self.insert_command)   #Add button with label "Add run" which inserts the run details 
        B1.grid(row=1, column=4, padx=15, pady=3, sticky="W")
        
        B2 = Button(F1, text="View all runs",width=12, command=self.view_all_command)   #Add button with label "View all runs" which shows all inserted runs
        B2.grid(row=2, column=4, padx=15, pady=3, sticky="WN")
           
        B3 = Button(F1, text="Search run", width=12, command=self.search_command)   #Add button with label "Search run" which search the run details 
        B3.grid(row=3, column=4, padx=15, pady=3, sticky="WN")
        
        B4 = Button(F1, text="Delete run",width=12, command=self.delete_command)   #Add button with label "Delete run" which deletes the run details 
        B4.grid(row=3, column=4, padx=15, pady=35, sticky="WN")
        
        B5 = Button(F1, text="Update run",width=12, command=self.update_command)   #Add button with label "Update run" which updates the run details 
        B5.grid(row=3, column=4, padx=15, pady=66, sticky="WN")
        
        B6 = Button(F1, text="Close",width=12, command=self.close)   #Add button with label "Close" which inserts the run details 
        B6.grid(row=3, column=4, padx=15, pady=97, sticky="WN")
        
        B7 = Button(F1, text="Total km",width=12, command=self.total_km_command)   #Add button with label "Close" which inserts the run details 
        B7.grid(row=0, column=4, padx=15, pady=3, sticky="S")
        
        vScroll = Scrollbar(F1, orient=VERTICAL, command=self.E4.yview)    #Create vertical scroolbar
        vScroll.grid(row=3, column=3, sticky='NS')    
        self.E4.configure(yscrollcommand=vScroll.set)
                
        window.mainloop()

    def delete_command(self):    #This function calls delete_run() function and pass the index of selected activity from the listbox output as the argument.
        self.db.delete_run(self.selectedTuple[0])
        self.E1.delete(0,END)        
        self.E2.delete(0,END)        
        self.E3.delete(0,END)
        self.E4.delete(0, END)
        self.view_all_command()
        
    def update_command(self):    #This function calls update_run(id,date,location,distance) function and pass the arguments previously taken from the entry widgets excluding id.           
        self.db.update_run(self.selectedTuple[0],self.E1.get(),self.E2.get(),self.E3.get())
        self.E4.delete(0, END)
        self.view_all_command()
       
    def view_all_command(self):    #This function calls get_all_runs() and then inserts the output in listbox (E4) 
        data = self.db.get_all_runs()
        self.E4.delete(0, END)    
        for row in data:
            self.E4.insert(END,row)
    
    def search_command(self):    #This function calls search_run() and then inserts the output in listbox (E4)
        self.E4.delete(0, END)
        for row in self.db.search_run(self.E1.get(),self.E2.get(),self.E3.get()):
            self.E4.insert(END,row)
                               
    def insert_command(self):    #This function calls insert_run() which inserts new run into the database
        self.db.insert_run(self.E1.get(),self.E2.get(),self.E3.get())
        self.E4.delete(0, END)
        self.E4.insert(END,(self.E1.get(),self.E2.get(),self.E3.get()))
        
    def get_selected_row(self, event):     #This function gets the index of the selected activity in listbox and then inserts Date,Location and Distance in appropriate entry widgets
        try:                    
            index=self.E4.curselection()[0]
            self.selectedTuple=self.E4.get(index)
            if "Total kilometers" not in self.E4.get(index):
                self.E1.delete(0,END)
                self.E1.insert(END,self.selectedTuple[1])
                self.E2.delete(0,END)
                self.E2.insert(END,self.selectedTuple[2])
                self.E3.delete(0,END)
                self.E3.insert(END,self.selectedTuple[3])
            else:
                pass
        except IndexError:
            pass
    
    def total_km_command(self):
        self.E4.delete(0, END)
        data=[i[0] for i in database.total_km()]
        sum=0
        for i in data:
            sum=sum+i
        self.E4.insert(END,("Total kilometers you have done so far are " + str(sum) + (". Well done!")))
        
        
    def close(self): #This function closes the program
        quit()
        
    def _del_(self):          #Destructor that closes the connection to the database
         self.curs.close()
         self.conn.close() 
                  
class Database():
        
    def __init__(self, dbName):            #_init_ function creates database if it doesn't exist
        self.conn = sqlite3.connect(dbName)
        self.curs = self.conn.cursor() 
        self.curs.execute("CREATE TABLE IF NOT EXISTS diary (id INTEGER PRIMARY KEY, date TEXT, location TEXT, distance INTEGER)")   
        self.conn.commit()
                    
    def insert_run(self,date,location,distance): #Adding activity. This function gets date,location and distance from entry widgets and then pass them as the arguments for the function add_entry. At the end it clears listbox and inserts the activity.
        self.curs.execute("INSERT INTO diary VALUES (NULL,?,?,?)", (date,location,distance))
        self.conn.commit() 
                         
    def get_all_runs(self):   
        self.curs.execute("SELECT * FROM diary")
        data = self.curs.fetchall()
        return data           
    
    def search_run(self,date="",location="",distance=""): #This function connects to the database and gets the activity (row) depending on the condition. So for example, if you type Hastings in Location entry widget and press "Search Entry" button this function will output every row where location was Hastings. 
        self.curs.execute("SELECT * FROM diary WHERE date=? OR location=? OR distance=?",(date,location,distance))
        data = self.curs.fetchall()
        return data
              
    def delete_run(self,id): #This function connects to the database and deletes the row (activity) with passed argument which is id of the row in the database (activity)      
        self.curs.execute("DELETE FROM diary WHERE id=?",(id,))
        self.conn.commit()
            
    def update_run(self,id,date,location,distance): #This function connects to the database and updates the row (activity) with the arguments passed by the update_command() function.         
        self.curs.execute("UPDATE diary SET date=?, location=?,distance=? WHERE id=?",(date,location,distance,id))
        self.conn.commit()
        
    def total_km(self):   
        self.curs.execute("SELECT distance FROM diary")
        data = self.curs.fetchall()
        return data
                 
if __name__ == "__main__":
    database = Database("database.db")
    window=Tk()
    gui=MainGUI(window,database)
