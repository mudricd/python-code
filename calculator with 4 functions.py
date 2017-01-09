

def enterNum1():
    
    while True:
    
        try: 
            a = int(input('\nEnter the first number: '))
            return a
                    
        except ValueError:
            print('\nNumber has to be integer. Please try again.')   
   
   
    
def enterNum2():
    
    while True:
        
        try:    
            b = int(input('\nEnter the second number: '))
            return b

        except ValueError:
            print('\nNumber has to be integer. Please try again')


def operator():
    
    while True:
    
        op = input ('\nPlease enter operator:')
        
        if op != '+' and op != '-' and op != '*' and op != '/':
            print('\nIt has to be valid operator.')
            continue
        
        else:   
            return op
            break
        
    

def calculation():
    
    c = enterNum1()
    d = enterNum2()
    e = operator()
    
    if e == '+':
        sumo = c + d
        print('\nSum is {}'.format(sumo))

    elif e == '-':
        sumo = c - d
        print('\nSum is {}'.format(sumo))
        
    elif e == '*':
        sumo = c * d
        print('\nSum is {}'.format(sumo))
        
    elif e == '/':
        sumo = c / d
        print('\nSum is {}'.format(sumo)) 
    
              
calculation()


while True:
    
    quest = input('\nDo you want top continue (y/n) ?: ')
        
    if quest == 'y':
        calculation()
    
    elif quest == 'n':
        print('\nOk see you later!')
        break
    
    else:
        print('You must enter y or n.')
        continue




        

        
 
   