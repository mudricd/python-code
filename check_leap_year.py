

def main():
    
    while True:
        
        try:
            year = int(input("Please input the year you want to check\n:"))
            check(year)
            break
        
        except ValueError:
            print("Please enter the valid year\n:")

def check(year):
    
    
    if (year % 4 == 0) and (year % 400 == 0):
        print("This is a leap year.\n")
    
    elif (year % 4 == 0) and (year % 100 == 0):
        print("This year IS NOT leap.\n")
    
    elif year % 4 == 0:
        print("This IS a leap year.\n")
        
    else:
        print("This IS NOT a leap year.\n")
        
    while True:    
        
        again = input("Would you like to try again?\n:")
        
        if again == "yes":
            main()
        elif again == "no":
            print("Cao!")
            quit()
        else:
            print("Your answer can be only yes or no!\n")

if __name__ == '__main__':
    main()