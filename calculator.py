for i in range(1, 6):

    try:
        number1 = int(input('Please enter the first number: '))
        number2 = int(input('Please enter the second number: '))
        operator = input('Please enter the operator: ')
        break
    except ValueError:
        print('Input cannot be string')
        continue
if i == 5:
    print('Sorry too many attempts ({}). Please try again'.format(i))
    quit()

elif operator == '+' : 
    result = number1 + number2
elif operator == '-' :
    result = number1 - number2
elif operator == '*' :
    result = number1 * number2
elif operator == '/' :
    result = number1 / number2
else:
    print('Operator cannot be string or integer')
print('Result is {} '.format(result))