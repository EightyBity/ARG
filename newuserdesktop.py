import sys
import time
import random

import game
import cls
import help
import wyvern_orders
import mission1
import wyvern1
import usr

def desk():
    cls.cls()
    user ='''
$$\      $$\ $$\     $$\ $$\    $$\ $$$$$$$$\ $$$$$$$\  $$\   $$\       $$$$$$$\  $$$$$$\ $$\        $$$$$$\  $$$$$$$$\ 
$$ | $\  $$ |\$$\   $$  |$$ |   $$ |$$  _____|$$  __$$\ $$$\  $$ |      $$  __$$\ \_$$  _|$$ |      $$  __$$\ \__$$  __|
$$ |$$$\ $$ | \$$\ $$  / $$ |   $$ |$$ |      $$ |  $$ |$$$$\ $$ |      $$ |  $$ |  $$ |  $$ |      $$ /  $$ |   $$ |   
$$ $$ $$\$$ |  \$$$$  /  \$$\  $$  |$$$$$\    $$$$$$$  |$$ $$\$$ |      $$$$$$$  |  $$ |  $$ |      $$ |  $$ |   $$ |   
$$$$  _$$$$ |   \$$  /    \$$\$$  / $$  __|   $$  __$$< $$ \$$$$ |      $$  ____/   $$ |  $$ |      $$ |  $$ |   $$ |   
$$$  / \$$$ |    $$ |      \$$$  /  $$ |      $$ |  $$ |$$ |\$$$ |      $$ |        $$ |  $$ |      $$ |  $$ |   $$ |   
$$  /   \$$ |    $$ |       \$  /   $$$$$$$$\ $$ |  $$ |$$ | \$$ |      $$ |      $$$$$$\ $$$$$$$$\  $$$$$$  |   $$ |   
\__/     \__|    \__|        \_/    \________|\__|  \__|\__|  \__|      \__|      \______|\________| \______/    \__|   
                                                                                                                        
                                                                                                                        
                                                                                                                        

'''
    for character in user:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.005)
    warning = 'files have been saved on this desktop, do you wish to recover them?(y/n)'
    for character in warning:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player = input()
    if player.lower().strip() in ['y','yes']:
         userScreen()
    elif player.lower().strip() in ['n', 'no']:
        cls.cls()
        print('''
$$\      $$\ $$\     $$\ $$\    $$\ $$$$$$$$\ $$$$$$$\  $$\   $$\       $$$$$$$\  $$$$$$\ $$\        $$$$$$\  $$$$$$$$\ 
$$ | $\  $$ |\$$\   $$  |$$ |   $$ |$$  _____|$$  __$$\ $$$\  $$ |      $$  __$$\ \_$$  _|$$ |      $$  __$$\ \__$$  __|
$$ |$$$\ $$ | \$$\ $$  / $$ |   $$ |$$ |      $$ |  $$ |$$$$\ $$ |      $$ |  $$ |  $$ |  $$ |      $$ /  $$ |   $$ |   
$$ $$ $$\$$ |  \$$$$  /  \$$\  $$  |$$$$$\    $$$$$$$  |$$ $$\$$ |      $$$$$$$  |  $$ |  $$ |      $$ |  $$ |   $$ |   
$$$$  _$$$$ |   \$$  /    \$$\$$  / $$  __|   $$  __$$< $$ \$$$$ |      $$  ____/   $$ |  $$ |      $$ |  $$ |   $$ |   
$$$  / \$$$ |    $$ |      \$$$  /  $$ |      $$ |  $$ |$$ |\$$$ |      $$ |        $$ |  $$ |      $$ |  $$ |   $$ |   
$$  /   \$$ |    $$ |       \$  /   $$$$$$$$\ $$ |  $$ |$$ | \$$ |      $$ |      $$$$$$\ $$$$$$$$\  $$$$$$  |   $$ |   
\__/     \__|    \__|        \_/    \________|\__|  \__|\__|  \__|      \__|      \______|\________| \______/    \__|   
                                                                                                                        
                                                                                                                        
usr                                                                                                                        

''')
        player = input('''type help for help
''')
        if player.lower().startswith('cd') or player.lower().startswith('cat'):
            cls.cls()
            print('''
$$\      $$\ $$\     $$\ $$\    $$\ $$$$$$$$\ $$$$$$$\  $$\   $$\       $$$$$$$\  $$$$$$\ $$\        $$$$$$\  $$$$$$$$\ 
$$ | $\  $$ |\$$\   $$  |$$ |   $$ |$$  _____|$$  __$$\ $$$\  $$ |      $$  __$$\ \_$$  _|$$ |      $$  __$$\ \__$$  __|
$$ |$$$\ $$ | \$$\ $$  / $$ |   $$ |$$ |      $$ |  $$ |$$$$\ $$ |      $$ |  $$ |  $$ |  $$ |      $$ /  $$ |   $$ |   
$$ $$ $$\$$ |  \$$$$  /  \$$\  $$  |$$$$$\    $$$$$$$  |$$ $$\$$ |      $$$$$$$  |  $$ |  $$ |      $$ |  $$ |   $$ |   
$$$$  _$$$$ |   \$$  /    \$$\$$  / $$  __|   $$  __$$< $$ \$$$$ |      $$  ____/   $$ |  $$ |      $$ |  $$ |   $$ |   
$$$  / \$$$ |    $$ |      \$$$  /  $$ |      $$ |  $$ |$$ |\$$$ |      $$ |        $$ |  $$ |      $$ |  $$ |   $$ |   
$$  /   \$$ |    $$ |       \$  /   $$$$$$$$\ $$ |  $$ |$$ | \$$ |      $$ |      $$$$$$\ $$$$$$$$\  $$$$$$  |   $$ |   
\__/     \__|    \__|        \_/    \________|\__|  \__|\__|  \__|      \__|      \______|\________| \______/    \__|   
                                                                                                                        
                                                                                                                        
usr                                                                                                                        

Corruption too advanced, type back to go back
''')
        elif player.lower().strip() == 'back':
            game.Game()
        elif player.lower().strip() in ['h','help']:
            help.help()
        else:
            cls.cls()
            print('''
$$\      $$\ $$\     $$\ $$\    $$\ $$$$$$$$\ $$$$$$$\  $$\   $$\       $$$$$$$\  $$$$$$\ $$\        $$$$$$\  $$$$$$$$\ 
$$ | $\  $$ |\$$\   $$  |$$ |   $$ |$$  _____|$$  __$$\ $$$\  $$ |      $$  __$$\ \_$$  _|$$ |      $$  __$$\ \__$$  __|
$$ |$$$\ $$ | \$$\ $$  / $$ |   $$ |$$ |      $$ |  $$ |$$$$\ $$ |      $$ |  $$ |  $$ |  $$ |      $$ /  $$ |   $$ |   
$$ $$ $$\$$ |  \$$$$  /  \$$\  $$  |$$$$$\    $$$$$$$  |$$ $$\$$ |      $$$$$$$  |  $$ |  $$ |      $$ |  $$ |   $$ |   
$$$$  _$$$$ |   \$$  /    \$$\$$  / $$  __|   $$  __$$< $$ \$$$$ |      $$  ____/   $$ |  $$ |      $$ |  $$ |   $$ |   
$$$  / \$$$ |    $$ |      \$$$  /  $$ |      $$ |  $$ |$$ |\$$$ |      $$ |        $$ |  $$ |      $$ |  $$ |   $$ |   
$$  /   \$$ |    $$ |       \$  /   $$$$$$$$\ $$ |  $$ |$$ | \$$ |      $$ |      $$$$$$\ $$$$$$$$\  $$$$$$  |   $$ |   
\__/     \__|    \__|        \_/    \________|\__|  \__|\__|  \__|      \__|      \______|\________| \______/    \__|   
                                                                                                                        
                                                                                                                        
usr                                                                                                                        

Sorry I did not understand type help for help or back to go back
''')                       
        
