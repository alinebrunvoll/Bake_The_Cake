import time
import sys
import os

a = [ "a", "A",]
b = [ "b", "B" ]
y = ["yes", "y",'yees', 'yeees' 'yep', 'yup', 'ya', 'ja', 'of course', 'ye', 'yas', 'mhm', 'jepp', 'ofc', 'affirmative', 'positive', 'oui', 'sure', 'i guess', 'fine', 'Yes please, thank you very much', 'aggressive yes', 'definitely', 'why not', 'ok', 'okey', 'okay', 'yes.', 'yep.', 'yes!', 'yes?']

name = ''
bakery = ''

def cont1():
    c = input('\n                Press ENTER to continue ( ⌒ ▽ ⌒ )☞ ')
    for i in c:
        return

def cont():
    c = input('\n                ')
    for i in c:
        return

def game_start():
    global name
    global bakery

    print("""\n
 ___                ___                     ___       ___                                      ___                   ___
(   )              (   )                   (   )     (   )                                    (   )                 (   )
 | |.-.     .---.   | |   ___     .--.      | |_      | | .-.     .--.       .--.      .---.   | |   ___     .--.    | |
 | /   \\   / .-, \\  | |  (   )   /    \\    (   __)    | |/   \\   /    \\     /    \\    / .-, \\  | |  (   )   /    \\   | |
 |  .-. | (__) ; |  | |  ' /    |  .-. ;    | |       |  .-. .  |  .-. ;   |  .-. ;  (__) ; |  | |  ' /    |  .-. ;  | |
 | |  | |   .'`  |  | |,' /     |  | | |    | | ___   | |  | |  |  | | |   |  |(___)   .'`  |  | |,' /     |  | | |  | |
 | |  | |  / .'| |  | .  '.     |  |/  |    | |(   )  | |  | |  |  |/  |   |  |       / .'| |  | .  '.     |  |/  |  | |
 | |  | | | /  | |  | | `. \\    |  ' _.'    | | | |   | |  | |  |  ' _.'   |  | ___  | /  | |  | | `. \\    |  ' _.'  | |
 | '  | | ; |  ; |  | |   \\ \\   |  .'.-.    | ' | |   | |  | |  |  .'.-.   |  '(   ) ; |  ; |  | |   \\ \\   |  .'.-.  |_|
 ' `-' ;  ' `-'  |  | |    \\ .  '  `-' /    ' `-' ;   | |  | |  '  `-' /   '  `-' |  ' `-'  |  | |    \\ .  '  `-' /  .-.
  `.__.   `.__.'_. (___ ) (___)  `.__.'      `.__.   (___)(___)  `.__.'     `.__,'   `.__.'_. (___ ) (___)  `.__.'  (   )
                                                                                                                     '-'
""")
    cont1()
    os.system('clear')

    print ("""
                    Welcome to BAKE THE CAKE!
            You are a chef facing the threat of bankruptcy!! >_<"
            To save your business you must create a cake that makes your customer
            CRY WITH HAPPINESS!!!!!


                    Good luck!\n\n""")
    cont1()
    os.system('clear')

    print ("        Before we get started, please enter your chef name!")
    name = input("\n                >>> ")
    os.system('clear')

    print ('\n        '+ name + "! What a great name!")
    print ("        Now please enter the name of your bakery!")
    bakery = input("                >>> ")
    os.system('clear')

    print ("\n        Ok, "+ name + "! \n        Let's get baking!!! :3")
    cont1()
    os.system('clear')

    print ('''
                                                         ___                            ___
                                                        (   )                          (   )
  .--.     .---.   ___ .-. .-.     .--.         .--.     | |_       .---.   ___ .-.     | |_
 /    \\   / .-, \\ (   )   '   \\   /    \\      /  _  \\   (   __)    / .-, \\ (   )   \\   (   __)
;  ,-. ' (__) ; |  |  .-.  .-. ; |  .-. ;    . .' `. ;   | |      (__) ; |  | ' .-. ;   | |
| |  | |   .'`  |  | |  | |  | | |  | | |    | '   | |   | | ___    .'`  |  |  / (___)  | | ___
| |  | |  / .'| |  | |  | |  | | |  |/  |    _\\_`.(___)  | |(   )  / .'| |  | |         | |(   )
| |  | | | /  | |  | |  | |  | | |  ' _.'   (   ). '.    | | | |  | /  | |  | |         | | | |
| '  | | ; |  ; |  | |  | |  | | |  .'.-.    | |  `\\ |   | ' | |  ; |  ; |  | |         | ' | |
'  `-' | ' `-'  |  | |  | |  | | '  `-' /    ; '._,' '   ' `-' ;  ' `-'  |  | |         ' `-' ;
 `.__. | `.__.'_. (___)(___)(___) `.__.'      '.___.'     `.__.   `.__.'_. (___)         `.__.
 ( `-' ;
  `.__.                                                                                        ''')
    cont1()
    os.system('clear')

    print ("        The once famous "+ name + " is standing in the kitchen of "+ bakery + ", their beloved pastry store.")
    cont()
    print ("        Suddenly, the bell rings, and a customer enters! "+ name + " hurries over to the counter.")
    cont()
    print ("        What will "+ name + " do???")
    print ("""
                    a: Tell the customer that the bakery is closed due to imminent bankruptcy
                    b: Ask the customer what they would like today""")

    choice0 = input("\n               >>> ")

    if choice0 in a:
        os.system('clear')
        print ("\n        The customer leaves and "+ bakery + " immediately goes bankrupt. \n\n")
        cont()
        os.system('clear')
        print("""
          /$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$$        /$$$$$$  /$$    /$$ /$$$$$$$$ /$$$$$$$
         /$$__  $$ /$$__  $$| $$$    /$$$| $$_____/       /$$__  $$| $$   | $$| $$_____/| $$__  $$
        | $$  \\__/| $$  \\ $$| $$$$  /$$$$| $$            | $$  \\ $$| $$   | $$| $$      | $$  \\ $$
        | $$ /$$$$| $$$$$$$$| $$ $$/$$ $$| $$$$$         | $$  | $$|  $$ / $$/| $$$$$   | $$$$$$$/
        | $$|_  $$| $$__  $$| $$  $$$| $$| $$__/         | $$  | $$ \\  $$ $$/ | $$__/   | $$__  $$
        | $$  \\ $$| $$  | $$| $$\\  $ | $$| $$            | $$  | $$  \\  $$$/  | $$      | $$  \\ $$
        |  $$$$$$/| $$  | $$| $$ \\/  | $$| $$$$$$$$      |  $$$$$$/   \\  $/   | $$$$$$$$| $$  | $$
         \\______/ |__/  |__/|__/     |__/|________/       \\______/     \\_/    |________/|__/  |__/
        """)
        cont()
        os.system('clear')
    elif choice0 in b:
        egg()
    else:
        os.system('clear')
        print ("\n        You can't fucking write."+ name + " does nothing. \n        The customer leaves and "+ bakery + " immediately goes bankrupt.\n \n                - - - YOU LOSE - - -\n\n\n")
        cont()
        os.system('clear')

