import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_title(text):
    print('_'*(len(text) + 20))
    print()
    print(' '*10 + text + ' '*10)
    print('_'*(len(text) + 20))
    print()    