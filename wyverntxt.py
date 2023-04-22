import wyverndesktop
import sys
import time
from cls import cls

def wyvernscript():
    cls()
    text='''I am drowning

Yes I am making progress, I am getting achievements and yet I still am drowning.

I try my best to make you all happy I want to stop I can't, I keep pushing I keep going
I am still here. I am smiling I am laughing and joking and yet I do not feel anymore
if what I am writting and doing is something or if im just living by the side letting
everything happen around me. Yet I am happy, I make you happy I make progress and small
achievements for me and for you all but what are those worth if I am losing myself in them I cannot stop
I cannot give up.

I am drowning

But it is for you

I am drowning

But it makes you happy

So I will keep drowning

So you can be happy.
--------------------------------------------------------------------------------------------------------------------
'''

    for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
    while True:
        user = input()

        if user.lower() == 'back':
             wyverndesktop.mainDesktop()
        else:
             cls()
             print('''I am drowning

Yes I am making progress, I am getting achievements and yet I still am drowning.

I try my best to make you all happy I want to stop I can't, I keep pushing I keep going
I am still here. I am smiling I am laughing and joking and yet I do not feel anymore
if what I am writting and doing is something or if im just living by the side letting
everything happen around me. Yet I am happy, I make you happy I make progress and small
achievements for me and for you all but what are those worth if I am losing myself in them I cannot stop
I cannot give up.

I am drowning

But it is for you

I am drowning

But it makes you happy

So I will keep drowning

So you can be happy.

--------------------------------------------------------------------------------------------------------------------
I did not get that, please type back to go back
''')


if __name__ == '__main__':
    wyvernscript()