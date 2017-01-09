import random,pickle

def main():
    
    global name  # Name of the user that will be used in whole program
    name = input("What is your name: \n")   
    print("\nWelcome *** %s ***  \n" %(name) )
    
# Main menu with input for difficulty   
    while True:
        
        choice = input('''\nPlease choose the difficulty of the program:
        
E - for easy
M - for medium
H - for hard\n
:''')
        
        if choice == 'E':    #If choice is E then check the file and send notification 

            with open('data.pickle', 'rb') as f:
                data1 = pickle.load(f)
                if data1 == 'E':
                    print("\n You have just been there! \n")
                                
            with open('data.pickle','wb') as f:  #If choice is E after checking write E (choice) into the file 
                pickle.dump(choice,f)
                                        
            count(10,5) #Go to count function and break
            break
        
        
        elif choice == 'M':   #If choice is M then check the file and send notification 
            
            with open('data.pickle', 'rb') as f:
                data2 = pickle.load(f)
                if data2 == 'M':
                    print("You have just been there! \n")
                                
            with open('data.pickle','wb') as f:   #If choice is M after checking write M (choice) into the file 
                pickle.dump(choice,f)
                                  
            count(25,7)  #Go to count function and break
            break
        
        
        elif choice == 'H':
            
            with open('data.pickle', 'rb') as f:   #If choice is H then check the file and send notification
                data3 = pickle.load(f)
                if data3 == 'H':
                    print("You have just been there!\n")
                                
            with open('data.pickle','wb') as f:  #If choice is H after checking write H (choice) into the file
                pickle.dump(choice,f)
                
            count(100,9)  #Go to count function and break
            break
        
        else:
            print("Your choice can be only E, M or H (capitals).\n")
            
        
    while True: # Loop that asks for retry
                   
        loop = input('Would you like to try again? yes/no \n:')
                           
        if loop == 'yes':
            main()
            
        elif loop == 'no':
            break
        
        else:
            print("Answer can be only yes or no.\n")
        
    print("Have a nice day!")       

def count(ran,param): # Guessing the number depending on choice from main function 
    
    userTry = 0  # Initiate variable for guess counting
    x = random.randint(1,ran) # Random number. Range is from 1 to ran. Ran value is passed from main function and user choice
    print(x)
    
    for i in range(1,param): # loop with number limit. Range is from 1 to param. Param value is passed from main function and user choice
                
        while True:
                             
            try:
               
                guess = int(input("Please guess the number: \n"))
                userTry += 1 #guess counting
                break
                
            except ValueError:
                print("Number has to be integer. Please try again. \n")
                
        if x > guess:
                 
            print("Your guess is to low. This is you try number %d.  Please try again.\n" % (userTry))
            continue 
              
        elif x < guess:
            
            print("Your guess is to high. This is you try number %d.  Please try again.\n" % (userTry)) 
            continue
        
        elif x == guess:
            break
               
    if x == guess:
        
        print("Congratulations {}! You won! You tried {} times.\n".format(name,userTry))
        
    else:
   
        print("Sorry you have already tried %s times.\n" % (userTry))