def egg():

    os.system('clear')
    print ("\n        The customer asks for the SPECIAL. "+ name + " enters the kitchen again.")
    cont()
    print ("\n        There is a rotten egg and a fresh egg on the counter. \n        What will "+ name + " do?????")
    print ("""
                    a: Take the fresh egg
                    b: Take the rotten egg""")

    choice1 = input("\n                >>> ")

    if choice1 in a:
        _a()
    elif choice1 in b:
        _b()
    else:
        os.system('clear')
        print ("\n        Nothing happens. The customer leaves. "+ bakery + " is bankrupt. \n \n")
        cont()
        os.system('clear')
        print("""
          /$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$$        /$$$$$$  /$$    /$$ /$$$$$$$$ /$$$$$$$
         /$$__  $$ /$$__  $$| $$$    /$$$| $$_____/       /$$__  $$| $$   | $$| $$_____/| $$__  $$
        | $$  \\__/| $$  \\ $$| $$$$  /$$$$| $$            | $$  \\ $$| $$   | $$| $$      | $$  \\ $$
        | $$ /$$$$| $$$$$$$$| $$ $$/$$ $$| $$$$$         | $$  | $$|  $$ / $$/| $$$$$   | $$$$$$$/
        | $$|_  $$| $$__  $$| $$  $$$| $$| $$__/         | $$  | $$ \\  $$ $$/ | $$__/   | $$__  $$
        | $$  \\ $$| $$  | $$| $$\\  $ | $$| $$            | $$  | $$  \\  $$$/  | $$      | $$  \\ $$
        |  $$$$$$/| $$  | $$| $$ \\/  | $$| $$$$$$$$      |  $$$$$$/   \\  $/   | $$$$$$$$| $$  | $$
         \\______/ |__/  |__/|__/     |__/|________/       \\______/     \\_/    |________/|__/  |__/
        """)
        cont()
        os.system('clear')

