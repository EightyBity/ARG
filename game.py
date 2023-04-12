#Wyvern squadron os
#project proposed by:Wyvern 3 aka Eighty Bity
import cmd
import textwrap
import sys
import os
import time
import random
from wyvern3 import passwordRequired
from newuser import screen1

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def Game():
    cls()
    disclaimer = '''MAKE SURE THE WINDOW IS IN FULLSCREEN OTHERWISE ASCII ART AND OTHER ASSETS MIGHT NOT SHOW PROPERLY
WRITE DOWN I AGREE WHEN THE SCREEN HAS BEEN PUT IN FULLSCREEN'''
    for character in disclaimer:
          sys.stdout.write(character)
          sys.stdout.flush()
          time.sleep(0.05)
    answer=input('''
''')
    if answer.lower().strip()=='i agree':
        def user():
            cls()
            print(''' __       __  __      __  __     __  ________  _______   __    __         ______    ______   __    __   ______   _______   _______    ______   __    __ 
/  |  _  /  |/  \    /  |/  |   /  |/        |/       \ /  \  /  |       /      \  /      \ /  |  /  | /      \ /       \ /       \  /      \ /  \  /  |
$$ | / \ $$ |$$  \  /$$/ $$ |   $$ |$$$$$$$$/ $$$$$$$  |$$  \ $$ |      /$$$$$$  |/$$$$$$  |$$ |  $$ |/$$$$$$  |$$$$$$$  |$$$$$$$  |/$$$$$$  |$$  \ $$ |
$$ |/$  \$$ | $$  \/$$/  $$ |   $$ |$$ |__    $$ |__$$ |$$$  \$$ |      $$ \__$$/ $$ |  $$ |$$ |  $$ |$$ |__$$ |$$ |  $$ |$$ |__$$ |$$ |  $$ |$$$  \$$ |
$$ /$$$  $$ |  $$  $$/   $$  \ /$$/ $$    |   $$    $$< $$$$  $$ |      $$      \ $$ |  $$ |$$ |  $$ |$$    $$ |$$ |  $$ |$$    $$< $$ |  $$ |$$$$  $$ |
$$ $$/$$ $$ |   $$$$/     $$  /$$/  $$$$$/    $$$$$$$  |$$ $$ $$ |       $$$$$$  |$$ |_ $$ |$$ |  $$ |$$$$$$$$ |$$ |  $$ |$$$$$$$  |$$ |  $$ |$$ $$ $$ |
$$$$/  $$$$ |    $$ |      $$ $$/   $$ |_____ $$ |  $$ |$$ |$$$$ |      /  \__$$ |$$ / \$$ |$$ \__$$ |$$ |  $$ |$$ |__$$ |$$ |  $$ |$$ \__$$ |$$ |$$$$ |
$$$/    $$$ |    $$ |       $$$/    $$       |$$ |  $$ |$$ | $$$ |      $$    $$/ $$ $$ $$< $$    $$/ $$ |  $$ |$$    $$/ $$ |  $$ |$$    $$/ $$ | $$$ |
$$/      $$/     $$/         $/     $$$$$$$$/ $$/   $$/ $$/   $$/        $$$$$$/   $$$$$$  | $$$$$$/  $$/   $$/ $$$$$$$/  $$/   $$/  $$$$$$/  $$/   $$/ 
                                                                                       $$$/                                                             
                                                                                                                                                        
                                                                                                                                                        

username:''')
            usernameFound = 'a username has been found, do you want to use it now?(y/n)'
            for character in usernameFound:
               sys.stdout.write(character)
               sys.stdout.flush()
               time.sleep(0.05)
            use_username=input()
            if use_username.lower().strip() in ['y','yes']:
                cls()
                passwordRequired()
            elif use_username.lower().strip() in ['n','no']:
                cls()
                screen1()

            else:
                cls()
               
                user()
        user()         