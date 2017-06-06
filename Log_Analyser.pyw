from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import threading

def main():
    
    global window
    window = Tk()   #Open main window  
    window.wm_title("Log Analyser") #Main window label/title
    
    global yesno
    yesno = BooleanVar(window)   #String for checkbutton  
    
    F1 = LabelFrame(window, text="", borderwidth=2, relief="groove")  #Create LabelFrame widget in main window 
    F1.grid(row=0, column=0, padx=3, sticky=(N, S, E, W))             #Put LabelFrame widget in row 0 column 0
       
    global E1
    E1 = Entry(F1, text="")                      #Create Entry widget (for file path) 
    E1.grid(row=0, column=1, sticky="EW")
        
    global E2
    E2 = Text(F1, height=30, width=80, fg="red")   #Create Text widget for log/file output
    E2.grid(row=3, column=1, sticky="EW")
    
    global E3
    E3 = Entry(F1, width=1)                       #Create Entry widget for entering string to search in browsed file
    E3.grid(row=1, column=1, sticky="EW") 
    
    global E4                                    
    E4 = Text(F1, height=1, width=8, fg="dark green")  # Create text widget for number of lines/rows in log output
    E4.grid(row=2, column=1, sticky="W")       
     
    hScroll = Scrollbar(window, orient=HORIZONTAL, command=E2.xview)  #Create horizontal scrollbar
    hScroll.grid(row=1, column=0, sticky='WE') 
    
    vScroll = Scrollbar(window, orient=VERTICAL, command=E2.yview)    #Create vertical scroolbar
    vScroll.grid(row=0, column=1, sticky='NS') 
    
    E2.configure(xscrollcommand=hScroll.set, yscrollcommand=vScroll.set, wrap = "none") #Add above created horizontal and vertical scrollbars to E2 text widget. Wrap=none will not break the line so you will need horizontal scrollbar to see the text
    
    L1 = Label(F1, text="Filename:")              #Add label "Filename"
    L1.grid(row=0, column=0, padx=3, sticky="E")
    
    L2 = Label(F1, text="Search string:")         #Add label "Search"
    L2.grid(row=1, column=0, sticky="E")
    
    L3 = Label(F1, text="Lines:")                 #Add label "Search"         
    L3.grid(row=2, column=0, sticky="E")
       
    global B1
    B1 = Button(F1, text="  Search  ", command=start_thread)   #Add button with label "Search" which triggers the function start_thread() 
    B1.grid(row=1, column=2, padx=30, pady=3, sticky="W")
    B1.bind("<Enter>", lambda event, h=B1: h.configure(bg="light gray")) #Change button color when hover
    B1.bind("<Leave>", lambda event, h=B1: h.configure(bg="SystemButtonFace")) #Change button color to default color when finish hovering
    
    B2 = Button(F1, text="Close", width=7, command=quit)   #Add button with label "Close" which triggers the function quit()
    B2.grid(row=3, column=2,padx=30, pady=3, sticky="NW")
    B2.bind("<Enter>", lambda event, h=B2: h.configure(bg="light gray")) #Change button color when hover
    B2.bind("<Leave>", lambda event, h=B2: h.configure(bg="SystemButtonFace")) #Change button color to default color when finish hovering
    
    B3 = Button(F1, text="Browse...", command=openfile)   #Add button with label "Browse..." which triggers the function openfile()
    B3.grid(row=0, column=2, padx=30, pady=3, sticky="W")
    B3.bind("<Enter>", lambda event, h=B3: h.configure(bg="light gray")) #Change button color when hover
    B3.bind("<Leave>", lambda event, h=B3: h.configure(bg="SystemButtonFace")) #Change button color to default color when finish hovering
    
    C1 = Checkbutton(F1, text="Highlight Search", variable=yesno, width=12, command=choice) #Add checkbutton with label "highlight" which triggers the function choice()
    C1.grid( row=2, column=2, padx=30, pady=3, sticky="W")
       
    window.columnconfigure(0, weight=1) #Next 6 lines enable auto resize of the window (when main window is maximised widgets moves accordingly)
    window.rowconfigure(0, weight=1)
    F1.columnconfigure(0, weight=3)
    F1.columnconfigure(1, weight=3)
    F1.columnconfigure(2, weight=3)
    F1.rowconfigure(1, weight=1)
    
    menubar = Menu(window) #Create toplevel menu 
    window.config(menu = menubar) 
          
    filemenu = Menu(menubar, tearoff=0)  #Create "File" menu bar and other submenus
    menubar.add_cascade(label = "File", menu = filemenu) 
    filemenu.add_command(label = "New", command = clear)
    filemenu.add_command(label = "Open", command = openfile)
    filemenu.add_command(label = "Save As...", command = save)
    filemenu.add_separator()
    filemenu.add_command(label = "Close", command = quit)
       
    editmenu = Menu(menubar, tearoff=0) #Create "Edit" menu bar and other submenus 
    menubar.add_cascade(label = "Edit", menu = editmenu)
    editmenu.add_command(label = "Cut", accelerator="Ctrl+X", command=lambda: window.event_generate('<Control-x>'))
    editmenu.add_command(label = "Copy", accelerator="Ctrl+C", command=lambda: window.event_generate('<Control-c>'))
    editmenu.add_command(label = "Paste", accelerator="Ctrl+V", command=lambda: window.event_generate('<Control-v>'))

    helpmenu = Menu(menubar, tearoff=0) # Create "Help" menu bar and other submenus
    menubar.add_cascade(label = "Help", menu = helpmenu)
    helpmenu.add_command(label = "About", command = about)
    helpmenu.add_command(label = "Disclaimer", command = disclaimer)
    
    global popupmenu
    popupmenu = Menu(menubar,tearoff=0) #Acreate popup menu with elements from menu bar menus from above (mouse right click)
    popupmenu.add_command(label = "Cut", accelerator="Ctrl+X", command=lambda: window.event_generate('<Control-x>'))
    popupmenu.add_command(label = "Copy", accelerator="Ctrl+C", command=lambda: window.event_generate('<Control-c>'))
    popupmenu.add_command(label = "Paste", accelerator="Ctrl+V", command=lambda: window.event_generate('<Control-v>'))
    popupmenu.add_separator()
    popupmenu.add_command(label = "New", command = clear)
    popupmenu.add_command(label = "Open", command = openfile)
    popupmenu.add_command(label = "Save As...", command = save)
    popupmenu.add_separator()
    popupmenu.add_command(label = "Close", command = quit)  
    
    window.bind("<Button-3>", popup) #Attach popup to the main window. Function that creates popup named "popup" is called here
    
    global progressbar
    progressbar = ttk.Progressbar(F1, orient=VERTICAL, length=200, mode='indeterminate', maximum=8) #Create progressbar. Maximum determines the speed of the progressbar movement.
    progressbar.grid(row=3, column=2, padx=10, pady=3, sticky="S") 
    
    grip = ttk.Sizegrip(window)   #Add Sizegrip widget which allows a user to resize entire application window. It is located in the bottom right corner of the application. 
    grip.grid(column=100, row=100, sticky=("se"))
             
    window.mainloop()   #Close main window
    

