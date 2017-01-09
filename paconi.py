
#print('My name is')
#for i in range(5):
 #   print('Jimmy Five Times (' + str(i) + ')')
 
 # -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 08:36:50 2016

@author: dmudric
"""
print(''' Cao packo kako te? Ja poceo malo da ucim python. Nije toliko lose za sad.
 Ali nije kao sto Goxa kaze samo da znas sta je string sta je integer i odmah si sve skapirao :)
 \n Da li hoces da nastavis dalje? (da/ne) :''')
while True:
    
    choice1 = input()
    if choice1 == 'da':
        print('''\nDobro si izabrao! Napisacu ti ovde sta sam radio da te malo uputim.
Kazu da se python lako uci i da je to najpopularniji programski jezik trenutno.''')
        break
    elif choice1 == 'ne':
        print('\nNemoj biti packo moras da zagrejes stolicu! POZDRAV')
        quit()
    else:
        print("Odgovor mora biti 'da' ili 'ne'. Pokusaj ponovo :  ")
        
print('''\nOk nastavljamo dalje. Bitno je da imas neko osnovno znanje iz programiranja.
Da znas sta je promenjiva, string, integer itd. Ne bi bilo lose i da znas sta je petlja (while,for)
i da znas sta su if,elif,else statements. Ne mislim da znas da koristis sve to ali makar da znas
sta je. To su neke univerzalne stvari. Python ima svoju sintaksu tako da ces to nauciti.
\nEvo jedan primer petlje. Namerno pogresi dole nekoliko puta da vidis kako ce da te vraca.
\nPlease enter your name (input (name) is case sensitive) :''')
name = input()
while name != 'Milos':
    print('\nYou missed the name. Please try again : ')
    name = input()
    
print('''\nEto to tako izgleda kad se izvrsi. Mozes da pogledas kod mada ce ti to biti jasnije kad pocnes da ucis.
Ok idemo sad dalje. Hoces da nastavis ili ides na kaficu? (dalje/kafica) : ''')

while True:
    
    choice2 = input()
    if choice2 == 'dalje':
        print('''\nOpa moram da priznam da si me pozitivno iznenadio. Ocekivao sam da ces da kazes "Ma sta ovaj sere!" i da odes na fuka :) .
Ok da ne prdimo puno. Prvo sto sam uradio je otisao sam na www.udemy.com i nasao besplatni python for beginers kurs. Tu sam skapirao 
elementarne stvari. Onda sam nasao jedan veliki kurs koji sam platio 30$. Traje bas dosta i vredi te pare. Nasao sam i super
online knjigu www.automatetheboringstuff.com nju prelazim kad mi je muka od video kursa. Usput pisem ove programcice zajebancije.
Daleko sam ja jos uvek od nekog skriptinga ali ide polako. Jebem li ga ja racunam da cu za godinu dana intenzivnog rada biti solidan.''')
        break
    
    elif choice2 == 'kafica':
        print('\nZnao sam da si paconi! Pozdrav')
        exit()
    
    else:
        ("Odgovor moze biti samo 'dalje' ili 'kafica'. Pokusaj ponovo : ")

print('''\nEto to ti je to ukratko. Cujemo se pa cemo da pricamo. Ne bi bilo lose da pocnes i ti da radis ovo pa da resavamo probleme zajedno.
Lakse je kad se uci u paru. Secas se kako smo Troda i ja ucili :) ? Nadam se da ste vas dvoje u paketu dobro. Pozdravi suprugu obavezno.
\nZa kraj pritisni q da izadjes iz programa : ''')
choice3 = input()
while choice3 != 'q':
    print('Moras da ukucas q ili ces zauvek da se vrtis :) :')
    choice3 = input()
print('''                 P O Z D R A V  
                   _
                 _(_)_                      
     @@@@       (_)@(_)  vVVVv    _     @@@@
    @@()@@ wWWWw  (_)\   (___)  _(_)_  @@()@@
     @@@@  (___)     `|/   Y   (_)@(_)  @@@@
      /      Y       \|   \|/   /(_)    \|
   \ |     \ |/       | /\ | / \|/       |/
  DM |///  \\|/// \\\\|//\\|///\|///  \\\|//
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ''')
