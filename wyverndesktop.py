#!/usr/bin/env python3

#Wyvern squadron os
#project proposed by:Wyvern 3 aka Eighty Bity
import sys
import time

from cls import cls
import newuser
import confidential
import userfile
import game
import wyverntxt
import help
import allies
import kos
import orders

def screen():
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
                                                                                                                                                        
Welcome back wyvern 3

Load complete! what should we do?
if this is not you and you simply found the password by accident please type 'back' and alert a wyvern lead as soon as possible

desktop         internet        about''')
     nav()

def nav():
         
         user1 = input()
         if user1.lower().strip()=='desktop':
            desktop()
         elif user1.lower().strip()=='internet':
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
                                                                                                                                                        
Welcome back wyvern 3

You do not seem to be connected please make another selection

desktop         internet        about''')
            nav()
         elif user1.lower().strip()=='about':
            cls()
            about = '''The Wyvern Squadron os is a project started by wyvern lead arrax eturnal for the purpose of training in cyber defense
the os has been designed by wyvern 3 aka Eighty_Bity in the hopes the squadron could use it to their advantage
current status of the os is unknown but some functionalities have been restored including a desktop and some files
current people allowed access to the main os: 
-Wyvern Lead 1 aka Arrax Eturnal
-Wyvern 2 aka Echo aka Bottom 2
-Wyvern 3 aka Eighty_Bity aka os creator

you should really remember that wyvern 3 since you did log in yourself here

write back to go back'''
            for character in about:
             sys.stdout.write(character)
             sys.stdout.flush()
             time.sleep(0.05)
            
            
            about_input = input('''
''')

            while True:
                if about_input.lower().strip() == 'back':
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
                                                                                                                                                        
Welcome back wyvern 3

what do you want to do?

desktop         internet        about''')
                    nav()
                else:
                    cls()
                    print('''I did not understand please type back to go back''')
                    about_input=input('''
''')    
         elif user1.lower().strip() == 'back':
            game.Game()
         else:
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
                                                                                                                                                        
Welcome back wyvern 3

I am sorry I didnt understand, please make sure you write what you want to do from these choices

desktop         internet        about''')
             nav()
def desktop():
    cls()
    error='''an error has occured please stand-by while we check stability
        
0%'''
    for character in error:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
    time.sleep(1)
    cls()
    print('''an error has occured please stand-by while we check stability

10%''')
    time.sleep(1)
    cls()
    print('''an error has occured please stand-by while we check stability

25%''')
    time.sleep(10)
    cls()
    error = '''os is unstable, some of the files have been saved in backup, do you wish to continue?(y/n)
'''
    for character in error:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
    while True:
        user = input()
        if user.lower().strip() in ['y','yes']:
            cls()
            mainDesktop1 = '''
  (`\ .-') /`                   (`-.      ('-.    _  .-')        .-') _                  
   `.( OO ),'                 _(OO  )_  _(  OO)  ( \( -O )      ( OO ) )                 
,--./  .--.    ,--.   ,--.,--(_/   ,. \(,------.  ,------.  ,--./ ,--,'         .-----.  
|      |  |     \  `.'  / \   \   /(__/ |  .---'  |   /`. ' |   \ |  |\        /  -.   \ 
|  |   |  |,  .-')     /   \   \ /   /  |  |      |  /  | | |    \|  | )       '-' _'  | 
|  |.'.|  |_)(OO  \   /     \   '   /, (|  '--.   |  |_.' | |  .     |/           |_  <  
|         |   |   /  /\_     \     /__) |  .--'   |  .  '.' |  |\    |         .-.  |  | 
|   ,'.   |   `-./  /.__)     \   /     |  `---.  |  |\  \  |  | \   |         \ `-'   / 
'--'   '--'     `--'           `-'      `------'  `--' '--' `--'  `--'          `----''  

confidential        users       wyverns.txt     

allies.txt          kos.txt     orders
for help type help
'''
            for character in mainDesktop1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.005)
            mainDesktop()
        elif user.lower().strip() in ['n','no']:
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
                                                                                                                                                        
Welcome back wyvern 3

what should we do?

