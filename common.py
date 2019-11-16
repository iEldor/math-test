import os
from win32com.client import Dispatch

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_title(text):
    print('_'*(len(text) + 20))
    print()
    print(' '*10 + text + ' '*10)
    print('_'*(len(text) + 20))
    print()    


def shell_send_keys(text):
    shell = Dispatch('WScript.Shell')
    shell.SendKeys(text)