def _a():
    global name
    global bakery
    os.system('clear')
    print ( '\n        '+ name + " picks up the fresh egg and a baking bowl.\n        The egg cracks open with a wonderful sound. ")
    cont()
    print ( '\n        '+ name + " is reminded of their love for baking that helped them through the rough beginnings of the bakery.")
    cont()
    print ( '\n        '+ name + " smiles peacefully.")
    cont()
    os.system('clear')

    print ("\n\n\n        There is a bag of flour and a bag of dirt in the cupboard. Which one will "+ name + " use?")
    print ("""
                    a: the dirt
                    b: the flour""")

    choice = input("\n        >>>")

    if choice in a:
        aa()
    elif choice in b:
        ab()
    else:
        os.system('clear')
        print ("\n        Unable to decide, "+ name + " is left standing frozen, and the customer leaves the bakery. \n \n" )
        cont()
        os.system('clear')
        print("""
          /$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$$        /$$$$$$  /$$    /$$ /$$$$$$$$ /$$$$$$$
         /$$__  $$ /$$__  $$| $$$    /$$$| $$_____/       /$$__  $$| $$   | $$| $$_____/| $$__  $$
        | $$  \\__/| $$  \\ $$| $$$$  /$$$$| $$            | $$  \\ $$| $$   | $$| $$      | $$  \\ $$
        | $$ /$$$$| $$$$$$$$| $$ $$/$$ $$| $$$$$         | $$  | $$|  $$ / $$/| $$$$$   | $$$$$$$/
        | $$|_  $$| $$__  $$| $$  $$$| $$| $$__/         | $$  | $$ \\  $$ $$/ | $$__/   | $$__  $$
        | $$  \\ $$| $$  | $$| $$\\  $ | $$| $$            | $$  | $$  \\  $$$/  | $$      | $$  \\ $$
        |  $$$$$$/| $$  | $$| $$ \\/  | $$| $$$$$$$$      |  $$$$$$/   \\  $/   | $$$$$$$$| $$  | $$
         \\______/ |__/  |__/|__/     |__/|________/       \\______/     \\_/    |________/|__/  |__/
        """)
        cont()
        os.system('clear')

def _b():
    global name
    global bakery
    os.system('clear')
    print ('\n        '+ name + " picks up the rotten egg and puts it in a baking bowl.")
    cont()
    print (f"""\n        The egg cracks open with a disgusting splat.
        {name} is reminded of how stressful and scary it was to start their own bakery. """)
    print ('\n        '+ name + "'s eyes begin to fill with tears.")
    cont()
    os.system('clear')

    print ("\n\n        There is a bag of flour and a bag of dirt in the cupboard. Which one will "+ name + " use?")
    print ("""
                    a: the dirt
                    b: the flour""")

    choice = input("        >>>")

    if choice in a:
        ba()
    elif choice in b:
        bb()
    else:
        os.system('clear')
        print ("\n        Unable to decide, "+ name + " is left standing frozen, and the customer leaves the bakery. \n \n")
        cont()
        os.system('clear')
        print("""
          /$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$$        /$$$$$$  /$$    /$$ /$$$$$$$$ /$$$$$$$
         /$$__  $$ /$$__  $$| $$$    /$$$| $$_____/       /$$__  $$| $$   | $$| $$_____/| $$__  $$
        | $$  \\__/| $$  \\ $$| $$$$  /$$$$| $$            | $$  \\ $$| $$   | $$| $$      | $$  \\ $$
        | $$ /$$$$| $$$$$$$$| $$ $$/$$ $$| $$$$$         | $$  | $$|  $$ / $$/| $$$$$   | $$$$$$$/
        | $$|_  $$| $$__  $$| $$  $$$| $$| $$__/         | $$  | $$ \\  $$ $$/ | $$__/   | $$__  $$
        | $$  \\ $$| $$  | $$| $$\\  $ | $$| $$            | $$  | $$  \\  $$$/  | $$      | $$  \\ $$
        |  $$$$$$/| $$  | $$| $$ \\/  | $$| $$$$$$$$      |  $$$$$$/   \\  $/   | $$$$$$$$| $$  | $$
         \\______/ |__/  |__/|__/     |__/|________/       \\______/     \\_/    |________/|__/  |__/
        """)
        cont()
        os.system('clear')

