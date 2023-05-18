import cls
import sys
import time
import os

import newuserdesktop
import help


def usr():
    cls.cls()
    directory = '''Wyvern3      newuser

    
type help for help

'''

    for characters in directory:
        sys.stdout.write(characters)
        sys.stdout.flush()
        time.sleep(0.05)

    while True:
        player = input()
        if player.lower().startswith('cd'):
            if player.lower().endswith('Wyvern3'):
                cls.cls()
                print('''Wyvern3      newuser
    
the directory you are trying to access has been corrupted and can not be accessed
''')
            elif player.lower().endswith('newuser'):
                cls.cls()
                print('''Wyvern3      newuser
    
Why are you trying to access yourself''',os.getlogin(),"\n" )
        elif player.lower().startswith('cat'):
            cls.cls()
            print('''Wyvern3      newuser

    
No text file found, did you mean to use cd?

''')
        elif player.lower().strip() == 'help':
            help.help()
        elif player.lower().strip() == 'back':
            newuserdesktop.userScreen()
if __name__ == '__main__':
    usr()