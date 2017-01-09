import random

print('What is your name? ')
name = input()
print("Hello {}. Idea is to gues the number between 1 and 20.".format(name))

ranNumber = random.randint(1, 20)

#print('Random number is {} . Delete this row later this is for debuging purposes'.format(ranNumber))



for rangeNum in range(1, 7):
#while True:
    print('\nPlease enter the random number: ')
    try:
        guessNum = int(input())
    except ValueError:
        print('Guess number has to be integer!')
        continue
        
    if guessNum > ranNumber:
        print('\nYour number is too high. PLease try again.')
    elif guessNum < ranNumber:
        print('\nYour number is too low. PLease try again.')
    else:
        break
    
if guessNum==ranNumber:
    print('\nYou are correct! Imginary number was {} and you tried  {} times!'.format(ranNumber, rangeNum))
else:
    print('\nToo much attempts {}'.format(guessNum))