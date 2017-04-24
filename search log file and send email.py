import smtplib,os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

lista=[] #initiating list 
with open('C:\\Users\\dmudric\\workspace\\Learning\\file1.txt','r') as jabber:        
    for line in jabber:                                    
        if 'error' in line: 
            lista.append(line) #Appending list with the line with error in it
            stringa = "".join(lista) #Converting list to a string
            
try:                           
    if stringa.strip(): #This will check if string has any characters. If it can "strip" then it is not empty
        
        #Creating variables                                                       
        fromaddr = "logsearch@citrix.com" 
        toaddr = "dragan.mudric@hbdhb.govt.nz"
        subject = "An error has been found in the log"
        body = stringa
        
        #Creating email 
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        #Sending email 
        server = smtplib.SMTP('10.32.128.146', 25)
        server.ehlo()
        text = msg.as_string() #Converting object to a string
        server.sendmail(fromaddr, toaddr, text)
        print("Email with error logs has been sent to you!")
    
except NameError:
    print("The file is empty!")