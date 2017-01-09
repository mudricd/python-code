print("""*************
*           *
* MAIN MENU *
*           * 
*************\n""")
    
    
def pick():
    
    while True:
                          
            choice1 = input("""\nWhat would you like to pick:
    ****************************
    (S)word
    (A)rmor""")
            
            if choice1 == 'S':
                print("\nYou picked up a sword!\n")
                break
            elif choice1 == 'A':
                print('\nYou picked up very rusty Armor!\n')
                break
            else:
                print('\nPlease note that you can pick only "S" or "A" so please try again.\n')
            

def search():

    while True:            
            
        
        choice2 = input("""Where would you like to search:
****************************
(R)ocks
(F)allen tree \n\nMake your selection:\n""")
        if choice2 == 'R':
            print("\nIt is very ROCKY there!\n")
            break
        elif choice2 == 'F':
            print('\nThat Fallen Tree was very big!\n')
            break
        else:
            print("You can chose only 'R' or 'F'. Please try again.\n ")
            
                
def run():          
    
    print("You have chosen to exit. See you later aligator!")
    quit()

def main():
    
    while True:
    
        print("""Make your initial selection:
    (P)ick up object
    (S)earch the area
    (R)un away""")
            
        first = input("\nMake your selection:\n")
        
        if first == 'P':
            pick()
            
        elif first == 'S':
            search()
            
        elif first == "R":
            run()
            
        else:
            print("You can chose only 'P' or 'S' or 'R'. Please try again.\n ")

if __name__ == '__main__':
    main()
    