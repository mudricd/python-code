#!/usr/bin/env python3
while True:
    choice = input('\nWould you like to delete all hosts? Yes/No ')
    print(choice)
    if choice.lower() == 'no':
        IP=input('\nPlease enter the host IP you want to delete: ')
        with open("/Users/mudricd/.ssh/known_hosts", "r") as f:
            lines = f.readlines()
        with open("/Users/mudricd/.ssh/known_hosts", "w") as f:
            for line in lines:
                if IP not in line:
                    f.write(line)
        print("You have successfully removed a host")            
        break

    elif choice.lower() == 'yes':
        with open("/Users/mudricd/.ssh/known_hosts", "w"):
            print("You have successfully removed all hosts")
            break
    
print('The End')


