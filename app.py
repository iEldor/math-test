from random import randint
from threading import Timer
from pythoncom import CoInitialize
from common import *
import time

number_of_questions = 10
timeout = 10
assessment = []
timed_out = False


def set_timed_out():
    CoInitialize()
    global timed_out
    timed_out = True
    question['user_answer'] = None
    question['score'] = 'TIMED OUT'
    assessment.append(question)

    print('Sorry, but time ran out for this question. Please continue...')
    time.sleep(2)
    shell_send_keys('{ENTER}')


for i in range(1, number_of_questions + 1):
    factor_1 = randint(0,12)
    factor_2 = randint(0,12)
    product = factor_1 * factor_2

    question = {
        'id':i,
        'question': f'{factor_1} x {factor_2} = ',
        'answer': factor_1 * factor_2
    }

    timed_out = False
    while not timed_out:
        clear_screen()
        print_title('multiplications test'.upper())
        print(f'You are answering the question {i} out of {number_of_questions}\n')
        t = Timer(timeout, set_timed_out)
        t.start()
        user_answer = input(f"{question['question']}")
        try:
            user_answer = int(user_answer)
            t.cancel()
        except ValueError:
            continue
        else:
            question['user_answer'] = user_answer
            if question['answer'] == question['user_answer']:
                question['score'] = 'PASS'
                print('\nBingo!\n'.upper())
                time.sleep(1)
            else:
                question['score'] = 'FAIL'
                print('\nWhoopsie!\n'.upper())
                time.sleep(1)
            assessment.append(question)
            break

correct_answers = len([question['score'] for question in assessment if question['score'] == 'PASS'])
incorrect_answers = len([question['score'] for question in assessment if question['score'] == 'FAIL'])
timedout_questions = len([question['score'] for question in assessment if question['score'] == 'TIMED OUT'])

print(f'''
        Total Questions:    {number_of_questions}
        Correct Answers:    {correct_answers}
        Incorrect Answers:  {incorrect_answers}
        Timed Out:          {timedout_questions}
        Score:              {100*correct_answers/number_of_questions} %
''')

for question in assessment:
    print(f"{question['question']} = {question['answer']} | {question['user_answer']} | {question['score']}")