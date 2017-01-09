

import random, time, os



def main():
    
    
    name = input("Zdravo. Kako se zoveš?\n:")
    
    print("\nCao %se! Dobro došao u S T A R  W A R S!\n" %(name))
    print("MAY THE FORCE BE WITH YOU YOUNG JEDI!\n")
    input("Pritisni <ENTER> da nastaviš.\n")
    planet()
        
    input("Pritisni <ENTER> da nastaviš.\n")
    #time.sleep(1)   
    story1()                  
     
    input("Pritisni <ENTER> da nastaviš.\n")
    #time.sleep(1)
    rebel_ships()
    
    input("Pritisni <ENTER> da nastaviš.\n")
    #time.sleep(1)   
    story1_1()
    
    input("Pritisni <ENTER> da nastaviš.\n")
    #time.sleep(1)   
    story1_2()

    
    input("Pritisni <ENTER> da nastaviš.\n")
    #time.sleep(1)   
    story1_3()

    input("Pritisni <ENTER> da nastaviš.\n")
    #time.sleep(1)
    star_destroyer()
    time.sleep(1)
    star_destroyer2()
    time.sleep(1)
    star_destroyer3()
    time.sleep(1)
    star_destroyer4()
    time.sleep(1)
    star_destroyer5()
    time.sleep(1)
    star_destroyer6()
           
    input("Pritisni <ENTER> da nastaviš.\n")
    selection()


def selection():
    
    while True:
         
        side = input("Da li želiš da budeš na Dark ili Light side?\n")
               
        if side.lower() == 'dark':
            
            os.startfile("darth.mp3") # Starts Darth Vader theme you need to copy file to working directory
            
            while True:

                darkJedi = input("""Sa kim bi hteo da se boriš:
                
1. Dart Vejder
2. Kajlo Ren
3. Dart Mol
4. General Grivijus
5. Kaunt Duku
6. Dart Sidijus\n:""")
                
                if darkJedi.lower() =="dart vejder":
                    
                    value = light_fighter_generator()
                    #===========================================================
                    # print("Snaga izabranog Light Dzedaja je %d"%(value))
                    #===========================================================
                    fight(darthVader,value)
                    repeat()
                    
                elif darkJedi.lower() =="kajlo ren":
                    
                    value = light_fighter_generator()
                    fight(kyloRen,value)
                    repeat()
                    
                elif darkJedi.lower() =="dart sidijus":
                    value = light_fighter_generator()
                    fight(darthSidius,value)
                    repeat()
                    
                elif darkJedi.lower() =="dart mol":
                    value = light_fighter_generator()
                    fight(darthMol,value)
                    repeat()
                
                elif darkJedi.lower() =="general grivijus":
                    value = light_fighter_generator()
                    fight(generalGrivius,value)
                    repeat()
                
                elif darkJedi.lower() =="kaunt duku":
                    value = light_fighter_generator()
                    fight(kauntDuku,value)
                    repeat()
                
                else:
                    print("Nisi dobro upisao ime Džedaja. Molim te pokušaj ponovo.\n")
           
        
    
        elif side.lower() == 'light':
            
            os.startfile("light.mp3") #Starts Star Wars theme you need to copy file to working directory
            
            while True:
                
                lightJedi = input("""Sa kim bi hteo da se boriš:
                       
1. Luk Skajvoker
2. Obi Van Kenobi
3. Joda
4. Mace Windu
5. Kui Gon Džin
6. Princeza Lea\n:""")
                
                if lightJedi.lower() =="luk skajvoker":
                    value = dark_fighter_generator()
                    fight(value,luk)
                    repeat()
                    
                elif lightJedi.lower() =="obi van kenobi":
                    value = dark_fighter_generator()
                    fight(value,obiVan)
                    repeat()
        
                elif lightJedi.lower() =="joda":
                    value = dark_fighter_generator()       
                    fight(value,joda)
                    repeat()
                
                elif lightJedi.lower() =="mace windu":
                    value = dark_fighter_generator()
                    fight(value,maceWindu)
                    repeat()
                    
                elif lightJedi.lower() =="kui gon dzin":
                    value = dark_fighter_generator()
                    fight(value,quiGonJinn)
                    repeat()
                    
                elif lightJedi.lower() =="princeza lea":
                    value = dark_fighter_generator()
                    #===========================================================
                    # print("Snaga izabranog Dark Dzedaja je %d"%(value))
                    # print("Snaga Princeze Lee je %d"%(lea))
                    #===========================================================
                    fight(value,lea)
                    repeat()

                else:
                    print("Nisi dobro upisao ime Džedaja. Molim te pokusaj ponovo.\n")
                
        else:
            print("Moraš da izabereš izmedu dark ili light.Molim te pokušaj ponovo.\n")
    
