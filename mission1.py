import cls
import sys
import time

import newuserdesktop

def mission1():
    cls.cls()
    print('______________________________________________________________________________________________________________________________________________')
    debrief = '''codename: fox's den


Hello eighty, I will keep this brief, an enemy group has been spotted recently flying around the wyvern's base of operation
After talking with them we have come to a semi-agreement of trust
Today we will be going in their base, they have invited us for a party, it will give us plenty of time to do some reconnaissance

Do not go in with an undercover identity, stay as close to the delta fox lead and keep your ears open
If you understand this you will be allowed to be our reconnaissance lead tonight, I myself will be joining the
Event.

do not disapoint me wyvern 3, I trust you

-Wyvern Lead 1 aka Arrax Eturnal

ps. I hid the password to the next files in here.
'''
    for characters in debrief:
        sys.stdout.write(characters)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
    print('_________________________________________________________________________________________________________________________________________________')
    player = input('''Type back to go back
''')
if __name__ == '__main__':
    mission1()