import string

while True:
    
    passwd = input("Please enter your password: \n")
    check1 = string.digits
    check2 = string.ascii_uppercase    
        
    if len(passwd) >= 5 and any(i in passwd for i in check1) and any(i in passwd for i in check2) :
        print("Password is OK")
        break        
    
    else:
        print("Password is NOT ok")