def light_fighter_generator():
    
    lightList = list(lightDict.keys()) # Knvertovanje dictionary u list
    lightRand = random.choice(lightList) # Random choosing character from the list
    value = int(lightDict.get(lightRand)) # Getting value from the key from dictionary
    print("\nTvoj protivnik je %s!\n"% lightRand)
    print("Borba je pocela!\n")
    time.sleep(3)
    return value

def dark_fighter_generator():
    
    darkList = list(darkDict.keys()) # Knvertovanje dictionary u list
    darkRand = random.choice(darkList) # Random choosing character from the list
    value = int(darkDict.get(darkRand)) # Getting value from the key from dictionary
    print("\nTvoj protivnik je %s!\n"% darkRand)
    print("Borba je pocela!\n")
    time.sleep(3)
    return value    
    
def fight(dark,light):
        
    if dark > light:
        print("Dark Džedaj je upalio svoj light saber i krenuo u napad!\n")
        time.sleep(1)
        print("Light Džedaj pokušava da se odbrani ali nema dovoljno sile...\n ")
        time.sleep(1)
        print("Dark Džedaj je pobedio!\n")
        time.sleep(1)
        dart()
    elif light > dark:
        print("Light Džedaj je upalio svoj light saber i krenuo u napad!\n")
        time.sleep(1)
        print("Dark Džedaj pokušava da se odbrani ali nema dovoljno sile!\n")
        time.sleep(1)
        print("Light Džedaj pobeduje i pobunjenici slave!\n")
        time.sleep(1)
        print("Pobunjenici su iskoristili šansu pobegli u Millenium Falcon i odleteli sa planete!\n")
        time.sleep(1)
        falcon()
    else:
        print("Oba Džedaj su upalili svoje light sabers i poceli da se bore!\n")
        time.sleep(1)
        print("Dark Džedaj je uspeo da rani Ligh Džedaja!\n")
        time.sleep(1)
        print("Light Džedaj je uzvratio i ranio Dark Džedaja!\n")
        time.sleep(1)
        print("Oba Džedaja su ranjena i nemaju snage da nastave borbu!\n")
        time.sleep(1)
        
def repeat():
    
    while True:
    
        choice = input("Da li želis ponovo da igraš? da/ne\n")
        if choice.lower() == "da":
            selection()
            
        elif choice.lower() == "ne":
            print("\nVoli te tvoj tata najviše na svetu!\n")
            time.sleep(1)
            print("TOGETHER WE CAN RULE THE GALAXY AS FATHER AND SON...\n")           
            quit()
        
        else:
            print("Moraš da ukucaš da ili ne. Molim te pokušaj ponovo.\n")
        
