
import random

def main(): #Main function
    
    #defining global variables and printing introduction
    global num    
    num = random.randint(10000,99999)
    global ones
    ones = num % 10
    global tens
    tens = (num // 10) % 10
    global hundreds
    hundreds = (num // 100) % 10
    global thousands
    thousands = (num // 1000)
    print("\nWelcome to the GAME!\n")
    print("The number is ****{}****\n".format(num))
    print("Thousands - {} || Hundreds - {} || Tens - {} || Ones - {}\n".format(thousands,hundreds,tens,ones))
    quest() #Calling the function quest() 
    

def quest(): # Function for random questioning, user input, checking if input is a integer and passing appropriate argument to to function check() 

    question = random.randint(1,4)
    
    while True:
    
        if question == 1:
            
            try:
                onesAnswer = int(input("Please enter ones!\n:"))
                check(onesAnswer,None,None,None)
            
            except ValueError:
                print("Number has to be integer.\n")
                
        if question == 2:
            
            try:
                tensAnswer = int(input("Please enter tens!\n:"))
                check(None,tensAnswer,None,None)
            
            except ValueError:
                print("Number has to be integer.\n")
                
        if question == 3:
            
            try:
                hundredsAnswer = int(input("Please enter hundreds!\n:"))
                check(None,None,hundredsAnswer,None)
            
            except ValueError:
                print("Number has to be integer.\n")
                
        if question == 4:
            
            try:
                thousandsAnswer = int(input("Please enter thousands!\n:"))
                check(None,None,None,thousandsAnswer)
                   
            except ValueError:
                print("Number has to be integer.\n")
                   

def check(onesAnswer,tensAnswer,hundredsAnswer,thousandsAnswer): # Function that checks if user input is correct and asks to try again or quits
       
    while True: #Loop that checks if user input is correct 
        
        if onesAnswer == ones:
            print("You won!\n") 
            break       
            
        if tensAnswer == tens:
            print("You won!\n")
            break
            
        if hundredsAnswer == hundreds:
            print("You won!\n")
            break
            
        if thousandsAnswer == thousands:
            print("You won!\n")
            break
            
        else:
            print("Sorry you miss!\n")
            break
        
    while True: #Loop that asks to continue or quits
        
        tryAgain = input("""Would you like to try again? yes/no/ova\n
yes - to try again with existing number
aoa - to try all over again
no  - to quit a game\n:""")
        
        if tryAgain == "yes":
            break       
        
        elif tryAgain == "no":
            print("\nSee you later aligator!")
            quit()
        
        elif tryAgain == "aoa":
            main() 
        
        else:
            print("Your answer can be only yes, no or aoa!\n")
    
            
# Variable initiation
onesAnswer = ""
tensAnswer = ""
hundredsAnswer = ""
thousandsAnswer = ""

if __name__ == '__main__': #Starts the program
    main()

