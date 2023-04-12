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
from cls import cls

def Game():
    cls()
    disclaimer = '''MAKE SURE THE WINDOW IS IN FULLSCREEN OTHERWISE ASCII ART AND OTHER ASSETS MIGHT NOT SHOW PROPERLY
PLEASE DO NOT PRESS ON CTRL+C UNLESS THE PROGRAM NEEDS TO BE CLOSED
WHEN NEEDED A HELP COMMAND WILL BE SHOWN TO GIVE YOU AVAILABLE COMMANDS 
WRITE DOWN I AGREE IF YOU UNDERSTOOD EVERYTHING IN THIS DISCLAIMER'''
    for character in disclaimer:
          sys.stdout.write(character)
          sys.stdout.flush()
          time.sleep(0.05)
    answer=input('''
''')
    if answer.lower().strip()=='i agree':
        cls()
        title = ''' __       __  __      __  __     __  ________  _______   __    __         ______    ______   __    __   ______   _______   _______    ______   __    __ 
/  |  _  /  |/  \    /  |/  |   /  |/        |/       \ /  \  /  |       /      \  /      \ /  |  /  | /      \ /       \ /       \  /      \ /  \  /  |
$$ | / \ $$ |$$  \  /$$/ $$ |   $$ |$$$$$$$$/ $$$$$$$  |$$  \ $$ |      /$$$$$$  |/$$$$$$  |$$ |  $$ |/$$$$$$  |$$$$$$$  |$$$$$$$  |/$$$$$$  |$$  \ $$ |
$$ |/$  \$$ | $$  \/$$/  $$ |   $$ |$$ |__    $$ |__$$ |$$$  \$$ |      $$ \__$$/ $$ |  $$ |$$ |  $$ |$$ |__$$ |$$ |  $$ |$$ |__$$ |$$ |  $$ |$$$  \$$ |
$$ /$$$  $$ |  $$  $$/   $$  \ /$$/ $$    |   $$    $$< $$$$  $$ |      $$      \ $$ |  $$ |$$ |  $$ |$$    $$ |$$ |  $$ |$$    $$< $$ |  $$ |$$$$  $$ |
$$ $$/$$ $$ |   $$$$/     $$  /$$/  $$$$$/    $$$$$$$  |$$ $$ $$ |       $$$$$$  |$$ |_ $$ |$$ |  $$ |$$$$$$$$ |$$ |  $$ |$$$$$$$  |$$ |  $$ |$$ $$ $$ |
$$$$/  $$$$ |    $$ |      $$ $$/   $$ |_____ $$ |  $$ |$$ |$$$$ |      /  \__$$ |$$ / \$$ |$$ \__$$ |$$ |  $$ |$$ |__$$ |$$ |  $$ |$$ \__$$ |$$ |$$$$ |
$$$/    $$$ |    $$ |       $$$/    $$       |$$ |  $$ |$$ | $$$ |      $$    $$/ $$ $$ $$< $$    $$/ $$ |  $$ |$$    $$/ $$ |  $$ |$$    $$/ $$ | $$$ |
$$/      $$/     $$/         $/     $$$$$$$$/ $$/   $$/ $$/   $$/        $$$$$$/   $$$$$$  | $$$$$$/  $$/   $$/ $$$$$$$/  $$/   $$/  $$$$$$/  $$/   $$/ 
                                                                                       $$$/                                                             
                                                                                                                                                        
'''
        for character in title:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.005)
        def user():
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