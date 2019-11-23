# https://www.engageny.org/resource/released-2019-3-8-ela-and-mathematics-state-test-questions

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_title(text):
    print('_'*(len(text) + 20))
    print()
    print(' '*10 + text + ' '*10)
    print('_'*(len(text) + 20))
    print()


def print_multi_choice(options):
    for count, item in enumerate(options):
        print(f'{count + 1}) {item}')


def draw_array(x,y):
    print(' _' * x)
    for i in range(y):
        print('|'+'_|' * x)