def about():    
    aboutText = """About

    This program is a basic log analyser. You can browse for a log file
    and display the content in the text box (Text Widget). You can also 
    type the search string and program will display only the lines with
    the search string. There is an option to highlight the search string 
    in the output. Output can be saved in the new file.
    Program was developed in 2017 by Dragan Mudric 
    """
    
    toplevel = Toplevel()
    label1 = Label(toplevel, text=aboutText, background = "white", foreground = "green4", height=8, width=56, pady = 20)
    label1.grid()
    
def clear(): #Clear all text from text and entry widgets
    E2.configure(state = "normal") #Enables write mode in the text box which was previously disabled in "go()" function
    E1.delete(0,END)
    E2.delete("1.0",END)
    E3.delete(0,END)
    E4.delete("1.0",END)
    E1.focus() #Focus to E1 (browse) Entry widget at the end of the function

def choice(event=None):  #If checkbutton is checked function find() will be executed. When unchecked function go() will be executed.   
    val = yesno.get()
    if val:
        find()
    else:
        go() 
    
def disclaimer():    
    disclaimerText = """Disclaimer

    Log Analyser v1.0 software was developed by Dragan Mudric.
    This program is free software. It comes without any warranty, to
    the extent permitted by applicable law. You can redistribute it
    and/or modify. Use at your own risk."""
        
    toplevel = Toplevel()
    label1 = Label(toplevel, text=disclaimerText, background = "white", foreground = "green4", height=8, width=56)
    label1.grid() 
        
