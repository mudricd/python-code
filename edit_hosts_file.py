
from tkinter.messagebox import YES
import time

print("\n*** This is YouTube blocker written by Dragan Mudric ***\n")

while True:
    password = input("Enter the password: \n")
    if password == "zinka":
        print("\nPassword matched!")
        break
        
    else:
        print("\nPassword is incorrect. Please try again.\n")

while True:
  
    answer = input("\nDo you want to block or unblock YouTube? block/unblock \n")

    if answer=="block":
        with open('C:\Windows\System32\drivers\etc\hosts', 'a') as f:
            f.write('127.0.0.1     www.youtube.com  ')
            print("YouTube is blocked!\n")
            time.sleep(5)
        break

    elif answer=="unblock":
        with open("C:\Windows\System32\drivers\etc\hosts", "r") as w:
            lines = w.readlines()
        with open("C:\Windows\System32\drivers\etc\hosts", "w") as w:
            for line in lines:
                if "youtube" not in line:
                    w.write(line)
            print("YouTube is unblocked!\n")        
            time.sleep(5)
            
        break

    else:
        print("\nYou need to type block or unblock. Please try again.")
