#!/usr/bin/env python3

from tkinter import *
import subprocess

class MainGUI(object):
        
    def __init__(self,window):
         
        self.window=window
        self.window.wm_title("HAProxy farm administration") #Main window label/title

        F1 = LabelFrame(window, text="HBDHB Infrastructure team", borderwidth=2, relief="groove")  #Create LabelFrame widget in main window 
        F1.grid(row=0, column=0, padx=3, pady=10, sticky="EW")             #Put LabelFrame widget in row 0 column 0      
        
        L1 = Label(F1, text="EXCHANGE",borderwidth=2, relief="ridge",fg="dark green")              #Add label "EXCHANGE"
        L1.grid(row=0, column=4,padx=3)

        L2 = Label(F1, text="ADFS",borderwidth=2, relief="ridge",fg="dark green")              #Add label "ADFS"
        L2.grid(row=0, column=5,padx=3,sticky="N")  
        
        L3 = Label(F1, text="IP FAILOVER",borderwidth=2, relief="ridge",fg="dark green")              #Add label "IP FAILOVER"
        L3.grid(row=0, column=6,padx=3,sticky="N")     
                           
        self.E1 = Listbox(F1,height=15, width=50)                           #Create Listbox widget (for output) 
        self.E1.grid(row=0,rowspan=13, column=0, padx=15, pady=15,  sticky="NS")
                
        B1 = Button(F1, text="Remove CAS01", width=12,command= lambda: self.remove_server('server Ex2010CasHt01'))   #Add button with label "Remove CAS01" which removes CAS01 server from the farm 
        B1.grid(row=1, column=4, padx=15, pady=3, sticky="WN")
        
        B2 = Button(F1, text="Remove CAS02",width=12,command= lambda: self.remove_server('server Ex2010CasHt02'))   #Add button with label "Remove CAS02" which removes CAS02 server from the farm
        B2.grid(row=2, column=4, padx=15, pady=3, sticky="WN")
           
        B3 = Button(F1, text="Remove CAS04", width=12,command= lambda: self.remove_server('server Ex2010CasHt04'))   #Add button with label "Remove CAS04" which removes CAS04 server from the farm
        B3.grid(row=3, column=4, padx=15, pady=3, sticky="WN")
        
        B4 = Button(F1, text="Remove CAS05",width=12,command= lambda: self.remove_server('server Ex2010CasHt05'))   #Add button with label "Remove CAS05" which removes CAS05 server from the farm
        B4.grid(row=4, column=4, padx=15, pady=3, sticky="WN")
        
        B5 = Button(F1, text="Add CAS01",width=12,command= lambda: self.add_server('server Ex2010CasHt01'))   #Add button with label "Add CAS01" which adds CAS01 server to the farm 
        B5.grid(row=5, column=4, padx=15, pady=3, sticky="NWN")
        
        B6 = Button(F1, text="Add CAS02",width=12,command= lambda: self.add_server('server Ex2010CasHt02'))   #Add button with label "Add CAS02" which adds CAS02 server to the farm 
        B6.grid(row=6, column=4, padx=15, pady=3, sticky="WN")
        
        B7 = Button(F1, text="Add CAS04",width=12,command= lambda: self.add_server('server Ex2010CasHt04'))   #Add button with label "Add CAS04" which adds CAS04 server to the farm 
        B7.grid(row=7, column=4, padx=15, pady=3, sticky="WN")
        
        B8 = Button(F1, text="Add CAS05",width=12,command= lambda: self.add_server('server Ex2010CasHt05'))   #Add button with label "Add CAS05" which adds CAS05 server to the farm 
        B8.grid(row=8, column=4, padx=15, pady=3, sticky="WN")

        B9 = Button(F1, text="Commit",width=12,command=self.commit)   #Add button with label "Commit" which reloads configuration
        B9.grid(row=9,column=4,columnspan=2, padx=15, pady=3, sticky="WENS")
        
        B10 = Button(F1, text="Clear screen",width=12,command=self.clear)   #Add button with label "Clear screen" which deletes output from the listbox 
        B10.grid(row=10, column=4, columnspan=2, padx=15, pady=3, sticky="WENS")
        
        B11 = Button(F1, text="Status",width=12,command=self.status)   #Add button with label "Status" which shows the status of the servers in the farm 
        B11.grid(row=11, column=4, columnspan=2, padx=15, pady=3, sticky="WENS")
        
        B12 = Button(F1, text="Close",width=12,command=self.close)   #Add button with label "Close" which closes the program 
        B12.grid(row=12, column=4, columnspan=2, padx=15, pady=3, sticky="WE")
        
        B13 = Button(F1, text="Remove ADFS-PROD",width=16,command= lambda: self.remove_server('server ADFS-PROD'))   #Add button with label "Remove ADFS-PROD" which removes ADFS-PROD server from the farm
        B13.grid(row=1, column=5, padx=5, pady=3, sticky="WN")
        
        B14 = Button(F1, text="Remove ADFS-DR",width=16,command= lambda: self.remove_server('server ADFS-DR'))   #Add button with label "Remove ADFS-DR" which removes ADFS-DR server from the farm
        B14.grid(row=2, column=5, padx=5, pady=3, sticky="WN")

        B15 = Button(F1, text="Add ADFS-PROD",width=16,command= lambda: self.add_server('server ADFS-PROD'))   #Add button with label "Add ADFS-PROD" which adds ADFS-PROD server to the farm 
        B15.grid(row=5, column=5, padx=5, pady=3, sticky="WN")
        
        B16 = Button(F1, text="Add ADFS-DR",width=16,command= lambda: self.add_server('server ADFS-DR'))    #Add button with label "Add ADFS-DR" which adds ADFS-PROD server to the farm 
        B16.grid(row=6, column=5, padx=5, pady=3, sticky="WN")
        
        B17 = Button(F1, text="Check IP",width=13,command=self.check_ip)   #Add button with label "Check IP" which shows in the output if one of the VIPs is present on the instance 
        B17.grid(row=1, column=6, padx=5, pady=3, sticky="WN")
        
        B18 = Button(F1, text="Keepalived start",width=13,command=self.start_keepalived)   #Add button with label "Keepalived start" which starts Keepalived service 
        B18.grid(row=2, column=6, padx=5, pady=3, sticky="WN")
        
        B19 = Button(F1, text="Keepalived stop",width=13,command=self.stop_keepalived)   #Add button with label "Keepalived stop" which stops Keepalived service  
        B19.grid(row=3, column=6, padx=5, pady=3, sticky="WN")
        
        B20 = Button(F1, text="Keepalived restart",width=13,command=self.restart_keepalived)   #Add button with label "Keepalived restart" which restarts Keepalived service  
        B20.grid(row=4, column=6, padx=5, pady=3, sticky="WN")
        
        B21 = Button(F1, text="Keepalived status",width=13,command=self.check_keepalived)   #Add button with label "Keepalived status" which cheks the status of the Keepalived service  
        B21.grid(row=5, column=6, padx=5, pady=3, sticky="WN")
        
        vScroll = Scrollbar(F1, orient=VERTICAL, command=self.E1.yview)    #Create vertical scroolbar
        vScroll.grid(row=0,rowspan=12, column=3, sticky='NS')    
        self.E1.configure(yscrollcommand=vScroll.set)
                
        window.mainloop()     
        
    def remove_server(self,server):               
        with open('/etc/haproxy/haproxy.cfg', 'r') as file :    # Read in the file
            filedata = file.read()
            
        if '#'+server in filedata:
            data = "You have already removed " + server + "!"
            self.E1.delete(0, END) 
            self.E1.insert(END,data)
        
        else:
                                    
            filedata = filedata.replace(" "+server, '#'+server)     # Replace the target string
                    
            with open('/etc/haproxy/haproxy.cfg', 'w') as file:     # Write the file out again
                file.write(filedata)
                data = "You have successfuly removed " + server
                data2 = "Dont forget to commit the changes!"
                self.E1.delete(0, END)
                self.E1.insert(END,data)
                self.E1.insert(END,data2)            
          
    def add_server(self,server):        
        with open('/etc/haproxy/haproxy.cfg', 'r') as file :    # Read in the file
            filedata = file.read()
        
        if '#'+server in filedata:
                 
            filedata = filedata.replace('#'+server, ' '+server)     # Replace the target string
               
            with open('/etc/haproxy/haproxy.cfg', 'w') as file:    # Write the file out again
                file.write(filedata)
                data = "You have successfuly added " + server
                data2 = "Dont forget to commit the changes!"
                self.E1.delete(0, END)
                self.E1.insert(END,data)
                self.E1.insert(END,data2)
        else:
            server = server[:1].upper() + server[1:]
            data = server + " is already active!"
            self.E1.delete(0, END)
            self.E1.insert(END,data)
                    
    def commit(self):
        subprocess.call('haproxy -D -f /etc/haproxy/haproxy.cfg -p /var/run/haproxy.pid -sf $(cat /var/run/haproxy.pid)',shell=True)
        notification = "You have successfully applied configuration!"
        self.E1.delete(0, END)
        self.E1.insert(END,notification)
           
    def clear(self):
        self.E1.delete(0, END)
        
    def status(self):
        with open('/etc/haproxy/haproxy.cfg', 'r') as file :    # Read in the file
            filedata = file.read()
            self.E1.delete(0, END)
            
        if "#server Ex2010CasHt01" in filedata:           
            self.E1.insert(END,"Ex2010CasHt01 is not active") 
            
        if "#server Ex2010CasHt02" in filedata:
            self.E1.insert(END,"Ex2010CasHt02 is not active")
            
        if "#server Ex2010CasHt04" in filedata:
            self.E1.insert(END,"Ex2010CasHt04 is not active")
            
        if "#server Ex2010CasHt05" in filedata:
            self.E1.insert(END,"Ex2010CasHt05 is not active")
        
        if "#server ADFS-PROD" in filedata:
            self.E1.insert(END,"ADFS-PROD is not active")
            
        if "#server ADFS-DR" in filedata:
            self.E1.insert(END,"ADFS-DR is not active")
        
        else:
            if "#server" not in filedata:
                self.E1.delete(0, END)
                self.E1.insert(END,"All servers are active")
    
    def check_ip(self):
        
        ip = subprocess.Popen("ip a | grep 'inet 10.32.128.1'", stdout=subprocess.PIPE, stderr=subprocess.PIPE,bufsize=1, universal_newlines=True,shell=True)
        self.E1.delete(0, END)
               
        comm = ip.communicate()
        stdoutValue, stderrValue = comm

        output_list = stdoutValue.split(" ")    #Split values in list by space. After the split we have a list of string in output_list
 
        if '10.32.128.147/32' in output_list:
            self.E1.insert(END,"EXCHANGE VIP 10.32.128.147 is present on this instance")
        if '10.32.128.100/32' in output_list:
            self.E1.insert(END,"ADFS          VIP 10.32.128.100 is present on this instance")
        else:
            self.E1.insert(END,"There is no VIPs on this instance")
            
    def start_keepalived(self):
        ip = subprocess.Popen("systemctl status keepalived.service", stdout=subprocess.PIPE, stderr=subprocess.PIPE,bufsize=1, universal_newlines=True,shell=True)
        self.E1.delete(0, END)
        for line in ip.stdout.readlines():
            if 'active (running)' in line:           
                self.E1.insert(END,"Service is already up and running!")
            elif 'inactive (dead)' in line:
                subprocess.call("systemctl start keepalived.service", stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, universal_newlines=True, shell=True)
                self.E1.insert(END,"Service has been successfully started!")
                
    def stop_keepalived(self):
        ip = subprocess.Popen("systemctl status keepalived.service", stdout=subprocess.PIPE, stderr=subprocess.PIPE,bufsize=1, universal_newlines=True,shell=True)
        self.E1.delete(0, END)
        for line in ip.stdout.readlines():
            if 'active (running)' in line:
                subprocess.call("systemctl stop keepalived.service", stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, universal_newlines=True, shell=True)           
                self.E1.insert(END,"Service has been successfully stopped!")
            elif 'inactive (dead)' in line:               
                self.E1.insert(END,"Service is already down!")
                
    def restart_keepalived(self):
        self.E1.delete(0, END)
        subprocess.call("systemctl restart keepalived.service", stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, universal_newlines=True, shell=True)           
        self.E1.insert(END,"Service has been successfully restarted!")
                                               
    def check_keepalived(self):
        ip = subprocess.Popen("systemctl status keepalived.service", stdout=subprocess.PIPE, stderr=subprocess.PIPE,bufsize=1, universal_newlines=True,shell=True)
        self.E1.delete(0, END)
        for line in ip.stdout.readlines():
            if 'active (running)' in line:           
                self.E1.insert(END,"Service is up and running")
            elif 'inactive (dead)' in line:
                self.E1.insert(END,"Service is down!")
   
    def close(self): #This function closes the program
        quit()
                                  
if __name__ == "__main__":
    window=Tk()
    gui=MainGUI(window)