def find():    
    E2.tag_remove('found', '1.0', END)   #Remove previous uses of tag `found', if any    
    s = E3.get()  #Get string to look for (if empty, no searching)
    
    if s:       
        idx = '1.0'   #Start from the beginning (and when we come to the end, stop)
        while 1:            
            idx = E2.search(s, idx, nocase=1, stopindex=END)   #Find next occurrence 
            if not idx: 
                break   #Exit loop if no more
            
            lastidx = ("{}+{}c").format(idx, len(s))   #Index right after the end of the occurrence           
            E2.tag_add('found', idx, lastidx)   #Tag the whole occurrence (start included, stop excluded)            
            idx = lastidx   #Prepare to search for next occurrence. Set the first index from the loop to be the last one so the search will start again but from the last found index.
        
        E2.tag_config('found', foreground='blue')   #Use a blue foreground for all the tagged occurrences    
    E3.focus_set()   #Give focus back to the Entry field

def go():    
    search=E3.get()                         #Get data from the Entry widget and store it into the variable
    with open(filename,'r') as jabber:      #This chunk of the code opens the file search the string and appends it into another file      
        for line in jabber:                                     
            if search in line:
                with open("file1error.txt","a") as file:
                    file.write(line)
                    
                 
    with open("file1error.txt","r") as file: #Open file
        data=file.read()                     #Read file and store it into the variable data       
        print(data)
        num_lines = sum(1 for line in open("file1error.txt")) #Count the number of lines in a file
        print(num_lines)
        E2.configure(state = "normal")       #Enable write mode in the text box. Later in fourth line down write mode will be disabled.
        E2.delete("1.0",END)                 #Delete everything from the E2 textbox
        E2.insert(END,data)                  #Insert file content stored in variable data into the E2 textbox
        E2.configure(state = "disabled")     #Disable writing in text box. For instance when there is an log output you won't be able to delete (edit) any displayed text.
        E4.delete("1.0",END)                 #Delete everything from the E4 textbox
        E4.insert(END,num_lines)             #Insert number of lines from log output stored in variable num_lines
        E4.tag_configure("center", justify='center') #Create and configure a tag named "center"
        E4.tag_add("center", "1.0", END)     #Apply tag named "center" which will center the number of lines number in E4 textbox

    with open("file1error.txt", "w"):        #Delete everything from the file "file1error.txt"
        pass        

def openfile():    
    global filename
    filename = filedialog.askopenfilename() #For file browsing and getting the path displayed
    E1.delete(0, END)                       #Delete the path from previous browsing
    E1.insert(0, filename)                  #Insert the path into the Entry box

def popup(event): #Create popup with popup menu elements created above 
    popupmenu.post(event.x_root, event.y_root)

def save(): # Function that saves the output from textbox into the file
    dialog = filedialog.asksaveasfile(mode = "w", defaultextension=".txt")
    saveText = str(E2.get(1.0, END))
    dialog.write(saveText)
    dialog.close()

def start_thread(): #Function that starts go() function as a separate thread from the main thread
    B1['state']='disable'  #Set the search button (B1) in disable state (grayed out)
    progressbar.start()  #Start progressbar 
    global secondaryThread
    secondaryThread = threading.Thread(target=go)   #Call function go() in new thread
    secondaryThread.start()   #Start thread's activity
    window.after(50, check_thread) #Call function check_thread() every 50 milliseconds

def check_thread():
    if secondaryThread.is_alive():
        window.after(50, check_thread) #Call function check_thread() every 50 milliseconds
    else:
        progressbar.stop()    #Stop progressbar if thread is not alive
        B1['state'] = 'normal'   #Set the search button (B1) to normal. Which means it is not grayed out any more and can be used again. 
        
def quit(): #Function that closes the program    
    close = messagebox.askyesno(message='Are you sure you want to exit?', icon='question', title='Log analyser') #yes/no message box
    
    if close:
        messagebox.showinfo(message='Have a good day!') #Massage box on exit
        exit()
        
    else:
        pass              
            
if __name__ == "__main__":    
    main() #Call main function