def userScreen():
    cls.cls()
    print('''
$$\      $$\ $$\     $$\ $$\    $$\ $$$$$$$$\ $$$$$$$\  $$\   $$\       $$$$$$$\  $$$$$$\ $$\        $$$$$$\  $$$$$$$$\ 
$$ | $\  $$ |\$$\   $$  |$$ |   $$ |$$  _____|$$  __$$\ $$$\  $$ |      $$  __$$\ \_$$  _|$$ |      $$  __$$\ \__$$  __|
$$ |$$$\ $$ | \$$\ $$  / $$ |   $$ |$$ |      $$ |  $$ |$$$$\ $$ |      $$ |  $$ |  $$ |  $$ |      $$ /  $$ |   $$ |   
$$ $$ $$\$$ |  \$$$$  /  \$$\  $$  |$$$$$\    $$$$$$$  |$$ $$\$$ |      $$$$$$$  |  $$ |  $$ |      $$ |  $$ |   $$ |   
$$$$  _$$$$ |   \$$  /    \$$\$$  / $$  __|   $$  __$$< $$ \$$$$ |      $$  ____/   $$ |  $$ |      $$ |  $$ |   $$ |   
$$$  / \$$$ |    $$ |      \$$$  /  $$ |      $$ |  $$ |$$ |\$$$ |      $$ |        $$ |  $$ |      $$ |  $$ |   $$ |   
$$  /   \$$ |    $$ |       \$  /   $$$$$$$$\ $$ |  $$ |$$ | \$$ |      $$ |      $$$$$$\ $$$$$$$$\  $$$$$$  |   $$ |   
\__/     \__|    \__|        \_/    \________|\__|  \__|\__|  \__|      \__|      \______|\________| \______/    \__|   
                                                                                                                        
                                                                                                                        
usr     wyvern_orders.txt       wyvern1.txt

mission1.txt

''')
    
    while True:
            player = input('''
type help for help
'''
        )
            if player.lower().strip() in ['h', 'help']:
                help.help()
            elif player.lower().strip().startswith('cat'):
                if player.lower().strip().endswith('wyvern_orders.txt'):
                    wyvern_orders.wyvernOrders()
                elif player.lower().strip().endswith('wyvern1.txt'):
                    wyvern1.wyvern1()
                elif player.lower().strip().endswith('mission1.txt'):
                    mission1.mission1()
                else:
                    cls.cls()
                    print('''
$$\      $$\ $$\     $$\ $$\    $$\ $$$$$$$$\ $$$$$$$\  $$\   $$\       $$$$$$$\  $$$$$$\ $$\        $$$$$$\  $$$$$$$$\ 
$$ | $\  $$ |\$$\   $$  |$$ |   $$ |$$  _____|$$  __$$\ $$$\  $$ |      $$  __$$\ \_$$  _|$$ |      $$  __$$\ \__$$  __|
$$ |$$$\ $$ | \$$\ $$  / $$ |   $$ |$$ |      $$ |  $$ |$$$$\ $$ |      $$ |  $$ |  $$ |  $$ |      $$ /  $$ |   $$ |   
$$ $$ $$\$$ |  \$$$$  /  \$$\  $$  |$$$$$\    $$$$$$$  |$$ $$\$$ |      $$$$$$$  |  $$ |  $$ |      $$ |  $$ |   $$ |   
$$$$  _$$$$ |   \$$  /    \$$\$$  / $$  __|   $$  __$$< $$ \$$$$ |      $$  ____/   $$ |  $$ |      $$ |  $$ |   $$ |   
$$$  / \$$$ |    $$ |      \$$$  /  $$ |      $$ |  $$ |$$ |\$$$ |      $$ |        $$ |  $$ |      $$ |  $$ |   $$ |   
$$  /   \$$ |    $$ |       \$  /   $$$$$$$$\ $$ |  $$ |$$ | \$$ |      $$ |      $$$$$$\ $$$$$$$$\  $$$$$$  |   $$ |   
\__/     \__|    \__|        \_/    \________|\__|  \__|\__|  \__|      \__|      \______|\________| \______/    \__|   
                                                                                                                        
                                                                                                                        
usr     wyvern_orders.txt       wyvern1.txt

mission1.txt

im sorry please make sure the file you are trying to read is a txt extension''')
                    player = input('''type help for help
''')
            elif player.lower().strip().startswith('cd'):
                if player.lower().strip().endswith('.txt'):
                    print('''
$$\      $$\ $$\     $$\ $$\    $$\ $$$$$$$$\ $$$$$$$\  $$\   $$\       $$$$$$$\  $$$$$$\ $$\        $$$$$$\  $$$$$$$$\ 
$$ | $\  $$ |\$$\   $$  |$$ |   $$ |$$  _____|$$  __$$\ $$$\  $$ |      $$  __$$\ \_$$  _|$$ |      $$  __$$\ \__$$  __|
$$ |$$$\ $$ | \$$\ $$  / $$ |   $$ |$$ |      $$ |  $$ |$$$$\ $$ |      $$ |  $$ |  $$ |  $$ |      $$ /  $$ |   $$ |   
$$ $$ $$\$$ |  \$$$$  /  \$$\  $$  |$$$$$\    $$$$$$$  |$$ $$\$$ |      $$$$$$$  |  $$ |  $$ |      $$ |  $$ |   $$ |   
$$$$  _$$$$ |   \$$  /    \$$\$$  / $$  __|   $$  __$$< $$ \$$$$ |      $$  ____/   $$ |  $$ |      $$ |  $$ |   $$ |   
$$$  / \$$$ |    $$ |      \$$$  /  $$ |      $$ |  $$ |$$ |\$$$ |      $$ |        $$ |  $$ |      $$ |  $$ |   $$ |   
$$  /   \$$ |    $$ |       \$  /   $$$$$$$$\ $$ |  $$ |$$ | \$$ |      $$ |      $$$$$$\ $$$$$$$$\  $$$$$$  |   $$ |   
\__/     \__|    \__|        \_/    \________|\__|  \__|\__|  \__|      \__|      \______|\________| \______/    \__|   
                                                                                                                        
                                                                                                                        
usr     wyvern_orders.txt       wyvern1.txt

mission1.txt

directory not found, did you mean to use cat?''')
                    player = input()
                elif player.lower().strip().endswith('usr'):
                    usr.usr()
            elif player.lower().strip() == 'back':
                game.Game()
            else:
                cls.cls()
                print('''
$$\      $$\ $$\     $$\ $$\    $$\ $$$$$$$$\ $$$$$$$\  $$\   $$\       $$$$$$$\  $$$$$$\ $$\        $$$$$$\  $$$$$$$$\ 
$$ | $\  $$ |\$$\   $$  |$$ |   $$ |$$  _____|$$  __$$\ $$$\  $$ |      $$  __$$\ \_$$  _|$$ |      $$  __$$\ \__$$  __|
$$ |$$$\ $$ | \$$\ $$  / $$ |   $$ |$$ |      $$ |  $$ |$$$$\ $$ |      $$ |  $$ |  $$ |  $$ |      $$ /  $$ |   $$ |   
$$ $$ $$\$$ |  \$$$$  /  \$$\  $$  |$$$$$\    $$$$$$$  |$$ $$\$$ |      $$$$$$$  |  $$ |  $$ |      $$ |  $$ |   $$ |   
$$$$  _$$$$ |   \$$  /    \$$\$$  / $$  __|   $$  __$$< $$ \$$$$ |      $$  ____/   $$ |  $$ |      $$ |  $$ |   $$ |   
$$$  / \$$$ |    $$ |      \$$$  /  $$ |      $$ |  $$ |$$ |\$$$ |      $$ |        $$ |  $$ |      $$ |  $$ |   $$ |   
$$  /   \$$ |    $$ |       \$  /   $$$$$$$$\ $$ |  $$ |$$ | \$$ |      $$ |      $$$$$$\ $$$$$$$$\  $$$$$$  |   $$ |   
\__/     \__|    \__|        \_/    \________|\__|  \__|\__|  \__|      \__|      \______|\________| \______/    \__|   
                                                                                                                        
                                                                                                                        
usr     wyvern_orders.txt       wyvern1.txt

mission1.txt

I did not understand please make sure to type the commands correctly''')
                player = input()
    
if __name__ == '__main__':
    desk()