desktop         internet        about''')
            nav()
        else:
            cls()
            print("please answer with y/n or yes/no")
def mainDesktop():
            cls()
            print('''
  (`\ .-') /`                   (`-.      ('-.    _  .-')        .-') _                  
   `.( OO ),'                 _(OO  )_  _(  OO)  ( \( -O )      ( OO ) )                 
,--./  .--.    ,--.   ,--.,--(_/   ,. \(,------.  ,------.  ,--./ ,--,'         .-----.  
|      |  |     \  `.'  / \   \   /(__/ |  .---'  |   /`. ' |   \ |  |\        /  -.   \ 
|  |   |  |,  .-')     /   \   \ /   /  |  |      |  /  | | |    \|  | )       '-' _'  | 
|  |.'.|  |_)(OO  \   /     \   '   /, (|  '--.   |  |_.' | |  .     |/           |_  <  
|         |   |   /  /\_     \     /__) |  .--'   |  .  '.' |  |\    |         .-.  |  | 
|   ,'.   |   `-./  /.__)     \   /     |  `---.  |  |\  \  |  | \   |         \ `-'   / 
'--'   '--'     `--'           `-'      `------'  `--' '--' `--'  `--'          `----''  

confidential        users       wyverns.txt     

allies.txt          kos.txt     orders
for help type help
''')
            while True:
                user = input()
                if user.lower().strip() =='help':
                    help.help()
                elif user.lower().startswith('cd'):
                    if user.endswith('confidential'):
                        confidential.conFile()
                    elif user.endswith('users'):
                         userfile.userdoc()
                    elif user.endswith('.txt') or user.endswith('orders'):
                         cls()
                         print('''
  (`\ .-') /`                   (`-.      ('-.    _  .-')        .-') _                  
   `.( OO ),'                 _(OO  )_  _(  OO)  ( \( -O )      ( OO ) )                 
,--./  .--.    ,--.   ,--.,--(_/   ,. \(,------.  ,------.  ,--./ ,--,'         .-----.  
|      |  |     \  `.'  / \   \   /(__/ |  .---'  |   /`. ' |   \ |  |\        /  -.   \ 
|  |   |  |,  .-')     /   \   \ /   /  |  |      |  /  | | |    \|  | )       '-' _'  | 
|  |.'.|  |_)(OO  \   /     \   '   /, (|  '--.   |  |_.' | |  .     |/           |_  <  
|         |   |   /  /\_     \     /__) |  .--'   |  .  '.' |  |\    |         .-.  |  | 
|   ,'.   |   `-./  /.__)     \   /     |  `---.  |  |\  \  |  | \   |         \ `-'   / 
'--'   '--'     `--'           `-'      `------'  `--' '--' `--'  `--'          `----''  

confidential        users       wyverns.txt     

allies.txt          kos.txt     orders
im sorry,''', user,'''is not a directory, did you mean to use cat?
''')
                    else:
                         cls()
                         print('''
  (`\ .-') /`                   (`-.      ('-.    _  .-')        .-') _                  
   `.( OO ),'                 _(OO  )_  _(  OO)  ( \( -O )      ( OO ) )                 
,--./  .--.    ,--.   ,--.,--(_/   ,. \(,------.  ,------.  ,--./ ,--,'         .-----.  
|      |  |     \  `.'  / \   \   /(__/ |  .---'  |   /`. ' |   \ |  |\        /  -.   \ 
|  |   |  |,  .-')     /   \   \ /   /  |  |      |  /  | | |    \|  | )       '-' _'  | 
|  |.'.|  |_)(OO  \   /     \   '   /, (|  '--.   |  |_.' | |  .     |/           |_  <  
|         |   |   /  /\_     \     /__) |  .--'   |  .  '.' |  |\    |         .-.  |  | 
|   ,'.   |   `-./  /.__)     \   /     |  `---.  |  |\  \  |  | \   |         \ `-'   / 
'--'   '--'     `--'           `-'      `------'  `--' '--' `--'  `--'          `----''  

confidential        users       wyverns.txt     

allies.txt          kos.txt     orders
no directory found
''')
                elif user.startswith('cat'):
                    if user.lower().endswith('wyverns.txt'):
                         wyverntxt.wyvernscript()
                    elif user.lower().endswith('allies.txt'):
                         allies.allies()
                    elif user.lower().endswith('kos.txt'):
                         kos.killOnSight()
                    elif user.lower().endswith('orders'):
                         orders.orders()
                else:
                     cls()
                     print('''
  (`\ .-') /`                   (`-.      ('-.    _  .-')        .-') _                  
   `.( OO ),'                 _(OO  )_  _(  OO)  ( \( -O )      ( OO ) )                 
,--./  .--.    ,--.   ,--.,--(_/   ,. \(,------.  ,------.  ,--./ ,--,'         .-----.  
|      |  |     \  `.'  / \   \   /(__/ |  .---'  |   /`. ' |   \ |  |\        /  -.   \ 
|  |   |  |,  .-')     /   \   \ /   /  |  |      |  /  | | |    \|  | )       '-' _'  | 
|  |.'.|  |_)(OO  \   /     \   '   /, (|  '--.   |  |_.' | |  .     |/           |_  <  
|         |   |   /  /\_     \     /__) |  .--'   |  .  '.' |  |\    |         .-.  |  | 
|   ,'.   |   `-./  /.__)     \   /     |  `---.  |  |\  \  |  | \   |         \ `-'   / 
'--'   '--'     `--'           `-'      `------'  `--' '--' `--'  `--'          `----''  

confidential        users       wyverns.txt     

allies.txt          kos.txt     orders


for help type help
''',
user, '''was not a valid input, type help for more help
''')
            
if __name__ == '__main__':
    nav()
    desktop()
    mainDesktop()