def planet():
    
    print("""



                 .                 .                    .                .
          .               A long time ago in a galaxy far, far away...   .              .             .             .          .
             .               .           .               .        .             .
     +        .      .            .                 .                                .      *        .             .
         .      .         .         .   . :::::+::::...      .          .         .
             .         .      .    ..::.:::+++++:::+++++:+::.    .     .                 .    .               ..             .
      .                         .:.  ..:+:..+|||+..::|+|+||++|:.             .     .
                    .   .    :::....:::::::::++||||O||O#OO|OOO|+|:.    .                     .           .             .
        .      .      .    .:..:..::+||OO#|#|OOO+|O||####OO###O+:+|+               .
                         .:...:+||O####O##||+|OO|||O#####O#O||OO|++||:     .    .          -o-         .     .              .
          .             ..::||+++|+++++|+::|+++++O#O|OO|||+++..:OOOOO|+  .         .
  .          .   .     +++||++:.:++:..+#|. ::::++|+++||++O##O+:.++|||#O+    .              .          .             .
        .           . ++++++++...:+:+:.:+: ::..+|OO++O|########|++++||##+            .
          .       .  :::+++|O+||+::++++:::+:::+++::+|+O###########OO|:+OO       .  .              +        .                .
             .       +:+++|OO+|||O:+:::::.. .||O#OOO||O||#@###@######:+|O|  .
   .     .          ::+:++|+|O+|||++|++|:::+O#######O######O@############O              .                        .       .
                  . ++++: .+OO###O++++++|OO++|O#@@@####@##################+         .                 . 
              .     ::::::::::::::::::::++|O+..+#|O@@@@#@###O|O#O##@#OO####     .
    .    .        . :. .:.:. .:.:.: +.::::::::  . +#:#@:#@@@#O||O#O@:###:#| .      .             .               .       .
                                   `. .:.:.:.:. . :.:.:%::%%%:::::%::::%:::
        .      .                                      `.:.:.:.:   :.:.:.:.  .   .
                   .           . .                                                   .                       *
                   
                   
                   \n

""")
    
def story1():
    
    print("""
                                          .    .           .
    .    .            .           .         .         .       .   .  +     .          .             .        .          .
       .            .        .  .      .      .   .       .      .      .     .  .   .         .
   -o-          .    .   .   .      .         .  . .       .    .        .  .    .       .    .                     .      .      .
                +    .    . .   .     Pre mnogo mnogo godina u jako udaljenoj            .         .      .     .     
     .          .     .            galaksiji u svemiru, odvijala se bitka izmedu  .    .    .   .    .      *    .    .
             . .     .        Imperije i pobunjenika... Pobunjenici se se sastali na  .     .        .    .        .
       . *        .      planeti Tatoin u kaficu Beka.Tu su bili Luk Skajvoker, princeza Lea, 
              Kui Gon Džin ,Mejs Vindu, Obi Van Kenobi, Joda C3PO, R2D2 i jos nekoliko  rebel trupera.\n   .        .     .    .
     .       .     . .  .
                 .       .         .     .    .   .       *     .    .        .         .              .      .         .
    .        .        .     .       .           .  .     .          .  .         .            .           .       .         .
      .  .       .       .         .      . .  . .           .          . .           . .   +         .       .        .
    """)
    
def story1_1():
    
    print("""
    
Kada su ušli u kafic R2D2 je izašao ispred da cuva stražu.
    
                           
                .---.       
              .'_:___". 
              |__ --==|
              [  ]  :[|       
              |__| I=[|     
              / / ____|     
             |-/.____.'      
            /___\ /___\      
         
   
    
    """)  


    
def story1_2():
    
    print("""
    
Boba Fet je sve to video i odmah je javio Dart Vejderu da su se pobunjenici sastali u kaficu Beka!
    
    
               |~
               |.---.
              .'_____`. /\
              |~xxxxx~| ||
              |_  #  _| ||
         .------`-#-'-----.
        (___|\_________/|_.`.
         /  | _________ | | |
        /   |/   _|_   \| | |
       /   /X|  __|__  |/ `.|
      (  --< \\/    _\//|_ |`.
      `.    ~----.-~=====,:=======
        ~-._____/___:__(``/| |
          |    |      XX|~ | |
           \__/======| /|  `.|
           |_\|\    /|/_|    )
           |_   \__/   _| .-'
           | \ .'||`. / |(_|
           |  ||.'`.||  |   )
           |  `'|  |`'  |  /
           |    |  |    |\/   Boba Fett
    
    """)
    
def story1_3():
    
    print(""" 
    
       
 .             .            .    . .   .                 .         .      .     .                           .                  .
             .          .     .            .    .    .   .    .          .    .  .    .
                     . .     .          .     .        .    .        .                   .     *        .            . 
        .       .         .      +    .    .                               .    .      .
   .                                .        .     .    .       *        .                .    .        . 
         .    .       .       .   .   .     .                                                                    .         .
               .             Dart Vejder je sve ispricao Dart Sidijusu i on je odmah    .        .      .        
      .                naredio da se krene u napad. Poslao je svoju flotu zajedno sa lošim                       .      . 
                    džedajima iz Dark Side... Tu su bili skoro svi sa Dark Side. Dart Vejder,
          .  .    Dart Mol, Kajlo Ren, General Grivijus, Kaunt Duku i mnogo mnogo storm trupera.\n. .  .    
                     .                   .              .              .              .                         .     .           .
                         .                  BORBA MOZE DA POCNE...          .             .           .   
     .                   .       .         .     .    .   .            .    .        .         .              .                
            .    *    .        .     .  +     .           .  .     .      *    .  .         .            .                -o-
              .  .       .       .         .      . .  . .           .          . .           . .            . 
    
    """)
    
