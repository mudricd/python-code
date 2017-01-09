def calc(num1,num2,oper):
    

    if oper == '+':
        rezul=int(num1)+int(num2)
        print('\nRezultat je {} '.format(rezul))
        return rezul   
    elif oper == '-':
        rezul=num1-num2
        print('\nRezultat je {} '.format(rezul))
        return rezul
    elif oper == '*':
        rezul=num1*num2
        print('\nRezultat je {} '.format(rezul))
        return rezul
    elif oper == '/':
        rezul=num1/num2
        print('\nRezultat je {} '.format(rezul))
        return rezul
    
    

while True:
        
    try:        
        x = int(input('\nPlease enter first num: '))
        y = int(input('\nPlease enter second num: '))
        
        
        while True:
            
            z = input('\nPlease enter operator: ')
            if z == '+':
                break
            elif z == '-':
                break
            elif z == '*':
                break
            elif z == '/':
                break
            else:  
                print('It has to be operator')  
                
        break
    except ValueError:
        print('\nIt has to be integer')

rezultat = calc(x,y,z)


print('\nRezultat {} je izracunat u funkciji'.format(rezultat))