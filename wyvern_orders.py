import sys
import time
import getpass

def wyvernOrders():
    warning = '''a password is required to continue, be careful it is case sensitive
'''
    for characters in warning:
        sys.stdout.write(characters)
        sys.stdout.flush()
        time.sleep(0.05)
    password = getpass.getpass('Password:') 
if __name__ == '__main__':
    wyvernOrders()