def dart():
    
    print("""
    
                  _________
                  III| |III
                IIIII| |IIIII
               IIIIII| |IIIIII
               IIIIII| |IIIIII
              IIIIIII| |IIIIIII
              IIIIIII\ /IIIIIII
             II (___)| |(___) II
            II  \    /D\    /  II
           II  \ \  /| |\  / /  II
          II    \_\/|| ||\/_/    II
         II     / O-------O \     II
        II_____/   \|||||/   \_____II
              /               \

                         
""")
    
def star_destroyer():
    print("""
    
    
    

                  _        .                          .            (
                 (_)        .       .                                     .             .        .                .
  .        ____.--^.
   .      /:  /    |                               +           .         .          .
         /:  `--=--'   .                                                .            *             .                  .
        /: __[\==`-.___          *           .
       /__|\ _~~~~~~   ~~--..__            .             .
       \   \|::::|-----.....___|~--.                                 .                      -o-               .
        \ _\_~~~~~-----:|:::______//---...___
    .   [\  \  __  --     \       ~  \_      ~~~===------==-...____
        [============================================================-
        /         __/__   --  /__    --       /____....----''''~~~~      .                .          .                .
  *    /  /   ==           ____....=---='''~~~~ .
      /____....--=-''':~~~~                      .                .
      .       ~--~              .           .        Star Destroyer               .           .                    .   
                     .              *                     .           .
                          .                      .             +                                                           .     +              .                                       <=>       .                      .
                                               .                .      .
   .                 *                 .                *                ` -                                                                         .             .              .       .
                                           .
                              .-o
                 .           /  |
        .                 . /   |   .      .        .       .         .           .          .        *        .
                           /    |
                  .       /     |     .                .           .         .          ..                           .
  .                      /      /         .
             .          /    _./   .
                   _.---~-.=:_                    +            .                         .           .    
                  (_.-=() <~`-`-.
                 _/ _() ~`-==-._,>  .       .                              .       -o-       .                     .
         ..--====--' `~-._.__()
     o===''~~             |__()
                .         \   |             .   .          .      .           . *                     .               .
                           \  \
                            \  \     .
        .                    \  \              .                 .                .         .              .        .
                 .            \  \         Imperial Shuttle         .                              .
                               \_ \        .
                                 ~o         .                              .                    +       .
              .       .                   
      .                        
                          .             .              .                                .                               
                                 
                       
 
  """)
    
def star_destroyer2():
    print("""
        
    
                      _        .                          .            (
                     (_)        .       .                                     .             .        .                .
      .        ____.--^.
       .      /:  /    |                               +           .         .          .
             /:  `--=--'   .                                                .            *             .                  .
            /: __[\==`-.___          *           .
           /__|\ _~~~~~~   ~~--..__            .             .
  .        \   \|::::|-----.....___|~--.                                 .                      -o-               .
            \ _\_~~~~~-----:|:::______//---...___
        .   [\  \  __  --     \       ~  \_      ~~~===------==-...____
.           [============================================================-
            /         __/__   --  /__    --       /____....----''''~~~~      .                .          .                .
      *    /  /   ==           ____....=---='''~~~~ .
          /____....--=-''':~~~~                      .                .
          .       ~--~                                 Star Destroyer               .           .                    .   
                         .                                   .           .
                              .                      .             +
 .           .     +              .                                       <=>       .                      .
                                                   .                .      .
  .     .                 *                 .                *                ` -
     .                                                                        .             .              .       .
                                               .
     .                            .-o
                     .           /  |
            .                 . /   |   .      .        .       .         .           .          .        *        .
                               /    |
                      .       /     |     .                .           .         .          ..                           .
      .                      /      /         .
                 .          /    _./   .
                       _.---~-.=:_                    +            .                         .           .    
                      (_.-=() <~`-`-.
                     _/ _() ~`-==-._,>  .       .                              .       -o-       .                     .
             ..--====--' `~-._.__()
         o===''~~             |__()
                    .         \   |             .   .          .      .           . *                     .               .
                               \  \
                                \  \     .
            .                    \  \              .                 .                .         .              .        .
                     .            \  \         Imperial Shuttle         .                              .
                                   \_ \        .
                                     ~o         .                              .                    +       .
                  .       .                   
          .                        
                              .             .              .                                .                               
                                     
                       
 
  """)