def aa():

    os.system('clear')
    print ('\n        '+ name + " dumps the dirt into the bowl. It smells questionable.")
    cont()
    print (f"""        The slightly gross batter reminds {name} that life can be a pile of dirt sometimes.
    {name} is no longer smiling as they present the cake to the customer.""")
    cont()
    view = input('        VIEW CAKE? (input yes/no)\n        >>> ')
    if view in y:
        print("""

                __....----''\\./ ````` `````----....__
          _-'''                                         ```-_
        .'                   ( ˵ ◐ ︿ ◐ ˵ )                   `.
        |`-_                                               _-'|
        |   ```--....____                     ____....--'''   |
        |                `````-----------'''''                |
        |-__                                               __-|
        |   ~~~--________                     ________--~~~   |
        |                ~~~~~-----------~~~~~                |
        |-__                                               __-|
        |   ~~~--________                     ________--~~~   |
        |                ~~~~~-----------~~~~~                |
         `-_                                               _-'
            ```--....____                     ____....--'''
                         `````-----------'''''
    """)
    print ("        The customer seems decently happy with the cake.")
    cont()
    print ("\n        Thanks to the customer, "+ bakery + " will not go bankrupt today. "+ name + " goes to bed, hoping that tomorrow will be a better day.")
    cont()
    os.system('clear')
    print ("""
  _______ _    _ ______   ______ _   _ _____
 |__   __| |  | |  ____| |  ____| \\ | |  __ \\
    | |  | |__| | |__    | |__  |  \\| | |  | |
    | |  |  __  |  __|   |  __| | . ` | |  | |
    | |  | |  | | |____  | |____| |\\  | |__| |
    |_|  |_|  |_|______| |______|_| \\_|_____/
    """)
    cont()
    os.system('clear')

def ab():

    os.system('clear')
    print ('        '+ name + " dumps a nice amount of flour into the cake batter. It smells lovely.")
    cont()
    print ('        '+ name + " is grinning from ear to ear as they present the cake to the customer. The customer's eyes fill up with tears of joy.")
    view = input('\n\n        VIEW CAKE?(input yes/no)\n        >>>')
    if view in y:
        print("""
                  *                                             *
                                               *
                    *
                                  *
                                                            *
         *
                                                  *
             *
                           *             *
                                                     *
      *                                                               *
               *
                               (             )
                       )      (*)           (*)      (
              *       (*)      |             |      (*)
                       |      |~|           |~|      |          *
                      |~|     | |           | |     |~|
                      | |     | |           | |     | |
                     ,| |a@@@@| |@@@@@@@@@@@| |@@@@a| |.
                .,a@@@| |@@@@@| |@@@@@@@@@@@| |@@@@@| |@@@@a,.
              ,a@@@@@@| |@@@@@@@@@@@@.@@@@@@@@@@@@@@| |@@@@@@@a,
             a@@@@@@@@@@@@@@@@@@@@@' . `@@@@@@@@@@@@@@@@@@@@@@@@a
             ;`@@@@@@@@@@@@@@@@@@'   .   `@@@@@@@@@@@@@@@@@@@@@';
             ;@@@`@@@@@@@@@@@@@'     .     `@@@@@@@@@@@@@@@@'@@@;
             ;@@@;,.aaaaaaaaaa       .       aaaaa,,aaaaaaa,;@@@;
             ;;@;;;;@@@@@@@@;@      @.@      ;@@@;;;@@@@@@;;;;@@;
             ;;;;;;;@@@@;@@;;@    @@ . @@    ;;@;;;;@@;@@@;;;;;;;
             ;;;;;;;;@@;;;;;;;  @@   .   @@  ;;;;;;;;;;;@@;;;;@;;
             ;;;;;;;;;;;;;;;;;@@     .     @@;;;;;;;;;;;;;;;;@@@;
         ,%%%;;;;;;;;@;;;;;;;;       .       ;;;;;;;;;;;;;;;;@@;;%%%,
      .%%%%%%;;;;;;;@@;;;;;;;;     ,%%%,     ;;;;;;;;;;;;;;;;;;;;%%%%%%,
     .%%%%%%%;;;;;;;@@;;;;;;;;   ,%%%%%%%,   ;;;;;;;;;;;;;;;;;;;;%%%%%%%,
     %%%%%%%%`;;;;;;;;;;;;;;;;  %%%%%%%%%%%  ;;;;;;;;;;;;;;;;;;;'%%%%%%%%
     %%%%%%%%%%%%`;;;;;;;;;;;;,%%%%%%%%%%%%%,;;;;;;;;;;;;;;;'%%%%%%%%%%%%
     `%%%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%%%%%%'
       `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
           `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
                  """"""""""""""`,,,,,,,,,'""""""""""""""\"\"\"


        """)
    cont()
    os.system('clear')
    print("        Thanks to the love of the happy customer, "+ bakery + " is no longer going bankrupt! (❁´▽`❁)ﾉ*:・ﾟ✧")
    cont()
    print ("""
   ____     __   ,-----.      ___    _         .--.      .--..-./`) ,---.   .--. .---.  .---.  .---.
   \\   \\   /  /.'  .-,  '.  .'   |  | |        |  |_     |  |\\ .-.')|    \\  |  | \\   /  \\   /  \\   /
    \\  _. /  '/ ,-.|  \\ _ \\ |   .'  | |        | _( )_   |  |/ `-' \\|  ,  \\ |  | |   |  |   |  |   |
     _( )_ .';  \\  '_ /  | :.'  '_  | |        |(_ o _)  |  | `-'`"`|  |\\_ \\|  |  \\ /    \\ /    \\ /
 ___(_ o _)' |  _`,/ \ _/  |'   ( \\.-.|        | (_,_) \\ |  | .---. |  _( )_\\  |   v      v      v
|   |(_,_)'  : (  '\\_/ \\   ;' (`. _` /|        |  |/    \\|  | |   | | (_ o _)  |  _ _    _ _    _ _
|   `-'  /    \\ `"/  \\  ) / | (_ (_) _)        |  '  /\\  `  | |   | |  (_,_)\\  | (_I_)  (_I_)  (_I_)
 \\      /      '. \\_/``".'   \\ /  . \\ /        |    /  \\    | |   | |  |    |  |(_(=)_)(_(=)_)(_(=)_)
  `-..-'         '-----'      ``-'`-''         `---'    `---` '---' '--'    '--' (_I_)  (_I_)  (_I_)
    """)
    cont()
    os.system('clear')

