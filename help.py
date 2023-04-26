import sys
import time

def help():
    help = '''type cd to move into folders
type cat to read txt files
some files might hide their extension
folders never have extenstions'''
    for character in help:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
if __name__ == '__main__':
    help()