def star_destroyer3():
    print("""
    
        
                          _        .                          .            (
                         (_)        .       .                                     .             .        .                .
    .     .        ____.--^.
           .      /:  /    |                               +           .         .          .
      .          /:  `--=--'   .                                                .            *             .                  .
                /: __[\==`-.___          *           .
  .       .    /__|\ _~~~~~~   ~~--..__            .             .
               \   \|::::|-----.....___|~--.                                 .                      -o-               .
    .  .      \ _\_~~~~~-----:|:::______//---...___
            .   [\  \  __  --     \       ~  \_      ~~~===------==-...____
  .     .       [============================================================-
                /         __/__   --  /__    --       /____....----''''~~~~      .                .          .                .
          *    /  /   ==           ____....=---='''~~~~ .
              /____....--=-''':~~~~                      .                .
    .         .       ~--~                                 Star Destroyer               .           .                    .   
                             .                                   .           .
                                  .                      .             +
      .         .     +              .                                       <=>       .                      .
                                                       .                .      .
   .       .                 *                 .                *                ` -
                                                                                 .             .              .       .
                                                   .
     .   .                          .-o
                         .           /  |
   .            .                 . /   |   .      .        .       .         .           .          .        *        .
                                   /    |
                          .       /     |     .                .           .         .          ..                           .
          .                      /      /         .
                     .          /    _./   .
   .                       _.---~-.=:_                    +            .                         .           .    
                          (_.-=() <~`-`-.
         .               _/ _() ~`-==-._,>  .       .                              .       -o-       .                     .
                 ..--====--' `~-._.__()
     .       o===''~~             |__()
                        .         \   |             .   .          .      .           . *                     .               .
                                   \  \
                                    \  \     .
                .                    \  \              .                 .                .         .              .        .
                         .            \  \         Imperial Shuttle         .                              .
                                       \_ \        .
                                         ~o         .                              .                    +       .
                      .       .                   
              .                        
                                  .             .              .                                .                               
                                 
                       
 
  """)
    
def star_destroyer4():
    print("""
    

                                  _        .                          .            (
   .        .                    (_)        .       .                                     .             .        .                .
                  .        ____.--^.
                   .      /:  /    |                               +           .         .          .
     .    .              /:  `--=--'   .                                                .            *             .                  .
                        /: __[\==`-.___          *           .
                       /__|\ _~~~~~~   ~~--..__            .             .
   .       .           \   \|::::|-----.....___|~--.                                 .                      -o-               .
                        \ _\_~~~~~-----:|:::______//---...___
   +                .   [\  \  __  --     \       ~  \_      ~~~===------==-...____
                        [============================================================-
     .      .           /         __/__   --  /__    --       /____....----''''~~~~      .                .          .                .
                  *    /  /   ==           ____....=---='''~~~~ .
                      /____....--=-''':~~~~                      .                .
   .     .            .       ~--~                                 Star Destroyer               .           .                    .   
                                     .                                   .           .
                                          .                      .             +
  .   .                 .     +              .                                       <=>       .                      .
                                                               .                .      .
                   .                 *                 .                *                ` -
                                                                                         .             .              .       .
  .    .         .      .                                      .
                                              .-o
                                 .           /  |
   .      .             .                 . /   |   .      .        .       .         .           .          .        *        .
                                           /    |
                                  .       /     |     .                .           .         .          ..                           .
                  .                      /      /         .
   .       .                 .          /    _./   .
                                   _.---~-.=:_                    +            .                         .           .    
                                  (_.-=() <~`-`-.
      .        .                 _/ _() ~`-==-._,>  .       .                              .       -o-       .                     .
                         ..--====--' `~-._.__()
   *       .         o===''~~             |__()
                                .         \   |             .   .          .      .           . *                     .               .
                                           \  \
                                            \  \     .
      .                 .                    \  \              .                 .                .         .              .        .
                                 .            \  \         Imperial Shuttle         .                              .
   .        .                                  \_ \        .
                                                 ~o         .                              .                    +       .
          +                    .       .                   
           .           .                        
                                          .             .              .                                .                               
                                                 
                       
 
  """)
    
