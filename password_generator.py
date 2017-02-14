def random_generator(size=8, chars=string.ascii_letters + string.digits + "!@#$%^&*()?" ):    
    return ''.join(random.choice(chars) for x in range(size))        
print(random_generator()) 

#Explenation:
#http://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-#and-digits-in-python



characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
chosen = random.sample(characters, 6)
password = "".join(chosen)
print(password)

#Explenation:
#We're importing the random  module and using its sample  method which picks 6 random items #from the characters  sequence. The items are stored in list chosen . Then we use a string #join method to join the list items to a string.