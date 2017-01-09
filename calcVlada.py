#!/usr/bin/python
def enterNum():
    while True:
        try:
            return int(raw_input())
        except ValueError:
            print('Number has to be integer. Please try again.')

def enterOperator():
    while True:
        op = str(raw_input())
        if (op != '+' and op != '-' and op != '*' and op != '/'):
            print('It has to be valid operator.')
            continue
        else:
            return op

def calculate(num1, num2, operation):
    return eval(str(num1) + operation + str(num2))

def main():
    print "Welcome to the calculator app"
    print "Enter first number: "
    num1 = enterNum();
    print "Enter second number: "
    num2 = enterNum();
    print "Enter operation: "
    operation = enterOperator();
    print "Your Result is: {}".format(calculate(num1, num2, operation));

if __name__ == '__main__':
    main();