def star_destroyer5():
    print("""
    
        
                                          _        .                          .            (
           .        .                    (_)        .       .                                     .             .        .                .
   .  .                   .        ____.--^.
                           .      /:  /    |                               +           .         .          .
    .  .     .    .              /:  `--=--'   .                                                .            *             .                  .
                                /: __[\==`-.___          *           .
                               /__|\ _~~~~~~   ~~--..__            .             .
           .       .           \   \|::::|-----.....___|~--.                                 .                      -o-               .
  .      .                      \ _\_~~~~~-----:|:::______//---...___
           +                .   [\  \  __  --     \       ~  \_      ~~~===------==-...____
                                [============================================================-
.            .      .           /         __/__   --  /__    --       /____....----''''~~~~      .                .          .                .
                          *    /  /   ==           ____....=---='''~~~~ .
  .                         /____....--=-''':~~~~                      .                .
           .     .            .       ~--~                                 Star Destroyer               .           .                    .   
     .    .                                    .                                   .           .
                                                  .                      .             +
          .   .                 .     +              .                                       <=>       .                      .
    .    .                                                               .                .      .
                           .                 *                 .                *                ` -
   .      .*                                                                                        .             .              .       .
          .    .         .      .                                      .
     .                                               .-o
                                         .           /  |
           .      .             .                 . /   |   .      .        .       .         .           .          .        *        .
                                                   /    |
   .    .          .                      .       /     |     .                .           .         .          ..                           .
                          .                      /      /         .
           .       .                 .          /    _./   .
                                           _.---~-.=:_                    +            .                         .           .    
                                          (_.-=() <~`-`-.
    .   .     .        .                 _/ _() ~`-==-._,>  .       .                              .       -o-       .                     .
                                 ..--====--' `~-._.__()
           *       .         o===''~~             |__()
                                        .         \   |             .   .          .      .           . *                     .               .
 .   .                                          \  \
                                                    \  \     .
.   .         .                 .                    \  \              .                 .                .         .              .        .
                                         .            \  \         Imperial Shuttle         .                              .
           .        .                                  \_ \        .
                                                         ~o         .                              .                    +       .
                  +                    .       .                   
                   .           .                        
    .                                              .             .              .                                .                               
       .                                                  
                               
         
  """)
    
def star_destroyer6():
    print("""
            
                
                                                  _        .                          .            (
                   .        .                    (_)        .       .                                     .             .        .                .
    .      .  .                   .        ____.--^.
                                   .      /:  /    |                               +           .         .          .
            .  .     .    .              /:  `--=--'   .                                                .            *             .                  .
                                        /: __[\==`-.___          *           .
   .     .                             /__|\ _~~~~~~   ~~--..__            .             .
                   .       .           \   \|::::|-----.....___|~--.                                 .                      -o-               .
          .      .                      \ _\_~~~~~-----:|:::______//---...___
                   +                .   [\  \  __  --     \       ~  \_      ~~~===------==-...____
                                        [============================================================-
        .            .      .           /         __/__   --  /__    --       /____....----''''~~~~      .                .          .                .
                                  *    /  /   ==           ____....=---='''~~~~ .
  .  .    .                         /____....--=-''':~~~~                      .                .
                   .     .            .       ~--~                                 Star Destroyer               .           .                    .   
             .    .                                    .                                   .           .
  .    .                                                    .                      .             +
                  .   .                 .     +              .                                       <=>       .                      .
            .    .                                                               .                .      .
   .    .                            .                 *                 .                *                ` -
           .      .*                                                                                        .             .              .       .
                  .    .         .      .                                      .
             .                                               .-o
      .  .                                       .           /  |
                   .      .             .                 . /   |   .      .        .       .         .           .          .        *        .
                                                           /    |
   .       .    .          .                      .       /     |     .                .           .         .          ..                           .
                                  .                      /      /         .
       .           .       .                 .          /    _./   .
                                                   _.---~-.=:_                    +            .                         .           .    
     +                                            (_.-=() <~`-`-.
            .   .     .        .                 _/ _() ~`-==-._,>  .       .                              .       -o-       .                     .
                                         ..--====--' `~-._.__()
                   *       .         o===''~~             |__()
                                                .         \   |             .   .          .      .           . *                     .               .
         .   .                                          \  \
                                                            \  \     .
        .   .         .                 .                    \  \              .                 .                .         .              .        .
                                                 .            \  \         Imperial Shuttle         .                              .
                   .        .                                  \_ \        .
                                                                 ~o         .                              .                    +       .
  .                        +                    .       .                   
    .                       .           .                        
            .                                              .             .              .                                .                               
               .                                                  
                                       
         
  """)
    
