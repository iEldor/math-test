from threading import Timer
from pythoncom import CoInitialize
from common import *


out_of_time=False

def time_ran_out():
    CoInitialize()
    print('You didn\'t answer in time')
    out_of_time=True
    print('TIMED OUT')
    shell_send_keys('{ENTER}')

t=Timer(2,time_ran_out)
t.start()

user_input=input('Enter something: \n')

if user_input!=None and not out_of_time:
    print('this should appear only if input was given in 2 seconds...')
    t.cancel()