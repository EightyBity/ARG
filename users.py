#!/usr/bin/env python3

#Wyvern squadron os
#project proposed by:Wyvern 3 aka Eighty Bity

import sys
import time

from cls import cls
from wyvern3 import passwordRequired
from newuser import screen1

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
                                                                                                                                                        
''')
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

if __name__=='__main__':
    user()