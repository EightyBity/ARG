import sys
import time
import getpass

import wyverndesktop
from cls import cls

def userdoc():
    cls()
    passw='''A password is required, please enter the password to continue:
'''
    for character in passw:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.005)
    user = getpass.getpass()

    if user =='Te5t':
        cls()
        print('correct')
    if user.lower().strip() =='back':
        wyverndesktop.mainDesktop()
if __name__ == '__main__':
    userdoc()