def ba():
    os.system('clear')
    print ('        '+ name + " dumps the dirt into the bowl. It smells horrible.")
    cont()
    print ("\n        The gross batter reminds "+ name + " that life is a pile of crap.")
    cont()
    view = input("        VIEW CAKE?(input yes/no)\n                >>> ")
    if view in y:
        print("""
     )   (    )
  (    ___  (
    _.'   `._  )
  .' ´༎ຶ ㅂ ༎ຶ` `.
_(_____________)___
        """)
    cont()
    print ('        '+ name + " is sobbing as they present the cake to the customer. The customer hates the cake and starts crying.")
    cont()
    print ('\n        '+ bakery + " immediatly goes bankrupt.")
    cont()
    os.system('clear')
    print ( """
▓██   ██▓ ▒█████   █    ██     ██▓     ▒█████    ██████ ▓█████
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓██▒    ▒██▒  ██▒▒██    ▒ ▓█   ▀
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒██░    ▒██░  ██▒░ ▓██▄   ▒███
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ▒██░    ▒██   ██░  ▒   ██▒▒▓█  ▄
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░██████▒░ ████▓▒░▒██████▒▒░▒████▒
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░░ ▒░ ░
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░    ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░ ░ ░  ░
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░ ░   ░ ░ ░ ▒  ░  ░  ░     ░
 ░ ░         ░ ░     ░            ░  ░    ░ ░        ░     ░  ░
 ░ ░

                                                              """)
    cont()
    os.system('clear')

def bb():

    os.system('clear')
    print ('        '+ name + " dumps a nice amount of flour into the cake batter. It smells okay.")
    cont()
    print (f"""        The sight of the flour reminds {name} of their love of baking.
    {name} dries their eyes and nods determined as they present the cake to the customer.""")
    cont()
    view = input('        VIEW CAKE?(input yes/no)\n                >>> ')
    if view in y:
        print("""

                    __....----''\\./ ````` `````----....__
              _-'''                                         ```-_
            .'                   (  ● ﹏ ● ')                    `.
            |`-_                                               _-'|
            |   ```--....____                     ____....--'''   |
            |                `````-----------'''''                |
            |-__                                               __-|
            |   ~~~--________                     ________--~~~   |
            |                ~~~~~-----------~~~~~                |
            |-__                                               __-|
            |   ~~~--________                     ________--~~~   |
            |                ~~~~~-----------~~~~~                |
             `-_                                               _-'
                ```--....____                     ____....--'''
                             `````-----------'''''
        """)
    print ("        The customer seems decently happy with the cake.")
    print (f"""\n        Thanks to the customer, {bakery} will not go bankrupt today.
    {name} goes to bed, hoping that tomorrow will be a better day.""")
    cont()
    os.system('clear')
    print ("""
  _______ _    _ ______   ______ _   _ _____
 |__   __| |  | |  ____| |  ____| \\ | |  __ \\
    | |  | |__| | |__    | |__  |  \\| | |  | |
    | |  |  __  |  __|   |  __| | . ` | |  | |
    | |  | |  | | |____  | |____| |\\  | |__| |
    |_|  |_|  |_|______| |______|_| \\_|_____/
    """)
    cont()
    os.system('clear')


game_start()