def falcon():
    
    print("""
    
    
                    c==o
              _/____\_
       _.,--'" ||^ || "`z._
      /_/^ ___\||  || _/o\ "`-._
    _/  ]. L_| || .||  \_/_  . _`--._
   /_~7  _ . " ||. || /] \ ]. (_)  . "`--.
  |__7~.(_)_ []|+--+|/____T_____________L|
  |__|  _^(_) /^   __\____ _   _|
  |__| (_){_) J ]K{__ L___ _   _]
  |__| . _(_) \v     /__________|________
  l__l_ (_). []|+-+-<\^   L  . _   - ---L|
   \__\    __. ||^l  \Y] /_]  (_) .  _,--'
     \~_]  L_| || .\ .\\/~.    _,--'"
      \_\ . __/||  |\  \`-+-<'"
        "`---._|J__L|X o~~|[\\      "Millenium Falcon"
               \____/ \___|[//      
                `--'   `--+-'
    
    
    """)
    
def rebel_ships():
    
    print("""

         .             .                            .                .
             ________                          
           =[________]========-------[]<--        *                     .                        .             *
             |  ___ |
  .          |==|  || .          .          .             .     .
             |==| _| |                                                    .                .                         .
    .        |==||   |
             |  ||   |         .              .          .       .                  .              .           .           .
   .    .    |  ||    |     .    .   .    .  *           .
             |  ~~    |                          +
      .      |________|    .           .         .          .              *                           .         .         .
           __L________\_                                                                         
          <_|_L___/   | |,        .          .          .             .     .           .       -o-         .            . 
 .     .     |__\_____|_|___
            /L___________   `---._________                                                            .          .         . 
           | | .----. _  |---v--.______ _ `-------------.--.__      X-Wing Starfighter 
          [| | |    |(_) |]__[_____]____________________]__ __]      .             .     . .                    .  
           | |___________|---^--'_________.-------------`--'
  *  .      \L______________.---'           .                              .                            +  .            .
           __|__/_    | |
          <_|_L___\___|_|'         .                   .                         .              . .                  .       .
   .         L________/ 
             |        |         *           .                     + .     .              .                    .                  .
             |   _    |
    +    .   |  ||    |        .                     .        .             .
             |  ||   |
             |==||_  |                     .                       .              .                   .              .
 .    .      |==|  | |      .                                              
             |==|__||                                   *              .               +                 .           
     .      |______|
           =[________]========-------[]<--        .                           
   .                                                                       .                     .                *
            .                    .                             .

    """)
    

lightDict = {"Luk Skajvoker": "90", "Obi Van Kenobi": "90", "Joda": "90", "Mace Windu": "70", "Kui Gon Džin": "60", "Princeza Lea": "50"}
darkDict = {"Dart Vejder": "90", "Dart Sidijus": "90", "Dart Mol": "90", "Kajlo Ren": "80", "General Grivijus": "50", "Kaunt Duku": "60", }

darthVader = 90
kyloRen = 80
darthMol = 70
generalGrivius = 60
kauntDuku = 70
darthSidius = 80
luk = 90
obiVan= 90
joda= 90
maceWindu = 70
lea = 50
quiGonJinn = 60   

if __name__ == '__main__':
    main()

