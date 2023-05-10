import sys
import time
import getpass

import cls

def wyvernOrders():
    cls.cls()
    warning = '''a password is required to continue, be careful it is case sensitive
'''
    for characters in warning:
        sys.stdout.write(characters)
        sys.stdout.flush()
        time.sleep(0.05)
    password = getpass.getpass('Password:') 

    if password != 'Hat Die':
        cls.cls()
        wrong = '''Wrong password please try again'''
if __name__ == '__main__':
    wyvernOrders()