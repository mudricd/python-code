from tkinter import *

def main():
   
    root = Tk() #Open main window   
    root.wm_title("Calculator") #Main window label/title
    
    #Function that calculates expression from textbox
    def calc():        
        resul=eval(E2.get("1.0", END))
        E2.delete("1.0",END)

        if resul == int(resul):  #If resul is a whole number it will strip 0 from the end. Generally it will change resul from float to integer
            insert(int(resul))
        else:
            insert(resul)
            
    #Function that deletes everything from textbox   
    def clear():
        E2.delete("1.0",END)
    
    #Function that inserts characters from the buttons in textbox       
    def insert(char):
        E2.tag_configure("left", justify='right') 
        E2.insert(END,char,"left")
    
    #Fuction that closes the program
    def quit():
        exit()
    
    
    def popup(event): #Create popup with popup menu. This is for mouse right click cut, copy, paste and close.
        popupmenu.post(event.x_root, event.y_root)
    
    #Create popup with information 
    def about():    
        aboutText = """About
    
        This program is a basic Calculator. You can use
        the folowing operations: +, -, / and *.
        Program was developed by Dragan Mudric in 2017. 
        """
        toplevel = Toplevel()
        label1 = Label(toplevel, text=aboutText, background = "white", foreground = "green4", height=5, width=45, pady = 20)
        label1.grid()
        
    def disclaimer(): #Create popup with information       
        disclaimerText = """Disclaimer
    
        Log Analyser v1.0 software was developed by Dragan Mudric.
        This program is free software. It comes without any warranty, to
        the extent permitted by applicable law. You can redistribute it
        and/or modify. Use at your own risk."""
            
        toplevel = Toplevel()
        label1 = Label(toplevel, text=disclaimerText, background = "white", foreground = "green4", height=8, width=56)
        label1.grid() 
    
    #Create Label Frame widget
    F1 = LabelFrame(root, text="Calculator v1.0", borderwidth=2, relief="groove")  #Create frame in main window 
    F1.grid(row=0, column=0, padx=3, sticky=(N, S, E, W))             #Put LabelFrame widget in row 0 column 0
    
    #Create Text widget for calculation output
    global E2
    E2 = Text(F1, height=2, width=22,font=14) 
    E2.grid(row=1, column=1,pady=7, columnspan=5, sticky="W") 

        

    #Create buttons
    B1 = Button(F1, text="7", height=1, width=3, font=("Arial",10,"bold"), command=lambda: insert("7")).grid(row=2, column=1, sticky = "WENS")
    B2 =Button(F1, text="8", height=1, width=3, font=("Arial",10,"bold"), command=lambda: insert("8")).grid(row=2, column=2, sticky="WENS")
    B3 =Button(F1, text="9", height=1, width=3, font=("Arial",10,"bold"), command=lambda: insert("9")).grid(row=2, column=3, sticky="WENS")
    B4 =Button(F1, text="/", height=1, width=3, font=("Arial",10,"bold"), command=lambda: insert("/")).grid(row=2, column=4, sticky="WENS")
    B5 =Button(F1, text="4", height=1, width=3, font=("Arial",10,"bold"), command=lambda: insert("4")).grid(row=3, column=1, sticky="WENS")
    B6 =Button(F1, text="5", height=1, width=3, font=("Arial",10,"bold"), command=lambda: insert("5")).grid(row=3, column=2, sticky="WENS")
    B7 =Button(F1, text="6", height=1, width=3, font=("Arial",10,"bold"), command=lambda: insert("6")).grid(row=3, column=3, sticky="WENS")
    B8 =Button(F1, text="*", height=1, width=3, font=("Arial",10,"bold"), command=lambda: insert("*")).grid(row=3, column=4, sticky="WENS")
    B9 =Button(F1, text="1", height=1, width=3, font=("Arial",10,"bold"), command=lambda: insert("1")).grid(row=4, column=1, sticky="WENS")
    B10 =Button(F1, text="2", height=1, width=3, font=("Arial",10,"bold"), command=lambda: insert("2")).grid(row=4, column=2, sticky="WENS")
    B11 =Button(F1, text="3", height=1, width=3, font=("Arial",10,"bold"), command=lambda: insert("3")).grid(row=4, column=3, sticky="WENS")
    B12 =Button(F1, text="-", height=1, width=3, font=("Arial",10,"bold"), command=lambda: insert("-")).grid(row=4, column=4, sticky="WENS")
    B13 =Button(F1, text="0", height=1, width=7, font=("Arial",10,"bold"), command=lambda: insert("0")).grid(row=5, column=1, columnspan=2, sticky="WENS")
    B14 =Button(F1, text=".", height=1, width=3, font=("Arial",10,"bold"), command=lambda: insert(".")).grid(row=5, column=3, sticky="WENS")
    B15 =Button(F1, text="+", height=1, width=3, font=("Arial",10,"bold"), command=lambda: insert("+")).grid(row=5, column=4, sticky="WENS")
    B16 =Button(F1, text="=", height=3, width=3, font=("Arial",10,"bold"), command=calc).grid(row=4, column=5, rowspan=2, sticky="WENS")
    B17 =Button(F1, text="C", height=3, width=3, font=("Arial",10,"bold"), command=clear).grid(row=2, column=5, rowspan=2, sticky="WENS")
    
    menubar = Menu(root) #Add toplevel menu 
    root.config(menu = menubar) 
    
    #Add "File" menu bar and other submenus      
    filemenu = Menu(menubar, tearoff=0)  
    menubar.add_cascade(label = "File", menu = filemenu) 
    filemenu.add_command(label = "Clear", command = clear)
    filemenu.add_command(label = "Quit", command = quit)
    
    #Add "Edit" menu bar and other submenus 
    editmenu = Menu(menubar, tearoff=0) 
    menubar.add_cascade(label = "Edit", menu = editmenu)
    editmenu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: root.event_generate('<Control-x>'))
    editmenu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: root.event_generate('<Control-c>'))
    editmenu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: root.event_generate('<Control-v>'))
    
    # Add "Help" menu bar and other submenus
    helpmenu = Menu(menubar, tearoff=0) 
    menubar.add_cascade(label = "Help", menu = helpmenu)
    helpmenu.add_command(label = "About", command=about)
    helpmenu.add_command(label = "Disclaimer", command=disclaimer)
    
    #Create popup menu with elements from menu bar menus from above. Mouse right click cut, copy, paste and close.
    popupmenu = Menu(menubar,tearoff=0) 
    popupmenu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: root.event_generate('<Control-x>'))
    popupmenu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: root.event_generate('<Control-c>'))
    popupmenu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: root.event_generate('<Control-v>'))
    popupmenu.add_separator()
    popupmenu.add_command(label = "Close", command = quit)
    
    root.bind("<Button-3>", popup) #Attach popup to the main window. Function that creates popup named "popup" is called here. Mouse right click cut, copy, paste and close.
    
    mainloop() #Close the loop, main window

#Call the function main()
if __name__ == "__main__":
    main()